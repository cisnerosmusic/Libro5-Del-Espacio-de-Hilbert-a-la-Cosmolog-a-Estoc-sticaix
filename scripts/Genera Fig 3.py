#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera Fig. 3 — Observables efectivos:
Ω_φ(t), Ω_χ(t), w_total(t) + histograma de w_total (régimen tardío).

MODOS
1) Simulación directa:
   python scripts/gen_fig3_observables.py --simulate --steps 200000 --dt-sim 0.002 --seed 42

2) Desde CSV (t,phi,dphi,chi,dchi):
   python scripts/gen_fig3_observables.py --from-csv --phi-chi-csv data/state.csv
   # si el CSV no trae 't', especifica --dt

SALIDAS
- assets/fig3-observables.png
- assets/fig3-observables.csv           (t, Omega_phi, Omega_chi, w_total, w_ma)
- assets/fig3-stats.txt                 (resumen: <w>, var, etc.)

Autor: Ernesto Cisneros Cino — CC0 1.0 (Dominio público)
"""
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt

try:
    import pandas as pd
except ImportError:
    pd = None


# ----------------- Núcleo de modelo (coherente con Fig.1/2) -----------------
def V(phi, chi, params):
    mp2 = params["m_phi"]**2
    mc2 = params["m_chi"]**2
    lph = params["lambda_phi"]
    lch = params["lambda_chi"]
    g   = params["g"]
    V0  = params["V0"]
    return (
        -0.5 * mp2 * phi**2 + 0.25 * lph * phi**4
        + 0.5 * mc2 * chi**2 + 0.25 * lch * chi**4
        + 0.5 * (g**2) * phi**2 * chi**2 + V0
    )

def dV_dphi(phi, chi, params):
    mp2 = params["m_phi"]**2
    lph = params["lambda_phi"]
    g   = params["g"]
    return -mp2 * phi + lph * phi**3 + (g**2) * phi * chi**2

def dV_dchi(phi, chi, params):
    mc2 = params["m_chi"]**2
    lch = params["lambda_chi"]
    g   = params["g"]
    return mc2 * chi + lch * chi**3 + (g**2) * chi * phi**2

def H_from_state(dphi, dchi, phi, chi, params):
    energy = 0.5*(dphi**2 + dchi**2) + V(phi, chi, params)
    energy = np.maximum(energy, 1e-16)
    return np.sqrt(energy)

def default_params():
    return dict(
        m_phi=1.0, m_chi=1.2,
        lambda_phi=0.5, lambda_chi=0.4,
        g=0.7, V0=0.05,
        alpha_phi=0.08, alpha_chi=0.08,
        tau_phi=2.0,  tau_chi=2.0,
        phi0=0.9, chi0=0.4, dphi0=0.0, dchi0=0.0,
    )


# ----------------- Simulación mínima para obtener series -----------------
def simulate_series(steps=200000, dt=0.002, seed=42, burn_in=20000, params=None):
    if params is None:
        params = default_params()
    rng = np.random.default_rng(seed)

    phi, chi = params["phi0"], params["chi0"]
    dphi, dchi = params["dphi0"], params["dchi0"]
    zph, zch = 0.0, 0.0

    keep = steps - burn_in
    T    = np.arange(keep) * dt
    PHI  = np.empty(keep); CHI = np.empty(keep)
    DPHI = np.empty(keep); DCHI = np.empty(keep)

    for n in range(steps):
        Hn   = H_from_state(dphi, dchi, phi, chi, params)
        Tgh  = Hn/(2.0*np.pi)
        GamP = params["alpha_phi"] * 3.0 * Hn
        GamC = params["alpha_chi"] * 3.0 * Hn

        # OU zetas
        zph += (-zph/params["tau_phi"]) * dt + np.sqrt((2.0*GamP*Tgh)/(params["tau_phi"]**2) * dt) * rng.standard_normal()
        zch += (-zch/params["tau_chi"]) * dt + np.sqrt((2.0*GamC*Tgh)/(params["tau_chi"]**2) * dt) * rng.standard_normal()

        # Velocidades y campos
        dphi += (-3.0*Hn*dphi - dV_dphi(phi, chi, params) + zph) * dt
        dchi += (-3.0*Hn*dchi - dV_dchi(phi, chi, params) + zch) * dt
        phi  += dphi * dt
        chi  += dchi * dt

        if n >= burn_in:
            i = n - burn_in
            PHI[i]  = phi
            DPHI[i] = dphi
            CHI[i]  = chi
            DCHI[i] = dchi

    return T, PHI, DPHI, CHI, DCHI, dt


# ----------------- Cargar desde CSV externo -----------------
def load_from_csv(path, dt_cli=None):
    if pd is None:
        raise RuntimeError("Para --from-csv se requiere pandas (pip install pandas).")
    df = pd.read_csv(path)
    cols = [c.lower() for c in df.columns]

    def pick(name, alts):
        for cand in [name] + alts:
            if cand in cols:
                return df[df.columns[cols.index(cand)]].to_numpy()
        return None

    t = pick("t", ["time"])
    phi  = pick("phi",  ["ϕ"])
    dphi = pick("dphi", ["phi_dot","phidot","dphidt","ϕdot"])
    chi  = pick("chi",  [])
    dchi = pick("dchi", ["chi_dot","chidot","dchidt"])

    if phi is None or dphi is None or chi is None or dchi is None:
        # Posicional: t,phi,dphi,chi,dchi
        if df.shape[1] >= 5:
            t   = df.iloc[:,0].to_numpy()
            phi = df.iloc[:,1].to_numpy()
            dphi= df.iloc[:,2].to_numpy()
            chi = df.iloc[:,3].to_numpy()
            dchi= df.iloc[:,4].to_numpy()
        else:
            raise ValueError("CSV debe contener columnas (t, phi, dphi, chi, dchi).")

    if t is None:
        if dt_cli is None:
            raise ValueError("CSV no tiene columna de tiempo; indique --dt.")
        t = np.arange(len(phi)) * dt_cli

    dt = float(np.mean(np.diff(t)))
    return t, phi, dphi, chi, dchi, dt


# ----------------- Observables efectivos -----------------
def observables(phi, dphi, chi, dchi, params):
    Vtot = V(phi, chi, params)
    Vphi = (-0.5 * params["m_phi"]**2 * phi**2 + 0.25 * params["lambda_phi"] * phi**4) + 0.5*(params["g"]**2)*phi**2*chi**2/2.0*2.0
    # Nota: para separar V_phi y V_chi de forma "atributiva", repartimos el término de acoplamiento φ^2 χ^2 a partes iguales.
    Vphi = -0.5 * params["m_phi"]**2 * phi**2 + 0.25 * params["lambda_phi"] * phi**4 + 0.25 * (params["g"]**2) * phi**2 * chi**2
    Vchi =  0.5 * params["m_chi"]**2 * chi**2 + 0.25 * params["lambda_chi"] * chi**4 + 0.25 * (params["g"]**2) * phi**2 * chi**2

    rho_phi = 0.5 * dphi**2 + Vphi
    rho_chi = 0.5 * dchi**2 + Vchi
    rho = rho_phi + rho_chi

    p = 0.5*(dphi**2 + dchi**2) - (Vphi + Vchi)
    # Evitar divisiones por 0:
    rho_safe = np.where(rho <= 1e-16, 1e-16, rho)
    w_total = p / rho_safe

    Omega_phi = rho_phi / rho_safe
    Omega_chi = rho_chi / rho_safe
    return Omega_phi, Omega_chi, w_total


def moving_average(x, M):
    if M <= 1:
        return x
    kernel = np.ones(M) / M
    return np.convolve(x, kernel, mode="same")


# ----------------- Figura y guardados -----------------
def plot_observables(t, Omega_phi, Omega_chi, w_total, w_ma, out_png, out_csv, out_txt,
                     hist_frac=0.4):
    """
    hist_frac: fracción final de la serie usada para el histograma (régimen tardío).
    """
    os.makedirs(os.path.dirname(out_png), exist_ok=True)

    # Guardar CSV
    arr = np.column_stack([t, Omega_phi, Omega_chi, w_total, w_ma])
    np.savetxt(out_csv, arr, delimiter=",", header="t,Omega_phi,Omega_chi,w_total,w_ma", comments="", fmt="%.9g")

    # Stats tardías
    N = len(w_total)
    n_tail = max(100, int(hist_frac * N))
    tail = w_total[-n_tail:]
    mean_w = float(np.mean(tail))
    var_w  = float(np.var(tail))
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write("Resumen de observables (régimen tardío)\n")
        f.write(f"<w>_tail = {mean_w:.6g}\n")
        f.write(f"Var(w)_tail = {var_w:.6g}\n")
        f.write(f"Ventana de suavizado (puntos) = usado en w_ma\n")

    # Figura: serie temporal + histograma
    fig, axes = plt.subplots(2, 1, figsize=(8, 7), gridspec_kw={"height_ratios":[2.2,1]}, sharex=False)

    ax = axes[0]
    ax.plot(t, Omega_phi, label=r"$\Omega_\phi$", linewidth=1.5)
    ax.plot(t, Omega_chi, label=r"$\Omega_\chi$", linewidth=1.5)
    ax.plot(t, w_total, label=r"$w_{\mathrm{total}}$", linewidth=1.0, alpha=0.6)
    ax.plot(t, w_ma, label=r"$\overline{w}_{\mathrm{total}}$ (móvil)", linewidth=1.8)
    ax.set_ylabel(r"Fracciones / $w_{\mathrm{total}}$")
    ax.set_title("Fig. 3 – $\Omega_\phi$, $\Omega_\chi$, $w_{\\mathrm{total}}$ y su promedio móvil")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")

    ax2 = axes[1]
    ax2.hist(tail, bins=40, density=True, alpha=0.8)
    ax2.set_xlabel("w_total (tardío)")
    ax2.set_ylabel("Densidad")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_png, dpi=220)
    plt.close()
    print(f"[OK] Guardado: {out_png}\n[OK] CSV: {out_csv}\n[OK] Stats: {out_txt}")


# ----------------- CLI -----------------
def main():
    ap = argparse.ArgumentParser(description="Fig.3: Ω_φ, Ω_χ, w_total y su histograma (régimen tardío).")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--simulate", action="store_true", help="Simula y genera la figura.")
    mode.add_argument("--from-csv", action="store_true", help="Carga series desde CSV y genera la figura.")
    ap.add_argument("--phi-chi-csv", type=str, default=None, help="CSV con t,phi,dphi,chi,dchi.")
    ap.add_argument("--dt", type=float, default=None, help="Paso de tiempo (si CSV no trae t).")
    ap.add_argument("--steps", type=int, default=200000, help="Pasos (simulación).")
    ap.add_argument("--burn-in", type=int, default=20000, help="Descartar pasos iniciales.")
    ap.add_argument("--dt-sim", type=float, default=0.002, help="Δt (simulación).")
    ap.add_argument("--seed", type=int, default=42, help="Semilla RNG.")
    ap.add_argument("--ma-window", type=int, default=2000, help="Ventana de media móvil (puntos).")
    ap.add_argument("--hist-frac", type=float, default=0.4, help="Fracción final para histograma.")
    ap.add_argument("--out", type=str, default="assets/fig3-observables.png", help="PNG de salida.")
    ap.add_argument("--out-csv", type=str, default="assets/fig3-observables.csv", help="CSV de salida.")
    ap.add_argument("--out-txt", type=str, default="assets/fig3-stats.txt", help="TXT de métricas.")

    # overrides del modelo
    for k in ["m_phi","m_chi","lambda_phi","lambda_chi","g","V0",
              "alpha_phi","alpha_chi","tau_phi","tau_chi",
              "phi0","chi0","dphi0","dchi0"]:
        ap.add_argument(f"--{k}", type=float, default=None)

    args = ap.parse_args()
    params = default_params()
    for k in ["m_phi","m_chi","lambda_phi","lambda_chi","g","V0",
              "alpha_phi","alpha_chi","tau_phi","tau_chi",
              "phi0","chi0","dphi0","dchi0"]:
        v = getattr(args, k)
        if v is not None:
            params[k] = v

    if args.from_csv:
        if not args.phi_chi_csv:
            raise ValueError("Use --phi-chi-csv con su archivo CSV.")
        t, phi, dphi, chi, dchi, dt = load_from_csv(args.phi_chi_csv, dt_cli=args.dt)
    else:
        t, phi, dphi, chi, dchi, dt = simulate_series(steps=args.steps, dt=args.dt_sim,
                                                      seed=args.seed, burn_in=args.burn_in, params=params)

    Om_phi, Om_chi, w = observables(phi, dphi, chi, dchi, params)
    w_ma = moving_average(w, max(1, int(args.ma_window)))

    plot_observables(t, Om_phi, Om_chi, w, w_ma,
                     args.out, args.out_csv, args.out_txt,
                     hist_frac=args.hist_frac)


if __name__ == "__main__":
    main()

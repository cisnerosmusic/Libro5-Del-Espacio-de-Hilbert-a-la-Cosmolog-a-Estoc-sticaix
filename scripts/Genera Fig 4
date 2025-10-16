#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fig. 4 — Barrido en τ: curvas Q(τ) y σ_w(τ) para el modelo de dos campos con ruido OU.
- Para cada τ en una lista, ejecuta N_real simulaciones (semillas distintas).
- Computa:   Q(τ)  = f0 / Δf  (del espectro de φ, χ o promedio)
             σ_w(τ) = Var(w_total) en régimen tardío

SALIDAS:
- assets/fig4-memoria.png   (curvas Q(τ) y σ_w(τ) vs τ)
- assets/fig4-memoria.csv   (tabla: tau, Q_mean, Q_std, sigma_w_mean, sigma_w_std, f0_mean, delf_mean)
- assets/fig4-memoria.txt   (resumen)

USO (ejemplos):
  python scripts/gen_fig4_barrido_tau.py --tau-list 0,0.5,1,2,3,5 --n-real 8 --steps 160000 --dt 0.002
  python scripts/gen_fig4_barrido_tau.py --tau-list 0,0.5,1,2,3,5 --metric-source avg --n-real 12

Autor: Ernesto Cisneros Cino — CC0 1.0 (Dominio público)
"""
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt

# ---------- Núcleo común (consistente con Fig.1/2/3) ----------
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

# ---------- Simulación: devuelve φ(t), χ(t), w_total(t) ----------
def simulate_series(steps=160000, dt=0.002, seed=42, burn_in=20000, params=None):
    if params is None:
        params = default_params()
    rng = np.random.default_rng(seed)

    phi, chi = params["phi0"], params["chi0"]
    dphi, dchi = params["dphi0"], params["dchi0"]
    zph, zch = 0.0, 0.0

    keep = steps - burn_in
    PHI = np.empty(keep); CHI = np.empty(keep)
    W   = np.empty(keep)

    for n in range(steps):
        Hn   = H_from_state(dphi, dchi, phi, chi, params)
        Tgh  = Hn / (2.0*np.pi)
        GamP = params["alpha_phi"] * 3.0 * Hn
        GamC = params["alpha_chi"] * 3.0 * Hn

        # OU
        zph += (-zph/params["tau_phi"]) * dt + np.sqrt((2.0*GamP*Tgh)/(params["tau_phi"]**2) * dt) * rng.standard_normal()
        zch += (-zch/params["tau_chi"]) * dt + np.sqrt((2.0*GamC*Tgh)/(params["tau_chi"]**2) * dt) * rng.standard_normal()

        # ecuaciones de movimiento
        dphi += (-3.0*Hn*dphi - dV_dphi(phi, chi, params) + zph) * dt
        dchi += (-3.0*Hn*dchi - dV_dchi(phi, chi, params) + zch) * dt
        phi  += dphi * dt
        chi  += dchi * dt

        if n >= burn_in:
            i = n - burn_in
            PHI[i] = phi
            CHI[i] = chi
            # w_total en línea (atribución mitad-mitad del acoplamiento)
            Vphi = -0.5*params["m_phi"]**2 * phi**2 + 0.25*params["lambda_phi"]*phi**4 + 0.25*(params["g"]**2)*phi**2*chi**2
            Vchi =  0.5*params["m_chi"]**2 * chi**2 + 0.25*params["lambda_chi"]*chi**4 + 0.25*(params["g"]**2)*phi**2*chi**2
            rho_phi = 0.5*dphi**2 + Vphi
            rho_chi = 0.5*dchi**2 + Vchi
            rho = rho_phi + rho_chi
            p   = 0.5*(dphi**2 + dchi**2) - (Vphi + Vchi)
            rho_safe = rho if rho > 1e-16 else 1e-16
            W[i] = p / rho_safe

    return PHI, CHI, W

# ---------- Espectro y Q ----------
def power_spectrum(x, dt):
    x = np.asarray(x, float)
    x = x - np.mean(x)
    N = x.size
    window = np.hanning(N)
    Xf = np.fft.rfft(x * window)
    psd = (np.abs(Xf)**2) / np.sum(window**2)
    freqs = np.fft.rfftfreq(N, dt)
    # normalizar para comparar
    m = psd.max() if psd.max() > 0 else 1.0
    return freqs, psd/m

def interp_half(x1, y1, x2, y2, yhalf):
    if x2 == x1:
        return x1
    a = (y2 - y1) / (x2 - x1)
    if a == 0:
        return 0.5*(x1+x2)
    return x1 + (yhalf - y1)/a

def peak_and_width(freqs, psd):
    start = 1 if freqs[0] == 0 else 0
    idx = start + np.argmax(psd[start:])
    f0 = freqs[idx]; p0 = psd[idx]
    if p0 <= 0:
        return f0, np.nan, np.nan
    half = 0.5 * p0
    # izquierda
    iL = idx
    while iL > 0 and psd[iL] >= half:
        iL -= 1
    fL = np.nan if iL == idx else interp_half(freqs[iL], psd[iL], freqs[iL+1], psd[iL+1], half)
    # derecha
    iR = idx
    while iR < len(psd)-1 and psd[iR] >= half:
        iR += 1
    fR = np.nan if iR == idx else interp_half(freqs[iR-1], psd[iR-1], freqs[iR], psd[iR], half)

    if np.isnan(fL) or np.isnan(fR):
        return f0, np.nan, np.nan
    delf = max(fR - fL, 1e-16)
    Q = f0 / delf
    return f0, delf, Q

# ---------- Barrido ----------
def run_sweep(tau_list, n_real=8, steps=160000, dt=0.002, burn_in=20000,
              base_params=None, metric_source="avg", tail_frac=0.4, seed0=100):
    """
    metric_source: 'phi' | 'chi' | 'avg'  (de dónde sacar Q)
    tail_frac: fracción tardía usada para σ_w
    """
    if base_params is None:
        base_params = default_params()
    results = []

    for tau in tau_list:
        Q_vals = []; f0_vals = []; delf_vals = []; sigw_vals = []
        for r in range(n_real):
            params = dict(base_params)
            params["tau_phi"] = float(tau)
            params["tau_chi"] = float(tau)
            # semillas distintas
            seed = seed0 + 7919*r + int(37*tau)

            phi, chi, w = simulate_series(steps=steps, dt=dt, seed=seed, burn_in=burn_in, params=params)

            # Q(τ)
            freqs, psd_phi = power_spectrum(phi, dt)
            _,     psd_chi = power_spectrum(chi, dt)
            if metric_source == "phi":
                f0, delf, Q = peak_and_width(freqs, psd_phi)
            elif metric_source == "chi":
                f0, delf, Q = peak_and_width(freqs, psd_chi)
            else:  # avg
                psd_avg = 0.5*(psd_phi + psd_chi)
                f0, delf, Q = peak_and_width(freqs, psd_avg)

            # σ_w(τ) en tardío
            N = len(w); n_tail = max(100, int(tail_frac*N))
            tail = w[-n_tail:]
            sigw = float(np.var(tail))

            Q_vals.append(Q); f0_vals.append(f0); delf_vals.append(delf); sigw_vals.append(sigw)

        # promedios y dispersión por τ
        Q_vals   = np.array(Q_vals, float)
        f0_vals  = np.array(f0_vals, float)
        delf_vals= np.array(delf_vals, float)
        sigw_vals= np.array(sigw_vals, float)

        results.append(dict(
            tau=float(tau),
            Q_mean=float(np.nanmean(Q_vals)),
            Q_std =float(np.nanstd(Q_vals, ddof=1)),
            f0_mean=float(np.nanmean(f0_vals)),
            delf_mean=float(np.nanmean(delf_vals)),
            sigma_w_mean=float(np.nanmean(sigw_vals)),
            sigma_w_std =float(np.nanstd(sigw_vals, ddof=1))
        ))

    return results

# ---------- Guardado y figura ----------
def save_results_and_plot(results, out_png, out_csv, out_txt):
    os.makedirs(os.path.dirname(out_png), exist_ok=True)
    # ordenar por τ
    results = sorted(results, key=lambda d: d["tau"])
    # CSV
    import csv
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["tau","Q_mean","Q_std","f0_mean","delf_mean","sigma_w_mean","sigma_w_std"])
        for r in results:
            w.writerow([r["tau"], r["Q_mean"], r["Q_std"], r["f0_mean"], r["delf_mean"], r["sigma_w_mean"], r["sigma_w_std"]])
    # TXT
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write("Barrido en tau: métricas promedio y desviaciones (N_real por punto)\n")
        for r in results:
            f.write(f"tau={r['tau']:>5g} | Q={r['Q_mean']:.4g}±{r['Q_std']:.3g} | σ_w={r['sigma_w_mean']:.4g}±{r['sigma_w_std']:.3g}\n")
    # Figura (dos ejes: Q y sigma_w)
    tau = np.array([r["tau"] for r in results], float)
    Qm  = np.array([r["Q_mean"] for r in results], float)
    Qe  = np.array([r["Q_std"]  for r in results], float)
    Swm = np.array([r["sigma_w_mean"] for r in results], float)
    Swe = np.array([r["sigma_w_std"]  for r in results], float)

    fig, ax1 = plt.subplots(figsize=(8, 6))
    ax1.errorbar(tau, Qm, yerr=Qe, fmt="o-", linewidth=1.6, capsize=3, label="Q(τ)")
    ax1.set_xlabel(r"$\tau$")
    ax1.set_ylabel(r"$Q=f_0/\Delta f$")
    ax1.grid(True, which="both", alpha=0.3)

    ax2 = ax1.twinx()
    ax2.errorbar(tau, Swm, yerr=Swe, fmt="s--", linewidth=1.6, capsize=3, color="tab:orange", label=r"$\sigma_w(\tau)$")
    ax2.set_ylabel(r"$\sigma_w$ (varianza tardía)")

    # Leyendas combinadas
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1+lines2, labels1+labels2, loc="best")

    plt.title("Fig. 4 — Barrido en $\\tau$: coherencia $Q(\\tau)$ y estabilidad $\\sigma_w(\\tau)$")
    plt.tight_layout()
    plt.savefig(out_png, dpi=220)
    plt.close()
    print(f"[OK] Guardados:\n- {out_png}\n- {out_csv}\n- {out_txt}")

# ---------- CLI ----------
def parse_tau_list(s):
    try:
        return [float(x.strip()) for x in s.split(",") if x.strip()!=""]
    except Exception as e:
        raise argparse.ArgumentTypeError(f"Lista τ inválida: {s}") from e

def main():
    ap = argparse.ArgumentParser(description="Fig.4: Barrido en τ → Q(τ) y σ_w(τ).")
    ap.add_argument("--tau-list", type=parse_tau_list, default=[0,0.5,1,2,3,5], help="Lista de τ separada por comas.")
    ap.add_argument("--n-real", type=int, default=8, help="Repeticiones por τ (semillas distintas).")
    ap.add_argument("--steps", type=int, default=160000, help="Pasos de simulación totales.")
    ap.add_argument("--burn-in", type=int, default=20000, help="Pasos a descartar al inicio.")
    ap.add_argument("--dt", type=float, default=0.002, help="Paso de tiempo Δt.")
    ap.add_argument("--metric-source", choices=["phi","chi","avg"], default="avg", help="De qué serie sacar Q (φ, χ o promedio).")
    ap.add_argument("--tail-frac", type=float, default=0.4, help="Fracción tardía para σ_w.")
    ap.add_argument("--seed0", type=int, default=100, help="Semilla base para generar semillas por repetición.")
    ap.add_argument("--out", type=str, default="assets/fig4-memoria.png", help="PNG de salida.")
    ap.add_argument("--out-csv", type=str, default="assets/fig4-memoria.csv", help="CSV de salida.")
    ap.add_argument("--out-txt", type=str, default="assets/fig4-memoria.txt", help="TXT resumen.")

    # Overrides de parámetros del modelo (opcionales)
    for k in ["m_phi","m_chi","lambda_phi","lambda_chi","g","V0",
              "alpha_phi","alpha_chi","phi0","chi0","dphi0","dchi0"]:
        ap.add_argument(f"--{k}", type=float, default=None)

    args = ap.parse_args()

    base = default_params()
    for k in ["m_phi","m_chi","lambda_phi","lambda_chi","g","V0",
              "alpha_phi","alpha_chi","phi0","chi0","dphi0","dchi0"]:
        v = getattr(args, k)
        if v is not None:
            base[k] = v

    results = run_sweep(
        tau_list=args.tau_list, n_real=args.n_real,
        steps=args.steps, dt=args.dt, burn_in=args.burn_in,
        base_params=base, metric_source=args.metric_source,
        tail_frac=args.tail_frac, seed0=args.seed0
    )
    save_results_and_plot(results, args.out, args.out_csv, args.out_txt)

if __name__ == "__main__":
    main()

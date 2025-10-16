#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera Fig. 2 — Espectro de potencia (phi(t), chi(t)) y estima f0, Δf, Q=f0/Δf.
Soporta simulación directa (Euler–Maruyama) o carga desde CSV.

USO
1) Simulación directa:
   python scripts/gen_fig2_espectro.py --simulate --steps 200000 --dt 0.002 --seed 42

2) Desde CSV (t,phi,dphi,chi,dchi):
   python scripts/gen_fig2_espectro.py --from-csv --phi-chi-csv data/state.csv
   # si el CSV no tiene 't', indica --dt explícitamente

SALIDAS
- assets/fig2-espectro.png        (gráfica del espectro normalizado)
- assets/fig2-metrics.txt         (valores f0, Δf, Q por serie)
- assets/fig2-spectrum.csv        (frecuencia, PSD_phi_norm, PSD_chi_norm)

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


# ----------------- Utilidades del modelo (mismo núcleo que Fig.1) -----------------
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

def simulate_series(steps=200000, dt=0.002, seed=42, burn_in=20000, params=None):
    """Devuelve arreglos de tiempo t, phi(t), chi(t) tras burn-in."""
    if params is None:
        params = default_params()
    rng = np.random.default_rng(seed)

    phi, chi = params["phi0"], params["chi0"]
    dphi, dchi = params["dphi0"], params["dchi0"]
    zph, zch = 0.0, 0.0

    keep = steps - burn_in
    PHI = np.empty(keep); CHI = np.empty(keep)
    T   = np.arange(keep) * dt  # relativo tras burn-in

    for n in range(steps):
        Hn   = H_from_state(dphi, dchi, phi, chi, params)
        Tgh  = Hn/(2.0*np.pi)
        GamP = params["alpha_phi"] * 3.0 * Hn
        GamC = params["alpha_chi"] * 3.0 * Hn

        zph += (-zph/params["tau_phi"]) * dt + np.sqrt((2.0*GamP*Tgh)/(params["tau_phi"]**2) * dt) * rng.standard_normal()
        zch += (-zch/params["tau_chi"]) * dt + np.sqrt((2.0*GamC*Tgh)/(params["tau_chi"]**2) * dt) * rng.standard_normal()

        dphi += (-3.0*Hn*dphi - dV_dphi(phi, chi, params) + zph) * dt
        dchi += (-3.0*Hn*dchi - dV_dchi(phi, chi, params) + zch) * dt

        phi  += dphi * dt
        chi  += dchi * dt

        if n >= burn_in:
            idx = n - burn_in
            PHI[idx] = phi
            CHI[idx] = chi

    return T, PHI, CHI


# ----------------- Espectro y métricas -----------------
def power_spectrum(x, dt):
    """PSD normalizada (0..Nyquist) con ventana Hann. Devuelve freqs, psd."""
    x = np.asarray(x, dtype=float)
    x = x - np.mean(x)
    N = x.size
    if N < 8:
        raise ValueError("Serie demasiado corta para FFT.")
    window = np.hanning(N)
    xw = x * window
    # Escala para energía ~ correcta (no crítico: normalizamos luego)
    Xf = np.fft.rfft(xw)
    psd = (np.abs(Xf)**2) / (np.sum(window**2))
    freqs = np.fft.rfftfreq(N, dt)
    # Normalizamos cada PSD por su máximo para compararlas en una misma escala
    m = psd.max() if psd.max() > 0 else 1.0
    return freqs, psd / m

def peak_and_width(freqs, psd):
    """Encuentra pico principal (excluye f=0) y calcula Δf (ancho a media altura) por interpolación lineal."""
    if len(freqs) != len(psd):
        raise ValueError("freqs y psd deben tener misma longitud.")
    # excluir f=0
    start = 1 if freqs[0] == 0 else 0
    idx_peak = start + np.argmax(psd[start:])
    f0 = freqs[idx_peak]
    p0 = psd[idx_peak]
    if p0 <= 0:
        return f0, np.nan, np.nan  # sin potencia
    half = 0.5 * p0

    # izquierda
    iL = idx_peak
    while iL > 0 and psd[iL] >= half:
        iL -= 1
    if iL == idx_peak:
        fL = np.nan
    else:
        # interpolación entre (iL, iL+1)
        fL = interp_half(freqs[iL], psd[iL], freqs[iL+1], psd[iL+1], half)

    # derecha
    iR = idx_peak
    while iR < len(psd)-1 and psd[iR] >= half:
        iR += 1
    if iR == idx_peak:
        fR = np.nan
    else:
        # interpolación entre (iR-1, iR)
        fR = interp_half(freqs[iR-1], psd[iR-1], freqs[iR], psd[iR], half)

    if np.isnan(fL) or np.isnan(fR):
        return f0, np.nan, np.nan
    delf = max(fR - fL, 1e-16)  # evitar cero
    Q = f0 / delf
    return f0, delf, Q

def interp_half(x1, y1, x2, y2, yhalf):
    """Interpolación lineal para hallar x donde y=yhalf entre (x1,y1) y (x2,y2)."""
    if x2 == x1:
        return x1
    a = (y2 - y1) / (x2 - x1)
    if a == 0:
        return (x1 + x2) * 0.5
    return x1 + (yhalf - y1) / a


# ----------------- Carga CSV -----------------
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
    chi  = pick("chi",  [])
    if phi is None or chi is None:
        # Intento posicional: t,phi,dphi,chi,dchi
        if df.shape[1] >= 5:
            t   = df.iloc[:,0].to_numpy()
            phi = df.iloc[:,1].to_numpy()
            chi = df.iloc[:,3].to_numpy()
        else:
            raise ValueError("CSV debe contener columnas (t, phi, ..., chi, ...).")
    if t is None:
        if dt_cli is None:
            raise ValueError("CSV no tiene columna de tiempo; indica --dt.")
        t = np.arange(len(phi)) * dt_cli

    # derivar dt medio del CSV
    dt = float(np.mean(np.diff(t)))
    return t, phi, chi, dt


# ----------------- Plot y guardados -----------------
def plot_and_save(freqs, psd_phi, psd_chi, metrics_phi, metrics_chi, out_png, out_csv, out_txt):
    os.makedirs(os.path.dirname(out_png), exist_ok=True)

    # Guardar CSV con espectros (normalizados)
    arr = np.column_stack([freqs, psd_phi, psd_chi])
    np.savetxt(out_csv, arr, delimiter=",", header="f,PSD_phi_norm,PSD_chi_norm", comments="")

    # Guardar métricas
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write("Métricas espectrales (pico principal y ancho a media altura)\n")
        f.write(f"phi(t):  f0={metrics_phi[0]:.6g},  Δf={metrics_phi[1]:.6g},  Q={metrics_phi[2]:.6g}\n")
        f.write(f"chi(t):  f0={metrics_chi[0]:.6g},  Δf={metrics_chi[1]:.6g},  Q={metrics_chi[2]:.6g}\n")

    # Figura
    plt.figure(figsize=(8, 6))
    plt.plot(freqs, psd_phi, label=r"PSD $\phi(t)$ (norm.)", linewidth=1.6)
    plt.plot(freqs, psd_chi, label=r"PSD $\chi(t)$ (norm.)", linewidth=1.6, linestyle="--")

    # Marcar picos y anchos
    for color, (f0, delf, Q), name in zip(["C0", "C1"], [metrics_phi, metrics_chi], [r"$\phi$", r"$\chi$"]):
        if np.isfinite(f0) and np.isfinite(delf):
            half = 0.5
            plt.axvline(f0, color=color, alpha=0.6, linestyle=":")
            plt.hlines(half, f0 - delf/2, f0 + delf/2, color=color, alpha=0.6)
            plt.text(f0, 0.55, f"{name}: f0={f0:.3g}, Δf={delf:.3g}, Q={Q:.2f}",
                     rotation=90, va="bottom", ha="center", fontsize=9, color=color)

    plt.xlabel("Frecuencia")
    plt.ylabel("PSD (normalizada)")
    plt.title("Fig. 2 – Espectro de potencia (pico $f_0$, ancho $\\Delta f$ y $Q=f_0/\\Delta f$)")
    plt.grid(True, alpha=0.3)
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig(out_png, dpi=220)
    plt.close()
    print(f"[OK] Guardado: {out_png}\n[OK] Métricas: {out_txt}\n[OK] CSV espectro: {out_csv}")


# ----------------- CLI -----------------
def main():
    ap = argparse.ArgumentParser(description="Fig.2: espectro de potencia y métricas (f0, Δf, Q).")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--simulate", action="store_true", help="Simula Euler–Maruyama y calcula el espectro.")
    mode.add_argument("--from-csv", action="store_true", help="Carga series desde CSV y calcula el espectro.")
    ap.add_argument("--phi-chi-csv", type=str, default=None, help="Ruta al CSV con t,phi,dphi,chi,dchi.")
    ap.add_argument("--dt", type=float, default=None, help="Paso de tiempo (solo si CSV no trae t).")
    ap.add_argument("--steps", type=int, default=200000, help="Pasos de simulación.")
    ap.add_argument("--burn-in", type=int, default=20000, help="Descartar pasos iniciales.")
    ap.add_argument("--dt-sim", type=float, default=0.002, help="Δt (simulación).")
    ap.add_argument("--seed", type=int, default=42, help="Semilla RNG.")
    ap.add_argument("--out", type=str, default="assets/fig2-espectro.png", help="PNG de salida.")
    ap.add_argument("--out-csv", type=str, default="assets/fig2-spectrum.csv", help="CSV de salida.")
    ap.add_argument("--out-txt", type=str, default="assets/fig2-metrics.txt", help="TXT de métricas.")

    # overrides de parámetros del modelo (opcional)
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
            raise ValueError("Usa --phi-chi-csv con la ruta a tu archivo CSV.")
        t, phi, chi, dt = load_from_csv(args.phi_chi_csv, dt_cli=args.dt)
    else:
        t, phi, chi = simulate_series(steps=args.steps, dt=args.dt_sim,
                                      seed=args.seed, burn_in=args.burn_in, params=params)
        dt = args.dt_sim

    # Espectros
    f_phi, psd_phi = power_spectrum(phi, dt)
    f_chi, psd_chi = power_spectrum(chi, dt)

    # Ajustar rejillas de frecuencia (interpolar si hiciera falta)
    if not np.array_equal(f_phi, f_chi):
        # Interpolar chi al grid de phi (simple y suficiente)
        psd_chi = np.interp(f_phi, f_chi, psd_chi)
        f = f_phi
    else:
        f = f_phi

    metrics_phi = peak_and_width(f, psd_phi)
    metrics_chi = peak_and_width(f, psd_chi)

    plot_and_save(f, psd_phi, psd_chi, metrics_phi, metrics_chi,
                  args.out, args.out_csv, args.out_txt)


if __name__ == "__main__":
    main()

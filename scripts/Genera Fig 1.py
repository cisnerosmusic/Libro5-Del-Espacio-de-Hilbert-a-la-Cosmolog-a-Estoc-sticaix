#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera Fig. 1 — Diagramas de fase (ciclos límite estocásticos) para el modelo de dos campos
con ruido OU ligado a T_GH = H/(2π).

MODOS DE USO
1) Simulación directa (Euler–Maruyama):
   python scripts/gen_fig1_fase.py --simulate --steps 200000 --dt 0.002 --seed 42

2) Cargar datos desde CSVs:
   python scripts/gen_fig1_fase.py --from-csv --phi-chi-csv data/state.csv
   # state.csv debe tener columnas: t,phi,dphi,chi,dchi (en ese orden o con encabezados)

SALIDA
- assets/fig1-fase.png (por defecto; editable con --out)

Autor: Ernesto Cisneros Cino (CC0 1.0 Dominio Público)
"""
import argparse
import os
import numpy as np

try:
    import pandas as pd
except ImportError:
    pd = None

import matplotlib.pyplot as plt


# ---------- Utilidades del modelo ----------
def V(phi, chi, params):
    """Potencial acoplado:
    V = -1/2 m_phi^2 phi^2 + (lambda_phi/4) phi^4 + 1/2 m_chi^2 chi^2 + (lambda_chi/4) chi^4 + 1/2 g^2 phi^2 chi^2 + V0
    """
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
    """Friedmann: H = sqrt( 1/2 (dphi^2 + dchi^2) + V )"""
    energy = 0.5*(dphi**2 + dchi**2) + V(phi, chi, params)
    energy = np.maximum(energy, 1e-16)  # evitar negativos numéricos
    return np.sqrt(energy)


# ---------- Simulación Euler–Maruyama ----------
def simulate_trajectories(steps=200000, dt=0.002, seed=42, burn_in=20000, params=None):
    """
    Integra las SDE con:
        zeta OU:  zeta_{i}^{n+1} = zeta_{i}^n - (dt/tau_i) zeta_{i}^n + sqrt( 2 Γ_i^n T_GH^n / tau_i^2 * dt ) * N(0,1)
        velocidades: dot{x}^{n+1} = dot{x}^n + (-3H^n dot{x}^n - dV/dx + zeta_i^n) dt
        campos:     x^{n+1} = x^n + dot{x}^{n+1} dt
        cierre:     H^{n+1} = sqrt( 1/2 (dot{phi}^{n+1}^2 + dot{chi}^{n+1}^2) + V(phi^{n+1}, chi^{n+1}) )
                    T_GH = H / (2π)
                    Γ_i^n = α_i * 3 H^n

    Devuelve arrays numpy con las trayectorias (descartando burn-in).
    """
    if params is None:
        params = default_params()

    rng = np.random.default_rng(seed)

    # Estado inicial
    phi  = params["phi0"]
    chi  = params["chi0"]
    dphi = params["dphi0"]
    dchi = params["dchi0"]
    zph  = 0.0  # ζ_φ
    zch  = 0.0  # ζ_χ

    # Buffers
    keep = steps - burn_in
    PHI  = np.empty(keep, dtype=float)
    DPHI = np.empty(keep, dtype=float)
    CHI  = np.empty(keep, dtype=float)
    DCHI = np.empty(keep, dtype=float)

    # Integración
    for n in range(steps):
        # Geometría/ruido (usar H^n)
        Hn   = H_from_state(dphi, dchi, phi, chi, params)
        Tgh  = Hn / (2.0*np.pi)
        GamP = params["alpha_phi"] * 3.0 * Hn
        GamC = params["alpha_chi"] * 3.0 * Hn

        # OU para zetas
        zph += (-zph/params["tau_phi"]) * dt + np.sqrt((2.0*GamP*Tgh)/(params["tau_phi"]**2) * dt) * rng.standard_normal()
        zch += (-zch/params["tau_chi"]) * dt + np.sqrt((2.0*GamC*Tgh)/(params["tau_chi"]**2) * dt) * rng.standard_normal()

        # Velocidades con disipación + gradiente + ruido
        dphi += (-3.0*Hn*dphi - dV_dphi(phi, chi, params) + zph) * dt
        dchi += (-3.0*Hn*dchi - dV_dchi(phi, chi, params) + zch) * dt

        # Actualizar campos
        phi  += dphi * dt
        chi  += dchi * dt

        # Guardar después de burn-in
        if n >= burn_in:
            idx = n - burn_in
            PHI[idx]  = phi
            DPHI[idx] = dphi
            CHI[idx]  = chi
            DCHI[idx] = dchi

    return PHI, DPHI, CHI, DCHI


def default_params():
    """Parámetros por defecto, ajustables si usas --param-* en el CLI."""
    return dict(
        # potencial
        m_phi=1.0, m_chi=1.2,
        lambda_phi=0.5, lambda_chi=0.4,
        g=0.7, V0=0.05,
        # ruido/disipación
        alpha_phi=0.08, alpha_chi=0.08,   # Γ_i = α_i * 3H
        tau_phi=2.0,  tau_chi=2.0,        # memorias (ajusta para tu caso)
        # condiciones iniciales
        phi0=0.9, chi0=0.4, dphi0=0.0, dchi0=0.0,
    )


# ---------- Carga desde CSV ----------
def load_from_csv(path):
    """
    Lee CSV con columnas: t,phi,dphi,chi,dchi (con encabezado).
    Si hay más columnas, se ignoran. Si no hay encabezado, intenta por posición.
    """
    if pd is None:
        raise RuntimeError("Se requiere pandas para --from-csv. Instala: pip install pandas")
    df = pd.read_csv(path)
    cols = [c.lower() for c in df.columns]
    # Mapear posibles nombres
    def pick(name, alts):
        for cand in [name] + alts:
            if cand in cols:
                return df[df.columns[cols.index(cand)]].to_numpy()
        return None

    phi  = pick("phi",  ["ϕ"])
    dphi = pick("dphi", ["phi_dot","phidot","dphidt","ϕdot"])
    chi  = pick("chi",  [])
    dchi = pick("dchi", ["chi_dot","chidot","dchidt"])
    if phi is None or dphi is None or chi is None or dchi is None:
        # Intento por posición: t,phi,dphi,chi,dchi
        if df.shape[1] >= 5:
            phi  = df.iloc[:,1].to_numpy()
            dphi = df.iloc[:,2].to_numpy()
            chi  = df.iloc[:,3].to_numpy()
            dchi = df.iloc[:,4].to_numpy()
        else:
            raise ValueError("CSV debe contener columnas (phi,dphi,chi,dchi).")
    return phi, dphi, chi, dchi


# ---------- Figura ----------
def plot_phase(phi, dphi, chi, dchi, out_path):
    plt.figure(figsize=(7, 6))
    # Trayectorias (segmento final para claridad visual)
    N = len(phi)
    tail = min(N, 10000)  # últimos puntos
    plt.plot(phi[-tail:], dphi[-tail:], linewidth=1.2, label="Órbitas tardías: (ϕ, ẋϕ)")
    plt.plot(chi[-tail:], dchi[-tail:], linewidth=1.2, linestyle="--", label="Órbitas tardías: (χ, ẋχ)")
    plt.xlabel("Campo")
    plt.ylabel("Velocidad")
    plt.title("Fig. 1 – Diagramas de fase (ciclos límite estocásticos)")
    plt.grid(True, alpha=0.3)
    plt.legend(loc="best")
    plt.tight_layout()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.savefig(out_path, dpi=220)
    plt.close()
    print(f"[OK] Figura guardada en: {out_path}")


# ---------- CLI ----------
def main():
    ap = argparse.ArgumentParser(description="Genera Fig. 1 (diagramas de fase) desde simulación o CSV.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--simulate", action="store_true", help="Simula Euler–Maruyama y genera la figura.")
    mode.add_argument("--from-csv", action="store_true", help="Carga datos desde CSV y genera la figura.")
    ap.add_argument("--phi-chi-csv", type=str, default=None, help="Ruta al CSV con columnas t,phi,dphi,chi,dchi.")
    ap.add_argument("--steps", type=int, default=200000, help="Número de pasos (simulación).")
    ap.add_argument("--dt", type=float, default=0.002, help="Paso de tiempo (simulación).")
    ap.add_argument("--burn-in", type=int, default=20000, help="Pasos a descartar antes de guardar.")
    ap.add_argument("--seed", type=int, default=42, help="Semilla RNG (simulación).")
    ap.add_argument("--out", type=str, default="assets/fig1-fase.png", help="Ruta de salida de la figura.")

    # Parámetros del modelo (opcionales para afinar sin tocar el código)
    ap.add_argument("--m_phi", type=float, default=None)
    ap.add_argument("--m_chi", type=float, default=None)
    ap.add_argument("--lambda_phi", type=float, default=None)
    ap.add_argument("--lambda_chi", type=float, default=None)
    ap.add_argument("--g", type=float, default=None)
    ap.add_argument("--V0", type=float, default=None)
    ap.add_argument("--alpha_phi", type=float, default=None)
    ap.add_argument("--alpha_chi", type=float, default=None)
    ap.add_argument("--tau_phi", type=float, default=None)
    ap.add_argument("--tau_chi", type=float, default=None)
    ap.add_argument("--phi0", type=float, default=None)
    ap.add_argument("--chi0", type=float, default=None)
    ap.add_argument("--dphi0", type=float, default=None)
    ap.add_argument("--dchi0", type=float, default=None)

    args = ap.parse_args()

    # Parám. base + overrides por CLI
    params = default_params()
    for k in ["m_phi","m_chi","lambda_phi","lambda_chi","g","V0",
              "alpha_phi","alpha_chi","tau_phi","tau_chi",
              "phi0","chi0","dphi0","dchi0"]:
        v = getattr(args, k)
        if v is not None:
            params[k] = v

    if args.from_csv:
        if not args.phi_chi_csv:
            raise ValueError("Debes indicar --phi-chi-csv con la ruta al CSV.")
        phi, dphi, chi, dchi = load_from_csv(args.phi_chi_csv)
        plot_phase(phi, dphi, chi, dchi, args.out)
        return

    if args.simulate:
        phi, dphi, chi, dchi = simulate_trajectories(
            steps=args.steps, dt=args.dt, seed=args.seed,
            burn_in=args.burn_in, params=params
        )
        plot_phase(phi, dphi, chi, dchi, args.out)
        return


if __name__ == "__main__":
    main()

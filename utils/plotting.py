# 📦 utils/plotting.py

import matplotlib.pyplot as plt
import numpy as np

def plot_phase_space(phi, dphi, chi, dchi):
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(phi, dphi, color='darkblue')
    plt.xlabel('ϕ')
    plt.ylabel('ϕ̇')
    plt.title('Diagrama de fase (ϕ, ϕ̇)')

    plt.subplot(1, 2, 2)
    plt.plot(chi, dchi, color='darkgreen')
    plt.xlabel('χ')
    plt.ylabel('χ̇')
    plt.title('Diagrama de fase (χ, χ̇)')
    plt.tight_layout()
    plt.show()

def plot_power_spectrum(freqs_phi, spec_phi, freqs_chi, spec_chi):
    plt.figure(figsize=(10, 4))
    plt.plot(freqs_phi, spec_phi, label='ϕ(t)', color='navy')
    plt.plot(freqs_chi, spec_chi, label='χ(t)', color='forestgreen')
    plt.xlabel('Frecuencia')
    plt.ylabel('Potencia')
    plt.title('Espectros de potencia')
    plt.legend()
    plt.grid()
    plt.show()

def plot_observables(t, Omega_phi, Omega_chi, w_total):
    plt.figure(figsize=(10, 4))
    plt.plot(t, Omega_phi, label='Ωϕ', color='navy')
    plt.plot(t, Omega_chi, label='Ωχ', color='darkgreen')
    plt.xlabel('Tiempo')
    plt.ylabel('Densidad fraccional')
    plt.title('Evolución de Ωϕ y Ωχ')
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(t, w_total, label='w_total', color='purple')
    plt.xlabel('Tiempo')
    plt.ylabel('w_total')
    plt.title('Evolución de w_total')
    plt.grid()
    plt.show()

def plot_histogram_w(w_tail):
    plt.figure(figsize=(8, 4))
    plt.hist(w_tail, bins=50, color='orchid', edgecolor='black', alpha=0.7)
    plt.xlabel('w_total')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de w_total en régimen tardío')
    plt.grid()
    plt.show()

def plot_tau_sensitivity(tau_values, Q_values, mean_w_values):
    plt.figure(figsize=(10, 4))
    plt.plot(tau_values, Q_values, marker='o', label='Factor de calidad Q', color='darkblue')
    plt.xlabel('τ (memoria)')
    plt.ylabel('Q')
    plt.title('Sensibilidad de la coherencia oscilatoria al parámetro τ')
    plt.grid()
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(tau_values, mean_w_values, marker='s', label='⟨w_total⟩', color='purple')
    plt.xlabel('τ (memoria)')
    plt.ylabel('⟨w_total⟩')
    plt.title('Convergencia de w_total en régimen tardío')
    plt.grid()
    plt.legend()
    plt.show()

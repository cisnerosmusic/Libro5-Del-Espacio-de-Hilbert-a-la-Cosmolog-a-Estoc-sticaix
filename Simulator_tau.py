import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from src.cosmology.common import DL
from src.cosmology.model_pt import Ez_PT
from src.cosmology.model_fluid import Ez_FLUID
from src.cosmology.common import Ez_LCDM

st.set_page_config(page_title="Simulador τ — Huella Oscilante")

st.title("Simulador de Memoria Cosmológica (τ > 0)")
st.write("Ajusta parámetros y observa el efecto en E(z), D_L(z) y w(z) efectivo.")

model = st.selectbox("Modelo", ["LCDM", "PT-simétrico", "Fluido con memoria"])

col1, col2, col3 = st.columns(3)
with col1:
    Om = st.slider("Ω_m", 0.15, 0.45, 0.315, 0.005)
with col2:
    H0 = st.slider("H0 [km/s/Mpc]", 60, 78, 70, 1)
with col3:
    A = st.slider("A (amplitud)", 0.0, 0.3, 0.10, 0.01)

omega = st.slider("ω (frecuencia log)", 0.0, 10.0, 3.0, 0.1)
z_tau = st.slider("z_τ (escala)", 0.1, 5.0, 1.0, 0.1)
delta = st.slider("δ (fase)", 0.0, 6.283, 0.0, 0.1)
b_over_a = st.slider("b/a (PT balance)", 0.0, 1.0, 0.1, 0.01)
tau_mem = st.slider("τ_mem (fluido)", 0.1, 3.0, 1.5, 0.1)

z = np.linspace(0, 2.0, 400)

if model == "LCDM":
    Ez = Ez_LCDM(z, Om=Om)
elif model == "PT-simétrico":
    Ez = Ez_PT(z, Om=Om, H0=H0, A=A, omega=omega, z_tau=z_tau, delta=delta, b_over_a=b_over_a)
else:
    Ez = Ez_FLUID(z, Om=Om, H0=H0, A=A, omega=omega, z_tau=z_tau, delta=delta, tau_mem=tau_mem)

# Plot E(z)
fig1, ax1 = plt.subplots()
ax1.plot(z, Ez, label="E(z)")
ax1.set_xlabel("z"); ax1.set_ylabel("E(z)")
ax1.legend(); st.pyplot(fig1)

# Plot D_L(z)
from src.cosmology.common import mu_theory
mu = mu_theory(z, H0=H0, Ez_fn=(Ez_LCDM if model=="LCDM" else (Ez_PT if model=="PT-simétrico" else Ez_FLUID)),
               Om=Om, H0=H0, A=A, omega=omega, z_tau=z_tau, delta=delta, b_over_a=b_over_a, tau_mem=tau_mem)
fig2, ax2 = plt.subplots()
ax2.plot(z, mu, label="μ(z)")
ax2.set_xlabel("z"); ax2.set_ylabel("μ (mag)")
ax2.legend(); st.pyplot(fig2)

st.caption("Tip: en PT sube b/a para ver cómo el balance suprime inestabilidades; en Fluido incrementa τ_mem para ver memoria más larga.")

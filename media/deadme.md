# 📁 Visualizaciones del Libro 5 — Del Espacio de Hilbert a la Cosmología Estocástica

Este directorio contiene todas las figuras generadas por simulación, análisis estadístico, visualización artística y modelado formal. Las imágenes están organizadas por capítulos y notebooks, y acompañan tanto la narrativa científica como la poética del proyecto.

---

## 🔬 Figuras generadas por simulación y visualización artística

### 📘 Notebook 04 — Esquema numérico y dinámica de campos

- `fig_04_phase_diagram_phi_chi.png`: Diagrama de fase de los campos ϕ(t) y χ(t), mostrando su trayectoria acoplada en el espacio de fase.
- `fig_04_power_spectrum_phi_chi.png`: Espectro de potencia de ϕ(t), con pico dominante en baja frecuencia, indicando oscilación amortiguada.

### 📘 Notebook 05 — Observables cosmológicos

- `fig_05_omega_evolution.png`: Evolución simulada de las densidades fraccionales Ωϕ(t) y Ωχ(t), mostrando su modulación temporal.
- `fig_05_w_total_evolution.png`: Evolución suavizada del parámetro de ecuación de estado total ⟨w_total⟩, con oscilaciones suaves alrededor de -1.
- `fig_05_w_total_histogram.png`: Histograma tardío de w_total, mostrando su distribución en régimen estacionario.

### 📘 Notebook 06 — Sensibilidad al parámetro de memoria τ

- `fig_06_Q_vs_tau.png`: Factor de calidad Q de las oscilaciones de ϕ(t) en función de τ, indicando estabilidad espectral.
- `fig_06_w_vs_tau.png`: Promedio tardío de ⟨w_total⟩ en función de τ, revelando un pico de resiliencia en τ ≈ 3.

### 🎨 Notebook 08 — Extensión artística

- `fig_08_cosmic_trajectories.png`: Visualización poética de las trayectorias cósmicas, con curvas entrelazadas en magenta, turquesa y dorado.
- `poem_08_cosmic_duet.txt`: Poema final que acompaña la visualización artística, evocando la danza de los campos en el vacío.

---

## 📐 Figuras generadas por modelos formales

### 📘 Capítulo 1 — Modelos I, II, III

- `fig_01_w_z_models.png`: Evolución de w(z) para los tres modelos: Krein, PT-simétrico y Fluido con memoria.

### 📘 Capítulo 2 — Dinámica en espacio de fase

- `fig_02_phase_map_w_dwdt.png`: Mapa de fase (w, dw/dt) para los tres modelos, mostrando sus trayectorias dinámicas.

### 📘 Capítulo 3 — Superficie de atracción

- `fig_03_attraction_surface.png`: Superficie A(τ, ω) que representa la estabilidad del sistema en función de memoria y frecuencia.

### 📘 Capítulo 4 — Análisis estadístico marginal

- `fig_04a_marginal_A.png`: Histograma marginal de A, con distribución aproximadamente normal.
- `fig_04b_marginal_omega.png`: Histograma marginal de ω, con pico en ω ≈ 2.
- `fig_04c_marginal_tau.png`: Histograma marginal de τ, centrado en τ ≈ 1.
- `fig_04d_scatter_A_omega.png`: Dispersión entre A y ω, sin correlación aparente.
- `fig_04e_scatter_A_tau.png`: Dispersión entre A y τ, distribución uniforme.
- `fig_04f_scatter_omega_tau.png`: Dispersión entre ω y τ, con concentración en ω ≈ 2 y τ ≈ 1.5.

### 📘 Capítulo 5 — Equivalencias entre modelos

- `fig_05_model_equivalence.png`: Diagrama que ubica los tres modelos en el plano (τ, ω), mostrando sus equivalencias dinámicas.

---

## 🧭 Uso sugerido

Estas figuras pueden ser referenciadas en los notebooks, el artículo principal o el README raíz. Para incluirlas en Markdown:

```markdown
![Diagrama de fase](media/fig_04_phase_diagram_phi_chi.png)

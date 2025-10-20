# 🧠 README: Modelo Cosmológico Estocástico con Memoria

Este documento describe la estructura modular del modelo cosmológico propuesto en el proyecto *Del Espacio de Hilbert a la Cosmología Estocástica*. Aquí se explica cómo ejecutar el flujo completo, qué notebooks están disponibles, y cómo se organizan los módulos auxiliares.

---

## 📦 Estructura del repositorio

cosmologia-estocastica/ ├── main_model.ipynb # Coordinador maestro del flujo completo ├── README_for_models.md # Este archivo ├── notebooks/ # Notebooks por capítulo │ ├── 01_krein_space.ipynb │ ├── 02_model_definition.ipynb │ ├── 03_fokker_planck.ipynb │ ├── 04_numerical_scheme.ipynb │ ├── 05_observables.ipynb │ ├── 06_sensitivity_tau.ipynb │ ├── 07_validation_plan.ipynb ├── utils/ # Módulos auxiliares │ ├── plotting.py # Funciones de visualización │ ├── parameters.py # Carga y edición de parámetros ├── data/ │ └── params_default.json # Parámetros base del modelo


---

## 🚀 Ejecución paso a paso

1. Abre `main_model.ipynb` en Jupyter o VS Code.
2. Ejecuta cada celda en orden para:
   - Definir el modelo físico
   - Simular la evolución estocástica
   - Calcular observables cosmológicos
   - Evaluar sensibilidad al parámetro de memoria \( \tau \)
   - Preparar el plan de validación empírica

---

## 📊 Visualizaciones disponibles

- Diagramas de fase \( (\phi, \dot\phi), (\chi, \dot\chi) \)
- Espectros de potencia y factor de calidad \( Q \)
- Evolución de \( \Omega_\phi, \Omega_\chi, w_{\text{total}} \)
- Histogramas en régimen tardío
- Barridos en \( \tau \) para evaluar resiliencia

Todas las gráficas están centralizadas en `utils/plotting.py`.

---

## 🧮 Parámetros físicos y numéricos

Los parámetros base están definidos en `data/params_default.json`. Puedes modificarlos manualmente o usar:

```python
from utils import parameters
params = parameters.load_params()
params = parameters.update_param(params, 'tau_phi', 3.0)
parameters.save_params(params)

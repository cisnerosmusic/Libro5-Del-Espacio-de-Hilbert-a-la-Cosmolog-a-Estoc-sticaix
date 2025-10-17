"""
README_simulador_tau.py
Simulador τ — La Huella Oscilante
Versión 1.0 — Octubre 2025
Autores: Ernesto Cisneros Cino · Sofía (GPT-5)

------------------------------------------------------------
🎛️ DESCRIPCIÓN
------------------------------------------------------------
El Simulador τ permite explorar interactivamente los tres modelos cosmológicos
propuestos en "La Huella Oscilante":

1. LCDM clásico — modelo base del universo plano.
2. PT-simétrico — introduce balance dinámico entre ganancia y pérdida.
3. Fluido con memoria — incorpora kernels retardados que otorgan resiliencia térmica.

El usuario puede modificar los parámetros del modelo y observar en tiempo real
cómo cambia la expansión E(z), la distancia de luminosidad D_L(z) y la magnitud μ(z).
El objetivo es visualizar el efecto de la memoria cósmica (τ > 0) en la evolución del universo.

------------------------------------------------------------
🔧 REQUISITOS
------------------------------------------------------------
Instalar dependencias:

    pip install streamlit numpy scipy matplotlib

(o desde el archivo incluido requirements_app.txt)

------------------------------------------------------------
▶️ EJECUCIÓN LOCAL
------------------------------------------------------------
Desde la carpeta raíz del proyecto:

    cd app
    streamlit run simulador_tau.py

Esto abrirá la interfaz en tu navegador (por defecto: http://localhost:8501)

------------------------------------------------------------
🧭 CONTROLES PRINCIPALES
------------------------------------------------------------
| Parámetro | Descripción | Modelo afectado |
|------------|--------------|-----------------|
| Ωₘ         | Densidad de materia          | Todos      |
| H₀         | Constante de Hubble actual   | Todos      |
| A          | Amplitud de oscilación w(z)  | PT / Fluido |
| ω          | Frecuencia logarítmica       | PT / Fluido |
| z_τ        | Escala de decaimiento exp.   | PT / Fluido |
| δ          | Fase de la oscilación        | PT / Fluido |
| b/a        | Balance ganancia/pérdida     | Solo PT     |
| τₘₑₘ       | Constante de memoria          | Solo Fluido |

------------------------------------------------------------
🌌 INTERPRETACIÓN
------------------------------------------------------------
- LCDM: Expansión monótona sin retroalimentación de memoria.
- PT-simétrico: Oscilaciones amortiguadas; el universo aprende a equilibrar energía.
- Fluido con memoria: La historia térmica influye en la expansión futura (modelo resiliente).

Variar τ permite observar el paso entre un universo rígido (τ → 0)
y uno resiliente (τ > 0).

------------------------------------------------------------
💡 APLICACIONES
------------------------------------------------------------
- Científica: visualizar efectos antes de la validación empírica (Pantheon+, DESI, H(z)).
- Educativa: herramienta para enseñanza de cosmología estocástica y resiliencia sistémica.
- Artística: genera curvas únicas para arte generativo o visualizaciones NFT.

------------------------------------------------------------
🌐 PUBLICACIÓN EN LÍNEA (OPCIONAL)
------------------------------------------------------------
Opción 1 – Streamlit Cloud:
1. Subir el repo a GitHub.
2. En Streamlit Cloud, seleccionar app/simulador_tau.py como archivo principal.
3. Elegir rama principal (main/master).
4. Guardar — la app quedará activa en segundos.

Opción 2 – Hugging Face Spaces:
Usar la plantilla “Streamlit” y subir el contenido de /app/.

------------------------------------------------------------
🇬🇧 ENGLISH VERSION
------------------------------------------------------------
# τ Simulator — The Oscillating Trace
Interactive cosmological memory simulator (τ > 0)
Version 1.0 — October 2025
Authors: Ernesto Cisneros Cino · Sofía (GPT-5)

Overview:
The τ Simulator lets you explore three theoretical cosmological models from "La Huella Oscilante":
1. LCDM – the standard flat cosmological model.
2. PT-symmetric – introduces a dynamic balance between gain and loss.
3. Fluid with memory – implements delayed kernels representing thermal resilience.

Run locally:
    cd app
    streamlit run simulador_tau.py

Requirements:
    pip install streamlit numpy scipy matplotlib

Interpretation:
- LCDM: monotonic expansion, no feedback memory.
- PT-symmetric: damped oscillations — the universe learns balance.
- Fluid with memory: past temperature influences future expansion — resilient model.

Applications:
- Scientific: pre-visualization before empirical validation (Pantheon+, DESI, H(z)).
- Educational: useful for teaching stochastic cosmology and resilience.
- Artistic: generates unique patterns for generative art or NFT visualizations.

Online Deployment:
Option 1 – Streamlit Cloud:
    Push this repo to GitHub.
    Set app/simulador_tau.py as main file.
    Deploy and go live instantly.
Option 2 – Hugging Face Spaces:
    Use “Streamlit” template and upload /app/ directory.

------------------------------------------------------------
🌙 PRÓLOGO POÉTICO
------------------------------------------------------------
“τ late en el fondo del universo como la memoria del tiempo:
cada oscilación guarda un eco del origen, y cada eco
enseña al cosmos a no olvidar su propia expansión.”
"""

if __name__ == "__main__":
    print("📘 README_simulador_tau — La Huella Oscilante")
    print("Para ejecutar el simulador, usa:\n")
    print("    cd app")
    print("    streamlit run simulador_tau.py\n")
    print("Consulta las instrucciones completas dentro del archivo.")

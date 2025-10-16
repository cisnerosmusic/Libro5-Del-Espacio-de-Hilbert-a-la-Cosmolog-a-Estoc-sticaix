---
title: "Del Espacio de Hilbert a la Cosmología Estocástica"
subtitle: "Un Modelo de Dos Campos con Ruido Cuántico Ligado a la Geometría del Universo"
author: "Ernesto Cisneros Cino"
place: "Miami"
year: "2025"
license: "CC0 1.0 (Public Domain Dedication)"
---

# Resumen

Presentamos un modelo cosmológico estocástico que vincula:  
(i) una extensión pseudo-Hermítica del espacio de Hilbert (espacio de Krein),  
(ii) una dinámica de dos campos escalares acoplados $(\phi,\chi)$ —con $\phi$ taquiónico y $\chi$ estable—, y  
(iii) ruido coloreado de Ornstein–Uhlenbeck cuya intensidad está fijada por la temperatura de Gibbons–Hawking

$$
T_{GH}=\frac{H}{2\pi}.
$$

Mostramos atractores oscilatorios (ciclos límite estocásticos) y transiciones efectivas entre regímenes *matter-like* ($w\approx 0$) y *vacuum-like* ($w\approx -1$). La memoria del ruido (tiempo de correlación $\tau$) resulta necesaria para la resiliencia cosmológica.

---

# 1. Introducción y Motivación

La pregunta central es si podemos modelar la energía oscura y la materia oscura **sin** introducir entidades exóticas adicionales, sino emergiendo de la **geometría** y del **ruido cuántico** asociado al horizonte. Proponemos tres ideas simples:

1. **Espacio de estados ampliado**: admitir un grado de libertad “taquiónico” en un espacio con métrica indefinida (tipo Krein) y recuperar la unitariedad en el subespacio físico.
2. **Dos campos acoplados**: un campo $\phi$ (taquiónico) y otro $\chi$ (estable), con acoplamiento $g$.
3. **Ruido con memoria ligado a la expansión**: usar un proceso de Ornstein–Uhlenbeck cuya intensidad sigue a la temperatura de Gibbons–Hawking, 
en línea: $T_{GH}=\tfrac{H}{2\pi}$.

La intuición es que la expansión ($H$) actúa como **fuente y disipador**: templa las oscilaciones y selecciona estados físicos estables. El parámetro clave es el **tiempo de correlación** del ruido ($\tau$): sin memoria ($\tau\to 0$), el sistema pierde coherencia; con memoria finita, aparece un **atractor oscilatorio** (ciclo límite estocástico).

**Ecuación de Friedmann (bloque de prueba):**

$$
H^2 \;=\; \tfrac12\!\left(\dot\phi^2+\dot\chi^2\right) \;+\; V(\phi,\chi).
$$

**Potencial efectivo (bloque de prueba):**

$$
V(\phi,\chi)\;=\; -\tfrac12 m_\phi^2\,\phi^2 \;+\; \tfrac{\lambda_\phi}{4}\phi^4 
\;+\; \tfrac12 m_\chi^2\,\chi^2 \;+\; \tfrac{\lambda_\chi}{4}\chi^4 
\;+\; \tfrac12 g^2\,\phi^2\chi^2 \;+\; V_0.
$$

**Resumen de objetivos de esta sección**
- Motivar por qué un **modo taquiónico** no rompe la teoría si se proyecta correctamente al subespacio físico.
- Justificar el uso de **ruido coloreado** (con memoria $\tau$) en lugar de ruido blanco.
- Adelantar predicciones cualitativas: transiciones *matter-like* ($w\!\approx\!0$) y *vacuum-like* ($w\!\approx\!-1$) y rol de $\tau$ en la **resiliencia**.

> Nota técnica mínima (en línea): métrica indefinida $\eta=\mathrm{diag}(-1,+1)$; temperatura del horizonte $T_{GH}=\tfrac{H}{2\pi}$; fricción cosmológica $3H$.



---

# 2. Fundamentos Teóricos

## 2.1 Espacio de Krein, pseudo-Hermitismo y proyección física

Usamos un espacio con métrica indefinida (tipo **Krein**) para alojar un grado de libertad taquiónico sin perder unitariedad en el subespacio físico. La métrica:

$$
\eta \;=\; \mathrm{diag}(-1,+1)
$$

actúa sobre el par de campos $(\phi,\chi)$, asignando signatura negativa al sector taquiónico y positiva al estable.

**Hamiltoniano homogéneo (modos de fondo):**

$$
H_{\text{tot}} \;=\;
\Big(\tfrac12 p_\phi^2 \;-\; \tfrac12 m_\phi^2\,\phi^2 \;+\; \tfrac{\lambda_\phi}{4}\,\phi^4\Big)
\;+\;
\Big(\tfrac12 p_\chi^2 \;+\; \tfrac12 m_\chi^2\,\chi^2 \;+\; \tfrac{\lambda_\chi}{4}\,\chi^4\Big)
\;+\;
\tfrac12 g^2\,\phi^2\chi^2 \;+\; V_0 \,.
$$

La inestabilidad de $\phi$ (masa imaginaria efectiva) no es un “fallo”: es una consecuencia de la signatura de $\eta$. El sector “en sombra” se controla a nivel geométrico.

**Pseudo-Hermitismo y espectro real.** Introducimos un operador de forma $C$ (involución, $C^2=\mathbb{1}$) tal que $[C,H_{\text{tot}}]=0$. Definimos la métrica positiva efectiva en el subespacio físico:

$$
\eta_C \;\equiv\; C\,\eta \;>\; 0 \quad \text{en } \mathcal{H}_{\text{phys}} \,,
$$

con lo cual se cumple

$$
H_{\text{tot}}^{\dagger} \;=\; \eta_C \, H_{\text{tot}} \, \eta_C^{-1} \,,
$$

garantizando **espectro real** y **evolución unitaria** en $\mathcal{H}_{\text{phys}}$.

**Proyector físico:**

$$
\Pi_{\text{phys}} \;=\; \tfrac12\big(\mathbb{1}+C\big) \,.
$$

> Intuición: el par $(\eta,C)$ reetiqueta normas para que el sector observable tenga norma positiva; el sector de norma negativa queda suprimido dinámicamente.

## 2.2 Selección dinámica del subespacio físico

En presencia de expansión y **ruido coloreado** (secciones 3–5), la combinación **disipación cosmológica** $3H$ + **ruido con memoria** (Ornstein–Uhlenbeck) actúa como **filtro dinámico**:
- amortigua los modos con norma negativa,
- estabiliza una órbita atractora en el subespacio físico,
- y preserva la unitariedad efectiva a nivel de observables.

**Ecuación de Friedmann (recordatorio):**

$$
H^2 \;=\; \rho_{\text{tot}}
\;=\;
\tfrac12\!\left(\dot\phi^2+\dot\chi^2\right)
\;+\; V(\phi,\chi) \,.
$$

**Temperatura del horizonte (para el ruido ligado a la geometría):**

$$
T_{GH} \;=\; \tfrac{H}{2\pi} \,.
$$

> Puente a la Sección 3: definiremos el **ruido OU** con intensidad regulada por $T_{GH}$ y mostraremos cómo el **tiempo de correlación** $\tau$ controla la coherencia del atractor y las transiciones *matter-like* / *vacuum-like*.




# 3. Modelo Cosmológico y Ruido Autoconsistente

## 3.1 Campos, potencial y expansión

Consideramos dos campos escalares acoplados en un universo FRW plano. El potencial:

$$
V(\phi,\chi) \;=\; 
-\tfrac12 m_\phi^2\,\phi^2 \;+\; \tfrac{\lambda_\phi}{4}\phi^4
\;+\; \tfrac12 m_\chi^2\,\chi^2 \;+\; \tfrac{\lambda_\chi}{4}\chi^4
\;+\; \tfrac12 g^2\,\phi^2\chi^2 \;+\; V_0 \,.
$$

Ecuación de Friedmann (unidades \(8\pi G=1\)):

$$
H^2 \;=\; \rho_{\text{tot}} 
\;=\; \tfrac12\!\left(\dot\phi^2+\dot\chi^2\right) \;+\; V(\phi,\chi) \,.
$$

## 3.2 Ruido de Ornstein–Uhlenbeck ligado a la geometría

El ruido está **autoconsistentemente** regulado por la temperatura del horizonte:

$$
T_{GH} \;=\; \tfrac{H}{2\pi}\,,
$$

y cada campo recibe una fuerza estocástica con **memoria** (tiempos de correlación $\tau_\phi,\tau_\chi$):

**Procesos OU (esquema continuo):**

$$
\[
\dot\zeta_\phi \;=\; -\frac{\zeta_\phi}{\tau_\phi}
\;+\; \sqrt{\frac{2\,\Gamma_\phi\,T_{GH}}{\tau_\phi^2}}\,\xi_\phi(t)\,,
\qquad
\dot\zeta_\chi \;=\; -\frac{\zeta_\chi}{\tau_\chi}
\;+\; \sqrt{\frac{2\,\Gamma_\chi\,T_{GH}}{\tau_\chi^2}}\,\xi_\chi(t)\,,
\]
$$

donde $\xi_i(t)$ son ruidos blancos unitarios y $\Gamma_i=\alpha_i\,3H$.

**Ecuaciones de movimiento con disipación + ruido:**

$$
\[
\ddot\phi \;=\; -3H\,\dot\phi \;-\; \partial_\phi V \;+\; \zeta_\phi\,,
\qquad
\ddot\chi \;=\; -3H\,\dot\chi \;-\; \partial_\chi V \;+\; \zeta_\chi\,.
\]
$$


# 4. Método Numérico

## 4.1 Integración Euler–Maruyama (SDEs)

Usamos un paso fijo $\Delta t$ y actualizamos en el orden: ruido $\to$ velocidades $\to$ campos $\to$ geometría.

**Discretización de los procesos OU** (para $i\in\{\phi,\chi\}$):

$$
\zeta_i^{\,n+1}
\;=\;
\zeta_i^{\,n}
\;-\;
\frac{\Delta t}{\tau_i}\,\zeta_i^{\,n}
\;+\;
\sqrt{\frac{2\,\Gamma_i^{\,n}\,T_{GH}^{\,n}}{\tau_i^{\,2}}\,\Delta t}\;\;\mathcal{N}_i^{\,n}\,,
$$

donde $\mathcal{N}_i^{\,n}\sim \mathcal{N}(0,1)$ independientes, $\Gamma_i^{\,n}=\alpha_i\,3H^{\,n}$ y $T_{GH}^{\,n}=\dfrac{H^{\,n}}{2\pi}$.

**Ecuaciones de movimiento (velocidades y campos):**

$$
\dot\phi^{\,n+1}
\;=\;
\dot\phi^{\,n}
\;+\;
\Big(-3H^{\,n}\dot\phi^{\,n}-\partial_\phi V(\phi^{\,n},\chi^{\,n})+\zeta_\phi^{\,n}\Big)\,\Delta t\,,
$$

$$
\dot\chi^{\,n+1}
\;=\;
\dot\chi^{\,n}
\;+\;
\Big(-3H^{\,n}\dot\chi^{\,n}-\partial_\chi V(\phi^{\,n},\chi^{\,n})+\zeta_\chi^{\,n}\Big)\,\Delta t\,,
$$

$$
\phi^{\,n+1}
\;=\;
\phi^{\,n}
\;+\;
\dot\phi^{\,n+1}\,\Delta t\,,
\qquad
\chi^{\,n+1}
\;=\;
\chi^{\,n}
\;+\;
\dot\chi^{\,n+1}\,\Delta t\,.
$$

**Cierre geométrico (Friedmann) y temperatura del horizonte:**

$$
H^{\,n+1}
\;=\;
\sqrt{
\tfrac12\Big[(\dot\phi^{\,n+1})^2+(\dot\chi^{\,n+1})^2\Big]
\;+\;
V(\phi^{\,n+1},\chi^{\,n+1})
}\,,
\qquad
T_{GH}^{\,n+1}
\;=\;
\frac{H^{\,n+1}}{2\pi}\,.
$$

> Nota: el orden “actualiza $\zeta$ $\rightarrow$ actualiza $(\dot\phi,\dot\chi)$ $\rightarrow$ actualiza $(\phi,\chi)$ $\rightarrow$ recalcula $(H,T_{GH})$” mantiene la autoconsistencia a cada paso.

---

## 4.2 Estabilidad y elección de $\Delta t$

Para estabilidad numérica, elige

$$
\Delta t \;\ll\; \min\!\big(\tau_\phi,\;\tau_\chi,\;H^{-1},\;m_\phi^{-1},\;m_\chi^{-1}\big)\,,
$$

y verifica que las variaciones relativas por paso sean pequeñas:

$$
\frac{|\Delta H|}{H}\ll 1,
\quad
\frac{|\Delta \phi|}{\max(1,|\phi|)}\ll 1,
\quad
\frac{|\Delta \chi|}{\max(1,|\chi|)}\ll 1\,.
$$

> Recomendación práctica inicial: usar $\Delta t$ entre $10^{-3}$ y $10^{-2}$ (en unidades adimensionales del modelo) y reducir si observas inestabilidades o explosiones numéricas.

---

## 4.3 Observables efectivos

**Densidades parciales y presión:**

$$
\rho_\phi \;=\; \tfrac12\,\dot\phi^{\,2} \;+\; V_\phi,
\qquad
\rho_\chi \;=\; \tfrac12\,\dot\chi^{\,2} \;+\; V_\chi,
\qquad
p \;=\; \tfrac12\big(\dot\phi^{\,2}+\dot\chi^{\,2}\big) \;-\; \big(V_\phi+V_\chi\big)\,,
$$

donde $V_\phi$ y $V_\chi$ son las contribuciones de $V(\phi,\chi)$ asociadas a cada campo.

**Fracciones y ecuación de estado total:**

$$
\rho \;=\; \rho_\phi+\rho_\chi,\qquad
\Omega_\phi \;=\; \frac{\rho_\phi}{\rho},\quad
\Omega_\chi \;=\; \frac{\rho_\chi}{\rho},\qquad
w_{\text{total}} \;=\; \frac{p}{\rho}\,.
$$

Para reducir ruido instantáneo, usa promedios móviles:

$$
\overline{w}_{\,\text{total}}(t_k)
\;=\;
\frac{1}{M}\sum_{j=0}^{M-1} w_{\text{total}}(t_{k-j})\,,
$$

con una ventana $M$ tal que $M\,\Delta t$ sea varias veces el período oscilatorio del atractor.

---

## 4.4 Ensamble y semillas

Para estimar promedios de conjunto y dispersión, ejecuta $N_{\text{real}}$ simulaciones independientes con distintas semillas:

$$
\langle \mathcal{O} \rangle \;\approx\; \frac{1}{N_{\text{real}}}\sum_{r=1}^{N_{\text{real}}}\mathcal{O}^{(r)}\,,
\qquad
\mathrm{Var}(\mathcal{O}) \;\approx\; \frac{1}{N_{\text{real}}-1}\sum_{r=1}^{N_{\text{real}}}\Big(\mathcal{O}^{(r)}-\langle \mathcal{O} \rangle\Big)^2\,.
$$

> Sugerencia: usa $N_{\text{real}}\in[16,64]$ para estadística razonable; guarda $\{\phi,\dot\phi,\chi,\dot\chi,H,w_{\text{total}},\Omega_\phi,\Omega_\chi\}$ a intervalos regulares para construir espectros y promedios.

---

## 4.5 Criterios de parada

Detén la integración cuando se cumpla alguno de:
- tiempo máximo $t_{\max}$ alcanzado;
- cambio relativo pequeño por varias ventanas:

  
$$
\frac{|\overline{w}_{\,\text{total}}(t)-\overline{w}_{\,\text{total}}(t-\Delta T)|}{\max\!\big(1,\;|\overline{w}_{\,\text{total}}(t-\Delta T)|\big)} \;\le\; \epsilon\,,
$$

- estacionariedad aproximada en $H$ y en la amplitud del ciclo (análisis de picos en el espectro).

Parámetros guía: $\epsilon\sim 10^{-3}$, $\Delta T$ de varias veces el período fundamental del atractor.


# 5. Resultados Principales
*(…)*

# 6. Discusión y Comparación
*(…)*

# 7. Conclusiones
*(…)*

---

## Apéndices
*(…)*

## Referencias
- Starobinsky (1986) *(…)*  
- Berera (1995) *(…)*  
- Calzetta & Hu (2008) *(…)*  
- Bender & Mannheim (2011) *(…)*  
- Planck Collaboration (2020) *(…)*  
- Kiefer (2012) *(…)*  

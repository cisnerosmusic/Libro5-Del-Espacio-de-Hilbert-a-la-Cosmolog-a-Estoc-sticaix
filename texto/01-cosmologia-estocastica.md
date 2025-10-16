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

> **Autor:** Ernesto Cisneros Cino · **Lugar/Año:** Miami, 2025 · **Licencia:** CC0 1.0 (Dominio público)


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

## 5.1 Dinámica de fase y ciclos límite estocásticos

Los diagramas de fase $(\phi,\dot\phi)$ y $(\chi,\dot\chi)$ muestran convergencia a **órbitas cerradas** con ancho finito (anchura debida al ruido OU). Esto evidencia un **ciclo límite estocástico** sostenido por la combinación de disipación $3H$ y ruido ligado a $T_{GH}$.

El espectro de potencia de $\phi(t)$ y $\chi(t)$ presenta un pico dominante en $f_0$ con **factor de calidad**:

$$
Q \;=\; \frac{f_0}{\Delta f} \,,
$$

donde $\Delta f$ es el ancho a media altura del pico. Observamos que $Q$ crece en el régimen tardío, señal de **coherencia oscilatoria** inducida por el acoplamiento “geometría $\leftrightarrow$ fluctuación”.

> Conclusión (E): la dinámica no colapsa a un punto fijo; se estabiliza en una **oscilación resiliente** mantenida por la expansión y el ruido coloreado.

---

## 5.2 Observables efectivos: fracciones de energía y ecuación de estado total

Definimos densidades parciales y presión:

$$
\rho_\phi \;=\; \tfrac12\,\dot\phi^{\,2} \;+\; V_\phi \,, 
\qquad
\rho_\chi \;=\; \tfrac12\,\dot\chi^{\,2} \;+\; V_\chi \,,
\qquad
p \;=\; \tfrac12\big(\dot\phi^{\,2}+\dot\chi^{\,2}\big) \;-\; \big(V_\phi+V_\chi\big) \,.
$$

Con $\rho \equiv \rho_\phi+\rho_\chi$, las fracciones y la ecuación de estado total son:

$$
\Omega_\phi \;=\; \frac{\rho_\phi}{\rho} \,, 
\qquad
\Omega_\chi \;=\; \frac{\rho_\chi}{\rho} \,, 
\qquad
w_{\text{total}} \;=\; \frac{p}{\rho} \,.
$$

En el régimen asintótico, el **histograma** de $w_{\text{total}}$ se concentra alrededor de

$$
\langle w \rangle \;\approx\; -1
$$

con dispersión finita, y se observan **fases transitorias** *matter-like* ($w\!\approx\!0$) durante la aproximación al atractor.

> Conclusión (F): el sistema reproduce un tardío **vacuum-like** con $\langle w\rangle \to -1$ y admite **transiciones naturales** *matter-like* $\leftrightarrow$ *vacuum-like* controladas por el acoplamiento y el ruido geométrico.

---

## 5.3 Memoria como condición de resiliencia

Barrimos el tiempo de correlación del ruido en un conjunto típico 
$\tau \in \{0,\;0.5,\;1,\;2,\;3,\;5\}$ (unidades adimensionales del modelo) y medimos la coherencia espectral y la estabilidad de $w_{\text{total}}$.

**Métricas de coherencia/estabilidad:**

$$
Q(\tau) \;=\; \frac{f_0(\tau)}{\Delta f(\tau)} \,,
\qquad
\sigma_w^2(\tau) \;=\; \mathrm{Var}\big[w_{\text{total}}\big]_{\text{tardío}} \,.
$$

Resultados cualitativos:

- **Ruido blanco** ($\tau \to 0$): $Q$ se degrada (picos anchos, baja coherencia) y $\sigma_w$ crece; $w_{\text{total}}$ presenta inestabilidad/dispersión excesiva.  
- **Memoria finita** ($\tau>0$ en banda óptima): $Q$ aumenta y $\sigma_w$ disminuye; $w_{\text{total}}$ converge de forma robusta al régimen *vacuum-like* ($\langle w\rangle \approx -1$).

> Conclusión (G): la **memoria** $\tau$ no es un detalle numérico; es el **parámetro físico** que **templa** el sistema. *Sin memoria no hay resiliencia*.


# 6. Discusión y Comparación

Esta sección contrasta el marco propuesto con líneas clásicas de la literatura: inflación estocástica tipo Starobinsky (ruido blanco), *warm inflation* (baño térmico exógeno), *stochastic gravity* (tratamiento cuántico profundo del ruido), enfoques PT/pseudo-Hermíticos, y modelos de quintesencia de un campo. El foco está en **qué añade** la **geometría-estocástica a dos campos** con memoria finita del ruido y selección dinámica del subespacio físico.

---

## 6.1 Síntesis conceptual

- **Sombra (estructura geométrica):** el uso de un espacio tipo Krein legitima un modo taquiónico sin violar la unitariedad observacional tras la proyección con $(\eta,C)$.  
- **Huella (ruido con memoria):** el ruido no es blanco; está **ligado a la geometría** vía $T_{GH}=\tfrac{H}{2\pi}$ y posee **memoria** $\tau>0$, condición clave para la **resiliencia** del atractor.  
- **Oscilación (atractor físico):** la dinámica acoplada con disipación $3H$ y ruido OU produce **ciclo límite estocástico**, coherencia espectral (alto $Q$) y transiciones naturales *matter-like* $\leftrightarrow$ *vacuum-like*.

---

## 6.2 Comparativa con marcos existentes

| Marco | Rasgos nucleares | En qué difiere el presente modelo |
|---|---|---|
| **Inflación estocástica (Starobinsky, 1986)** | Ruido **blanco** añadido al campo inflatón; difusión en espacio de configuraciones. | El ruido es **coloreado** (OU) y su intensidad se **auto-regula** con $H$ vía $T_{GH}$; se emplean **dos campos acoplados** y se evidencia un **atractor oscilatorio** tardío. |
| **Warm inflation (Berera)** | Fricción/baño **térmico exógeno**; producción de radiación durante inflación. | La “temperatura” **no** es un baño externo: $T_{GH}$ es **geométrica**. La disipación $3H$ y la **memoria $\tau$** sustituyen el acoplamiento a un reservorio ad hoc. |
| **Stochastic Gravity (Calzetta–Hu)** | Ruido derivado de operadores cuánticos (enfoque de primeros principios). | Aquí se implementa un **esquema efectivo** y **numérico** con OU **autoconsistente**; es compatible con una futura derivación *ab initio* (se sugiere en líneas futuras con Schwinger–Keldysh). |
| **PT/pseudo-Hermitismo (Bender, Mannheim)** | Espectros reales con operadores no-Hermíticos y métricas efectivas. | Se **traduce** ese andamiaje a cosmología: $(\eta,C)$ **selecciona dinámicamente** $\mathcal{H}_{\text{phys}}$ bajo expansión + ruido, dando un sentido físico a la “sombra” taquiónica. |
| **Quintesencia (1 campo)** | Un solo campo suave ajusta $w(t)$. | **Dos campos + ruido geométrico con memoria** generan **transiciones emergentes** *matter/vacuum-like* y un **tardío** con $\langle w\rangle\!\to\!-1$ **sin** fine-tuning extremo. |

---

## 6.3 Rol de la memoria frente a ruido blanco

Con **ruido blanco** ($\tau\to 0$), el sistema pierde coherencia: el pico espectral se ensancha ($Q\downarrow$) y $w_{\text{total}}$ exhibe mayor varianza. Con **memoria finita** ($\tau>0$), el acoplamiento “geometría $\leftrightarrow$ fluctuación” estabiliza la órbita y reduce la dispersión:

$$
Q(\tau)\;\uparrow
\quad\text{y}\quad
\sigma_w(\tau)\;\downarrow
\quad \text{para}\ \tau \ \text{en una banda óptima}\,.
$$

Físicamente, la **memoria** actúa como *temple* del ruido: transmite información de la geometría (vía $H$) con retardo suficiente para sostener coherencia.

---

## 6.4 Observables y fenomenología efectiva

- **Ecuación de estado tardía:** histograma concentrado alrededor de $\langle w\rangle\!\approx\!-1$ con cola controlada por $(g,\lambda_i,\tau,\alpha_i)$.  
- **Fracciones de energía** $(\Omega_\phi,\Omega_\chi)$: muestran *cross-talk* modulando la partición *matter/vacuum-like* en la aproximación al atractor.  
- **Espectros de potencia**: un pico dominante $f_0$ y armónicos débiles; el ancho $\Delta f$ sirve como **termómetro de coherencia**.

> Implicación: el marco sugiere una **unificación efectiva** (geométrico-estocástica) de energía y materia oscuras mediante una **dinámica acoplada** modulada por el **horizonte**.

---

## 6.5 Limitaciones y alcance

1. **Homogeneidad del fondo:** aquí se analiza el **modo cero**. Falta propagar perturbaciones espaciales para comparar con **CMB/LSS**.  
2. **Efectividad del ruido:** el OU geométrico es un **modelo efectivo**; su derivación desde **Schwinger–Keldysh** es una línea prioritaria.  
3. **Espacio de parámetros:** el barrido es ilustrativo; un ajuste **Bayesiano** (Planck 2018, BAO, SNe) está en “Trabajos futuros”.

---

## 6.6 Conclusión integradora

El marco **geométrico–estocástico de dos campos** con **proyección pseudo-Hermítica** y **ruido con memoria ligado al horizonte** produce:

- **Atracción oscilatoria** (coherencia con $Q$ elevado).  
- **Transiciones emergentes** *matter-like* $\leftrightarrow$ *vacuum-like*.  
- **Tardío vacuum-like** robusto con $\langle w\rangle\!\to\!-1$.  

La **memoria** $\tau$ no es un detalle técnico: es la **condición física** que permite **resiliencia**. El siguiente paso es cuantificar estas predicciones en perturbaciones y datos observacionales.


# 7. Conclusiones

Proponemos un marco **geométrico–estocástico** con dos campos acoplados, proyección pseudo-Hermítica y ruido con **memoria** ligado al horizonte. Las conclusiones principales son:

1. **Coherencia con “sombra” controlada.** La extensión tipo Krein permite alojar un modo taquiónico sin violar la unitariedad observacional tras la proyección con $(\eta,C)$:
   
$$
H_{\text{tot}}^{\dagger} \;=\; \eta_C\, H_{\text{tot}}\, \eta_C^{-1}
$$
   
   con métrica efectiva positiva $\eta_C>0$ en $\mathcal{H}_{\text{phys}}$.

2. **Lazo geometría–ruido.** La expansión regula **disipación** y **fluctuación** mediante
   
$$
T_{GH} \;=\; \frac{H}{2\pi}\,,
$$
   
   de modo que el acoplamiento “geometría $\leftrightarrow$ ruido” se cierra de forma autoconsistente.

3. **Atractor oscilatorio.** La dinámica combinada (disipación $3H$ + OU con memoria) no colapsa en un punto fijo, sino que conduce a un **ciclo límite estocástico** con coherencia espectral (factor de calidad $Q$ elevado).

4. **Fenomenología efectiva oscura.** El sistema exhibe transiciones naturales *matter-like* ($w\!\approx\!0$) $\leftrightarrow$ *vacuum-like* ($w\!\approx\!-1$) y un régimen tardío con
   
$$
\langle w \rangle \;\approx\; -1\,,
$$
   
   sugiriendo una **unificación efectiva** (geométrica–estocástica) de materia y energía oscuras.

5. **Memoria como condición física.** El tiempo de correlación $\tau$ **templa** el sistema: para $\tau>0$ (banda óptima) crece $Q(\tau)$ y disminuye la varianza de $w_{\text{total}}$; con ruido blanco ($\tau\!\to\!0$) se pierde coherencia.

---

## Líneas futuras

- **Ajuste Bayesiano** a datos (Planck 2018, BAO, SNe) y exploración sistemática del espacio de parámetros $(g,\lambda_i,\alpha_i,\tau)$.
- **Perturbaciones espaciales** y espectros (CMB/LSS), incluida posible **no-Gaussianidad** inducida por memoria.
- **Derivación ab initio** del ruido coloreado desde **Schwinger–Keldysh** para consolidar los kernels no locales.
- **Extensiones multiescala** (tres campos, acoplamientos cruzados dependientes de $H$) y análisis de robustez del atractor.

> Síntesis: **Sombra (Krein) + Huella (memoria) + Oscilación (atractor)** conforman un mecanismo de **resiliencia cosmológica** regido por el horizonte.


---

# Apéndice A — Estructura pseudo-Hermítica (Krein) resumida

## A.1 Métrica, operador \(C\) y proyección

Usamos un espacio tipo **Krein** con métrica indefinida actuando sobre \((\phi,\chi)\):

$$
\eta \;=\; \mathrm{diag}(-1,\,+1)\,.
$$

Definimos un **operador de forma** \(C\) tal que \

$$
(C^2=\mathbb{1}\) y \([C,H_{\text{tot}}]=0\)
$$

La **métrica positiva efectiva** en el subespacio físico es

$$
\eta_C \;\equiv\; C\,\eta \;>\; 0 \quad \text{en } \mathcal{H}_{\text{phys}}\,,
$$

y satisface la condición de **pseudo-Hermitismo**

$$
H_{\text{tot}}^{\dagger} \;=\; \eta_C \, H_{\text{tot}} \, \eta_C^{-1}\,,
$$

que garantiza **espectro real** y **evolución unitaria** restringida a \(\mathcal{H}_{\text{phys}}\).

La **proyección** al subespacio físico se implementa con

$$
\Pi_{\text{phys}} \;=\; \tfrac12\big(\mathbb{1}+C\big)\,.
$$

## A.2 Intuición operativa

- La signatura de \(\eta\) **legitima** un modo “taquiónico” sin romper la unitariedad observable tras la proyección.  
- El par \((\eta,C)\) **reetiqueta normas**: el sector de norma negativa queda **suprimido dinámicamente** (expansión + ruido coloreado).  
- La dinámica efectiva conserva la **coherencia** en \(\mathcal{H}_{\text{phys}}\).

---

# Apéndice B — Fokker–Planck ampliada (descripción de conjunto)

## B.1 Variables y SDEs

Definimos el vector de estado

$$
\mathbf{X} \;=\; (\phi,\;\dot\phi,\;\chi,\;\dot\chi,\;\zeta_\phi,\;\zeta_\chi)\,,
$$

con procesos de **Ornstein–Uhlenbeck** (OU) ligados a la geometría:

$$
\dot\zeta_\phi \;=\; -\frac{\zeta_\phi}{\tau_\phi}
\;+\; \sqrt{\frac{2\,\Gamma_\phi\,T_{GH}}{\tau_\phi^2}}\,\xi_\phi(t)\,,
\qquad
\dot\zeta_\chi \;=\; -\frac{\zeta_\chi}{\tau_\chi}
\;+\; \sqrt{\frac{2\,\Gamma_\chi\,T_{GH}}{\tau_\chi^2}}\,\xi_\chi(t)\,,
$$

donde 

$$
\(T_{GH}=\tfrac{H}{2\pi}\), \(\Gamma_i=\alpha_i\,3H\) y \(\xi_i(t)\) 
$$

son ruidos blancos unitarios. Las ecuaciones de movimiento son

$$
\ddot\phi \;=\; -3H\,\dot\phi \;-\; \partial_\phi V(\phi,\chi) \;+\; \zeta_\phi \,,
\qquad
\ddot\chi \;=\; -3H\,\dot\chi \;-\; \partial_\chi V(\phi,\chi) \;+\; \zeta_\chi \,.
$$

## B.2 Ecuación de Fokker–Planck tipo Kramers

Para la densidad 

$$
\(P(\mathbf{X},t)\),
$$

$$
\partial_t P \;=\; -\sum_i \partial_{x_i}\!\big[A_i(\mathbf{X})\,P\big]
\;+\; \tfrac12 \sum_{i,j} \partial_{x_i}\partial_{x_j}\!\big[D_{ij}(\mathbf{X})\,P\big]\,,
$$

donde los **drifts** \(A_i\) recogen los términos deterministas

$$
\((\dot\phi,\; -3H\dot\phi-\partial_\phi V+\zeta_\phi,\; \dot\chi,\; -3H\dot\chi-\partial_\chi V+\zeta_\chi,\; -\zeta_\phi/\tau_\phi,\; -\zeta_\chi/\tau_\chi)\)
$$

y la **difusión** es no nula en el subbloque \(\zeta\)-\(\zeta\):

$$
D_{\zeta_\phi\zeta_\phi} \;=\; \frac{2\,\Gamma_\phi\,T_{GH}}{\tau_\phi^2}\,,
\qquad
D_{\zeta_\chi\zeta_\chi} \;=\; \frac{2\,\Gamma_\chi\,T_{GH}}{\tau_\chi^2}\,,
$$

siendo cero en los demás elementos (difusión aditiva sólo en \(\zeta\)).

## B.3 Estado cuasi-estacionario y reducción

En régimen tardío, cuando 

$$
\(H\simeq\text{cte}\)
$$

y la dinámica orbita un **atractor oscilatorio**, se verifica

$$
\partial_t P_{\text{st}} \;\approx\; 0\,,
$$

con 

$$
\(P_{\text{st}}\)
$$

aproximadamente **gaussiana** alrededor de la órbita límite y varianzas regidas por 

$$
\(\big(T_{GH},\tau\big)\)
$$

Bajo **reducción adiabática**, se puede integrar el subespacio de 

$$
\(\zeta\)
$$

y obtener un **kernel de memoria** efectivo para 

$$
\((\phi,\dot\phi,\chi,\dot\chi)\)
$$

## B.4 Métricas de coherencia y estabilidad

El **factor de calidad** espectral y la **varianza tardía** de la ecuación de estado brindan diagnósticos compactos:

$$
Q \;=\; \frac{f_0}{\Delta f}\,,
\qquad
\sigma_w^2 \;=\; \mathrm{Var}\!\left[w_{\text{total}}\right]_{\text{tardío}}\,.
$$

Empíricamente,
- ruido **blanco**

$$
\((\tau\to 0)\): \(Q\downarrow\)
$$

$$
\(\sigma_w\uparrow\)
$$

- **memoria finita**

$$
\((\tau>0)\): \(Q\uparrow\), \(\sigma_w\downarrow\)
$$

en una banda óptima.

> Lectura: la **memoria** \(\tau\) *templa* el ruido y transmite información geométrica con retardo suficiente para sostener coherencia.


# Referencias

[1] **Starobinsky, A. A.** (1986). *Stochastic de Sitter (inflationary) stage in the early Universe*. En: **Field Theory, Quantum Gravity and Strings**, Lecture Notes in Physics, Vol. 246, pp. 107–126. Springer. ISBN: 978-3-540-16758-0.

[2] **Berera, A.** (1995). *Warm Inflation*. **Physical Review Letters** 75, 3218–3221. DOI: 10.1103/PhysRevLett.75.3218.

[3] **Calzetta, E., & Hu, B.-L.** (2008). *Nonequilibrium Quantum Field Theory*. Cambridge University Press. ISBN: 978-0-521-86978-1.

[4] **Hu, B.-L., & Verdaguer, E.** (2020). *Stochastic Gravity: Noise, Fluctuations, and Non-Equilibrium Processes in Gravity*. Cambridge University Press. ISBN: 978-1-107-02425-1.

[5] **Bender, C. M., & Mannheim, P. D.** (2011). *{\it PT} symmetry and real spectra in non-Hermitian Hamiltonians* (contexto pseudo-Hermítico relacionado). **Physical Review D** 84, 105038. DOI: 10.1103/PhysRevD.84.105038.

[6] **Bender, C. M.** (2007). *Making sense of non-Hermitian Hamiltonians*. **Reports on Progress in Physics** 70, 947–1018. DOI: 10.1088/0034-4885/70/6/R03.

[7] **Gibbons, G. W., & Hawking, S. W.** (1977). *Cosmological event horizons, thermodynamics, and particle creation*. **Physical Review D** 15, 2738–2751. DOI: 10.1103/PhysRevD.15.2738.

[8] **Uhlenbeck, G. E., & Ornstein, L. S.** (1930). *On the Theory of the Brownian Motion*. **Physical Review** 36, 823–841. DOI: 10.1103/PhysRev.36.823.

[9] **Planck Collaboration** (2020). *Planck 2018 results. VI. Cosmological parameters*. **Astronomy & Astrophysics** 641, A6. DOI: 10.1051/0004-6361/201833910.

[10] **Kiefer, C.** (2012). *Quantum Gravity* (3rd ed.). Oxford University Press. ISBN: 978-0-19-958520-5.

---

### Referencias complementarias (opcional)

[11] **Starobinsky, A. A., & Yokoyama, J.** (1994). *Equilibrium state of a self-interacting scalar field in the de Sitter background*. **Physical Review D** 50, 6357–6368. DOI: 10.1103/PhysRevD.50.6357.

[12] **Bender, C. M.** (2005). *Introduction to PT-Symmetric Quantum Theory*. **Contemporary Physics** 46, 277–292. DOI: 10.1080/00107500072632.

[13] **Grimbert, E., & Rigopoulos, G.** (2024). *Stochastic inflation with colored noise* (ejemplo reciente sobre memoria en ruido). **JCAP** 03, 015. DOI: 10.1088/1475-7516/2024/03/015.

---



# Capítulos 2–6 (Texto completo con fórmulas renderizables)

> Archivo sugerido: `texto/capitulos_2_6.md`  
> Formato: **Markdown** con **LaTeX** (MathJax).  
> Consejos:  
> - En GitHub, las fórmulas LaTeX se renderizan bien en **.md** si usas `$ ... $` (inline) y `$$ ... $$` (display).  
> - Evita caracteres repetidos o pegados que rompan el math (ej.: `η=diag(−1,+1)` → `\eta=\mathrm{diag}(-1,+1)`).

---

## Capítulo 2 — Modelo I: Espacio de Krein y la Sombra Taquiónica

### 2.1. Motivación: La sombra necesaria
Toda teoría completa necesita su **sombra**. En física, esa sombra son los **modos de energía negativa**, los estados “prohibidos” que el formalismo ordinario intenta descartar. Aquí, la sombra se legitima: no es ruido, sino **memoria estructural del cosmos**.

El espacio de **Krein** reemplaza la geometría positiva de Hilbert por una **métrica indefinida**:

$$
\eta=\mathrm{diag}(-1,+1).
$$

El signo negativo no es un error: es la huella del **desequilibrio** que mantiene al universo en expansión.

---

### 2.2. Definición del espacio y métrica
Sea $\mathcal{K}$ un espacio vectorial complejo con forma bilineal indefinida

$$
\langle \psi_1,\psi_2\rangle_\eta=\psi_1^\dagger\,\eta\,\psi_2,
\qquad
\eta=\begin{pmatrix}-1&0\\0&+1\end{pmatrix}.
$$

El **campo taquiónico** $\phi$ vive en el subespacio de **norma negativa**; el campo estable $\chi$, en el **positivo**.  
La métrica efectiva **redefine** la noción de probabilidad: la estabilidad no depende solo del signo del término cuadrático, sino del **equilibrio dinámico** entre subespacios.

---

### 2.3. Hamiltoniano total

$$
H_{\text{tot}}=\frac{1}{2}p_\phi^2-\frac{1}{2}m_\phi^2\phi^2+\frac{\lambda_\phi}{4}\phi^4
\;+\;\frac{1}{2}p_\chi^2+\frac{1}{2}m_\chi^2\chi^2+\frac{\lambda_\chi}{4}\chi^4
\;+\;\frac{1}{2}g^2\phi^2\chi^2+V_0.
$$

El término **negativo** en $H_\phi$ no destruye la unitariedad si se **redefine el producto interno** mediante un operador de forma $C$ que cumple

$$
[C,H_{\text{tot}}]=0,
\qquad
\eta_C=C\,\eta>0.
$$

De este modo,

$$
H_{\text{tot}}^\dagger=\eta_C\,H_{\text{tot}}\,\eta_C^{-1},
$$

y el **espectro permanece real**.  
La métrica $\eta_C$ es el **puente** entre la sombra y la coherencia: el universo se mantiene unitario gracias a la **memoria de lo que niega**.

---

### 2.4. Dinámica cosmológica y acoplamiento al ruido
En un espacio **FRW** plano (tomando $8\pi G=1$), el sistema obedece:

$$
H^2=\frac{1}{2}\big(\dot\phi^2+\dot\chi^2\big)+V(\phi,\chi),
$$

con

$$
V(\phi,\chi)=
-\tfrac{1}{2}m_\phi^2\phi^2+\tfrac{\lambda_\phi}{4}\phi^4
+\tfrac{1}{2}m_\chi^2\chi^2+\tfrac{\lambda_\chi}{4}\chi^4
+\tfrac{1}{2}g^2\phi^2\chi^2+V_0.
$$

El ruido estocástico $\zeta_\phi,\zeta_\chi$ se modela con **Ornstein–Uhlenbeck (OU)**:

$$
\dot\zeta_i=-\frac{\zeta_i}{\tau_i}+\sqrt{\frac{2\,\Gamma_i\,T_{GH}}{\tau_i^2}}\,\xi_i(t),
\qquad
i\in\{\phi,\chi\},
$$

donde $T_{GH}=\tfrac{H}{2\pi}$ y $\Gamma_i=\alpha_i\,3H$.

Ecuaciones de movimiento:

$$
\ddot\phi=-3H\dot\phi-\partial_\phi V+\zeta_\phi, \qquad
\ddot\chi=-3H\dot\chi-\partial_\chi V+\zeta_\chi.
$$

El **ruido coloreado** introduce **memoria temporal** ($\tau>0$): cada fluctuación conserva un eco de sí misma.  
- Si $\tau=0$ el sistema tiende a un gas térmico (ruido blanco).  
- Si $\tau>0$ emerge **resiliencia**: **oscilaciones persistentes** del parámetro de estado $w=p/\rho$.

---

### 2.5. Atractores oscilatorios y resiliencia
La dinámica exhibe tres regímenes:
- **Matter-like**: $w\approx 0$ (dominan términos cinéticos).  
- **Vacuum-like**: $w\approx -1$ (domina el potencial).  
- **Intermedio**: la memoria del ruido fuerza oscilaciones cuasi-periódicas con **atractores estocásticos**.

Promedio típico:

$$
\langle w(t)\rangle \approx -1 + A\,e^{-t/\tau}\cos(\omega t),
$$

donde $A$ depende de $g,\lambda_i,\Gamma_i$.  
El término $e^{-t/\tau}$ determina la **duración de la memoria cósmica**.

---

### 2.6. Interpretación física
- El espacio de **Krein** legitima modos “negativos” como parte necesaria de la **completitud**.  
- El ruido **autoconsistente** impide el colapso térmico: la estructura se mantiene por la fluctuación.  
- La **memoria** ($\tau>0$) es un análogo cosmológico de la **conciencia del sistema**: recordar su propia fluctuación permite **adaptarse**.

---

### 2.7. Predicciones observacionales mínimas
- **Ecuación de estado oscilante**: modulaciones pequeñas en $w(z)$ detectables como corrugaciones en $H(z)$ o en $f\sigma_8(z)$.  
- **No-gaussianidad metaestable**: el ruido coloreado introduce correlaciones de fase (CMB/LSS débiles).  
- **Rango de estabilidad**: resiliencia para $\tau\sim 10^{2}$–$10^{3}\,H^{-1}$ (orden de magnitud).

---

### 2.8. Comentario final
Este modelo no busca “corregir” el universo, sino **comprender su ritmo**.  
El cosmos **oscila porque recuerda**; el olvido absoluto sería equilibrio térmico, **silencio**.  
En la música del espacio-tiempo, el **taquión** no es disonancia: es la **nota que falta** para que la melodía tenga sentido.

---

## Capítulo 3 — Modelo II: Simetría PT y la Ganancia del Caos

### 3.1. Motivación: El espejo complejo
Si el Modelo I legitimaba la sombra con la métrica de Krein, el Modelo II la **internaliza**: el universo equilibra energía positiva y negativa mediante un **campo complejo**

$$
\Phi=\phi_r+i\,\phi_i,
$$

cuyo espectro **permanece real** gracias a la **simetría PT**:

$$
V_{\text{PT}}(\Phi)=V_0+a\,\Phi^2+i\,b\,\Phi^3+c\,\Phi^4,\qquad a,b,c\in\mathbb{R}.
$$

El término imaginario $i\,b\,\Phi^3$ introduce una “**fuerza fantasma**” que alterna disociación y coherencia —eco del taquión de Krein, ahora **sin métrica negativa**.

---

### 3.2. Dinámica general

$$
\ddot\Phi+3H\dot\Phi+\frac{\partial V_{\text{PT}}}{\partial \Phi^\ast}=\zeta(t),
\qquad
\dot\zeta=-\frac{\zeta}{\tau}+\sqrt{\frac{2\,\Gamma\,T_{GH}}{\tau^2}}\,\xi(t),
\quad T_{GH}=\frac{H}{2\pi}.
$$

Separando partes reales:

$$
\begin{cases}
\ddot\phi_r=-3H\dot\phi_r-\partial_{\phi_r}V_R+\partial_{\phi_i}V_I+\zeta_r,\\[4pt]
\ddot\phi_i=-3H\dot\phi_i-\partial_{\phi_i}V_R-\partial_{\phi_r}V_I+\zeta_i,
\end{cases}
$$

donde $V_R,V_I$ son partes real e imaginaria del potencial.  
La simetría PT exige oscilación alrededor de una curva $\phi_i=f(\phi_r)$ que mantiene **espectro real**.

---

### 3.3. Condición de realidad y “balance de flujo”
El sistema conserva la **pseudonorma**

$$
\mathcal{N}=|\phi_r|^2-|\phi_i|^2,
$$

constante si ciertos balances entre $b/a$ y $H$ se cumplen (esquema fenomenológico).  
Interpretación: la expansión geométrica **ajusta su respiración** para que el flujo complejo no rompa la realidad del espectro.

---

### 3.4. Interpretación física
- **Krein $\to$ PT**: la sombra internalizada en la parte imaginaria del campo, sin destruir la realidad global.  
- **Memoria geométrica**: el término $3H\dot\Phi$ actúa como disipación dinámica, análogo al amortiguamiento OU; la **expansión** es fuente de memoria.  
- **Ruido autoconsistente** vía $T_{GH}$ estabiliza el régimen estadístico.

---

### 3.5. Atractores PT y transiciones
Promedio típico:

$$
\langle w(t)\rangle \approx -1 + A_{\text{PT}}\,e^{-t/\tau_{\text{PT}}}\cos(\omega_{\text{PT}} t+\delta),
$$

con $\omega_{\text{PT}}\propto b/a$ (fenomenológico).  
- Si $b\to 0$, se recupera el Modelo I.  
- Si $b$ crece, aparece **oscilación autoexcitada** (tipo láser PT).

---

### 3.6. Predicciones diferenciales
- **Oscilaciones $w(z)$ más rápidas** (frecuencia $\sim b/a$).  
- **Modulación de fase** real/imag $\Rightarrow$ posibles **firmas tensoriales** (CMB B-modes).  
- **Transiciones “láser cósmico”**: ráfagas breves de aceleración seguidas de relajación (señales en jerk/snap).

---

### 3.7. Comparativa cualitativa I ↔ II
| Propiedad | Modelo I (Krein) | Modelo II (PT) |
|---|---|---|
| Sombra | Métrica indefinida $\eta$ | Parte imaginaria del campo |
| Conservación | Unitariedad restaurada $\eta_C$ | Simetría PT global |
| Memoria | $\tau$ del OU | $\tau$ geométrica $\sim H^{-1}$ |
| Atractores | Ciclos límite suaves | Oscilaciones autoexcitadas |
| Observables extra | Modulación suave de $w(z)$ | Polarización tensorial |

---

## Capítulo 4 — Modelo III: Fluidos con Memoria y Cosmología de la Persistencia

### 4.1. Motivación: Del campo al medio
Todo campo, visto desde lejos, se comporta como un **fluido**.  
Pregunta: ¿puede un fluido cósmico—**sin taquiones ni PT**—exhibir el mismo pulso oscilatorio si su ecuación de estado **conserva memoria**?  
Respuesta: **sí**. Lo que antes era **ruido coloreado** ahora es **retardo causal** en las **relaciones constitutivas**.

---

### 4.2. Variante A — *k*-essence con memoria
Partimos de un lagrangiano no canónico:

$$
\mathcal{L}=K(X)-V(\phi),\qquad X=\tfrac{1}{2}\partial_\mu\phi\,\partial^\mu\phi,
$$

$$
p=K(X)-V,\qquad \rho=2XK_X-K+V.
$$

Incorporamos memoria (retardo):

$$
\ddot{\phi}(t)+3H\dot{\phi}(t)+\int_0^t \mathcal{K}_\tau(t-t')\,\frac{\partial V[\phi(t')]}{\partial \phi}\,dt'=0,
$$

con **kernel exponencial** (análogo a OU):

$$
\mathcal{K}_\tau(t-t')=\frac{1}{\tau}\,e^{-(t-t')/\tau}.
$$

---

### 4.3. Variante B — Dos fluidos acoplados con retardo
Dos componentes efectivas:  
- $\rho_m(t)$ (matter-like, $w_m\approx 0$)  
- $\rho_v(t)$ (vacuum-like, $w_v\approx -1$)

Acopladas mediante un **término de intercambio retardado**:

$$
\begin{cases}
\dot{\rho}_m+3H(1+w_m)\rho_m=+Q[\rho_v](t),\\[4pt]
\dot{\rho}_v+3H(1+w_v)\rho_v=-Q[\rho_v](t),
\end{cases}
\qquad
Q[\rho_v](t)=\int_0^t \mathcal{K}_\tau(t-t')\,\rho_v(t')\,dt'.
$$

El retardo **estabiliza**: con $\tau=0$ el sistema tiende a equilibrio térmico; con $\tau>0$ **oscila** entre regímenes.

---

### 4.4. Ecuación efectiva de estado

$$
w_{\text{eff}}(t)=\frac{p_m+p_v}{\rho_m+\rho_v}
\;\approx\;
-1 + A\,e^{-t/\tau}\cos(\omega t+\delta),
$$

idéntica en forma a I–II, pero donde $A,\omega$ emergen del **acoplamiento retardado**.

---

### 4.5. Correspondencia entre modelos

| Elemento | I (Krein) | II (PT) | III (Fluido) |
|---|---|---|---|
| Fuente de memoria | OU autoconsistente | Disipación geométrica (PT) | Kernel retardado $\mathcal{K}_\tau$ |
| Dualidad matter/vacuum | Dos campos $(\phi,\chi)$ | Partes real/imag de $\Phi$ | Dos fluidos $(\rho_m,\rho_v)$ |
| Oscilaciones de $w$ | Por $\tau$–OU | Por fase compleja | Por retardo causal |
| Interpretación | Memoria cuántica | Memoria geométrica | Memoria termodinámica |

---

### 4.6. Predicciones observacionales
- **Ondulaciones** en $H(z)$ de baja frecuencia.  
- **Señales no armónicas** en la reconstrucción de $w(z)$ (SNe Ia/BAO).  
- **Estabilidad térmica**: la memoria regula la energía oscura sin quintesencia exótica.

---

### 4.7. Interpretación poética
El universo no solo se expande: **recuerda** cómo lo hizo.  
Lo que en física es un kernel exponencial, en poesía es una **cicatriz**.

---

### 4.8. Conclusión del tríptico
Los tres modelos convergen en una tesis: **la memoria es estructural**.  
- I: la sombra (Krein) legitima la inestabilidad.  
- II: PT contiene la pérdida dentro de la ganancia.  
- III: sin campos, la **memoria causal** basta para producir **ritmo**.

---

## Capítulo 5 — Comparación Integral de los Modelos I–III

### 5.1. Invariantes comunes
- **Memoria** como propiedad estructural ($\tau>0$ u análogo).  
- **Atractores oscilatorios** modulando $w(t)$.  
- **Resiliencia**: la memoria evita el colapso a equilibrio trivial.

---

### 5.2. Estructura formal (lado a lado)
*(resumen compacto; ampliar en el libro)*

| Rasgo | I (Krein) | II (PT) | III (Fluido) |
|---|---|---|---|
| GdL | $\phi$ (taq.), $\chi$ (estable) | $\Phi=\phi_r+i\phi_i$ | $\rho_m,\rho_v$ o *k*-essence |
| Sombra | $\eta$ indefinida, $\eta_C$ | Parte imag. del potencial | Retardo causal |
| Memoria | OU ($\tau$, $\Gamma=\alpha\,3H$) | $\tau\sim H^{-1}$, $b/a$ | Kernel $\mathcal{K}_\tau$ |
| Atractores | Estocásticos suaves | Autoexcitados | Hopf por retardo |
| Observables | $w(z)$ ondulado suave | firmas tensoriales posibles | corrugaciones $H(z)$ |

---

### 5.3. Mapeo paramétrico (correspondencias)
- **Intensidad de memoria**:  
  I: $\tau$ (OU); II: $\tau_{\text{PT}}\sim H^{-1}$ y $b/a$; III: $\tau$ del kernel.  
- **Frecuencia**:  
  I depende de $m_\phi,m_\chi,g,\lambda_i$; II $\propto b/a$; III del acoplamiento retardado.  
- **Amplitud $A$** en $\langle w\rangle$: crece con memoria/acoplo; decrece con fricción $3H$.

---

### 5.4. Discriminadores observacionales
- **Rápidas y coherentes (H & CMB)** $\Rightarrow$ II.  
- **Corrugaciones suaves sin tensoriales** $\Rightarrow$ III.  
- **Modulaciones débiles y estables** $\Rightarrow$ I.

---

### 5.5. Estabilidad y bifurcaciones (esbozo)
- I: OU con $\tau>0$ + $3H$ $\Rightarrow$ ciclos límite estocásticos.  
- II: transición PT $\to$ broken-PT al cruzar umbral $b/a$ (Hopf no lineal).  
- III: retardo $\Rightarrow$ Hopf retardado; rango estable si $\int \mathcal{K}_\tau<\text{const.}$

---

### 5.6. Falsabilidad mínima
- Si no hay modulaciones $\Delta w\gtrsim 0.02$ en $0<z<2$, los tres modelos se restringen a amplitudes muy bajas (cercanos a $\Lambda$CDM).  
- Oscilaciones rápidas coherentes favorecen II; retardos suaves favorecen III o I.

---

## Capítulo 6 — Ventanas Observacionales y Marco Bayesiano

### 6.1. Objetivo
Confrontar la hipótesis de **universo con memoria oscilante** con datos presentes/futuros, mediante un **marco Bayesiano** transparente.  
Parámetros clave:

$$
\theta=\{A,\omega,\tau\}.
$$

---

### 6.2. Parametrización universal de $w(z)$

$$
w(z)=-1+A\,e^{-z/z_\tau}\cos\!\big[\omega\ln(1+z)+\delta\big],
\qquad
z_\tau=c\,H_0\,\tau.
$$

- I: $A,\omega$ ligados a $m_\phi,m_\chi,g,\lambda_i$; $\tau$ del OU.  
- II: $A\propto b/a$, $\omega\propto b/a$, $\tau\approx H^{-1}$.  
- III: $A,\omega$ del kernel retardado; $\tau$ causal térmica.  

**Priors físicos (ejemplo):** $0<A<0.3,\; 0<\omega<10,\; 0.1<\tau H_0<5$.

---

### 6.3. Datasets
- **Expansión:** $H(z)$ (cronometría), SNe Ia (Pantheon), BAO (BOSS/eBOSS/DESI).  
- **Estructura:** $f\sigma_8(z)$ (KiDS/DES/Euclid).  
- **CMB:** Planck + ACT/SPT (ISW, B-modes).

---

### 6.4. Verosimilitud (ejemplo)

$$
\mathcal{L}(\theta|\text{datos})
\propto
\exp\!\left[-\frac{1}{2}\sum_i \frac{\big(H_{\text{obs}}(z_i)-H_{\text{mod}}(z_i;\theta)\big)^2}{\sigma_i^2}\right],
$$

ampliable a $D_L(z)$, $f\sigma_8(z)$ e ISW.  
**Selección de modelos:** AIC/BIC/Evidencia.

---

### 6.5. Pipeline sugerido
Ecuación de Friedmann con $w(z)$:

$$
H^2(z)=H_0^2\!\left[\Omega_m(1+z)^3+\Omega_r(1+z)^4
+\Omega_{DE}\exp\!\Big(3\!\int_0^z\frac{1+w(z')}{1+z'}dz'\Big)\right].
$$

Validar con reconstrucción no paramétrica (Gaussian Process) y **stress tests** sintéticos.

---

### 6.6. Escenarios de falsación (resumen)
- **Oscilaciones rápidas** coherentes $\Rightarrow$ II.  
- **Corrugaciones suaves** sin tensoriales $\Rightarrow$ III.  
- **Metaestabilidad** $w\approx -1\pm 0.05$ sostenida $\Rightarrow$ I.  
- **Ausencia total de modulación** $\Rightarrow$ $\Lambda$CDM.

---

> **Nota de edición:** Puedes dividir este archivo en `capitulo_2.md`, `capitulo_3.md`, `capitulo_4.md`, `capitulo_5.md`, `capitulo_6.md`.  
> Para PDF/LaTeX: compilar con `pandoc` o integrar en tu *paper* (sección “Texto” del libro).


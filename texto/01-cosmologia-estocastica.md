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

2. Fundamentos Teóricos
2.1 Espacio de Krein, pseudo-Hermitismo y proyección física

Usamos un espacio con métrica indefinida (tipo Krein) para alojar un grado de libertad taquiónico sin perder unitariedad en el subespacio físico. La métrica:

𝜂
=
d
i
a
g
(
−
1
,
+
1
)
η=diag(−1,+1)

actúa sobre el par de campos $(\phi,\chi)$, asignando signatura negativa al sector taquiónico.

Hamiltoniano homogéneo (modos de fondo):

𝐻
tot
=
(
1
2
𝑝
𝜙
2
−
1
2
𝑚
𝜙
2
𝜙
2
+
𝜆
𝜙
4
𝜙
4
)
+
(
1
2
𝑝
𝜒
2
+
1
2
𝑚
𝜒
2
𝜒
2
+
𝜆
𝜒
4
𝜒
4
)
+
1
2
𝑔
2
𝜙
2
𝜒
2
+
𝑉
0
.
H
tot
	​

=(
2
1
	​

p
ϕ
2
	​

−
2
1
	​

m
ϕ
2
	​

ϕ
2
+
4
λ
ϕ
	​

	​

ϕ
4
)+(
2
1
	​

p
χ
2
	​

+
2
1
	​

m
χ
2
	​

χ
2
+
4
λ
χ
	​

	​

χ
4
)+
2
1
	​

g
2
ϕ
2
χ
2
+V
0
	​

.

La inestabilidad de $\phi$ (masa imaginaria efectiva) no se interpreta como un fallo, sino como consecuencia de la signatura: el grado de libertad “en sombra” se controla a nivel geométrico.

Pseudo-Hermitismo y espectro real.
Introducimos un operador de forma $C$ (involución, $C^2=\mathbb{1}$) tal que $[C,H_{\text{tot}}]=0$. Definimos métrica efectiva positiva en el subespacio físico:

𝜂
𝐶
≡
𝐶
 
𝜂
>
0
en 
𝐻
phys
,
η
C
	​

≡Cη>0en H
phys
	​

,

con lo cual se cumple

𝐻
tot
†
=
𝜂
𝐶
 
𝐻
tot
 
𝜂
𝐶
−
1
,
H
tot
†
	​

=η
C
	​

H
tot
	​

η
C
−1
	​

,

lo que garantiza espectro real y evolución unitaria en $\mathcal{H}_\text{phys}$.

Proyector físico:

Π
phys
=
1
2
(
1
+
𝐶
)
.
Π
phys
	​

=
2
1
	​

(1+C).

Intuición: el par $(\eta,C)$ reetiqueta normas para que el sector observable tenga norma positiva; el sector de norma negativa queda suprimido dinámicamente.

2.2 Selección dinámica del subespacio físico

Con expansión y ruido coloreado (secciones 3–5), la combinación disipación cosmológica $3H$ + ruido con memoria (Ornstein–Uhlenbeck) actúa como filtro dinámico:

amortigua los modos con norma negativa,

estabiliza una órbita atractora en el subespacio físico,

y preserva la unitariedad efectiva al nivel de observables.

Ecuación de Friedmann (recordatorio):

𝐻
2
=
𝜌
tot
=
1
2
(
𝜙
˙
2
+
𝜒
˙
2
)
+
𝑉
(
𝜙
,
𝜒
)
.
H
2
=ρ
tot
	​

=
2
1
	​

(
ϕ
˙
	​

2
+
χ
˙
	​

2
)+V(ϕ,χ).

Puente a la Sección 3: especificaremos el ruido OU ligado a la temperatura del horizonte $T_{GH}=\tfrac{H}{2\pi}$ y mostraremos cómo la memoria $\tau$ controla la coherencia del atractor.

---

# 3. Modelo Cosmológico y Ruido Autoconsistente
*(…)*

# 4. Método Numérico
*(…)*

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

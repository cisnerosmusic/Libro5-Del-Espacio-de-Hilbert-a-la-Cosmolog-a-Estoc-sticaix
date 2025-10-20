# Cómo Contribuir

## 🎯 Tipos de Contribución Bienvenidos

Este es un proyecto en **dominio público (CC0)** que busca activamente colaboración para:
- ✅ Validación empírica con datos reales
- ✅ Correcciones matemáticas
- ✅ Mejoras de código
- ✅ Documentación y traducciones
- ✅ Críticas constructivas

---

## 👥 Para Diferentes Perfiles

### 🔬 Científicos / Cosmólogos

**Si tienes acceso a datos observacionales:**

1. **Revisa el marco teórico:**
   - [Capítulo 1: Cosmología Estocástica](../paper/full-text/01-cosmologia-estocastica.md)
   - [Modelos I-III](../paper/full-text/)
   
2. **Explora el código base:**
   - [`/code/src/cosmology/`](../code/src/cosmology/)
   - Notebooks explicativos en [`/code/notebooks/`](../code/notebooks/)

3. **Propón colaboración:**
   - Abre un [Issue tipo "Validation Collaboration"](https://github.com/cisnerosmusic/Libro5-Del-Espacio-de-Hilbert-a-la-Cosmolog-a-Estoc-sticaix/issues/new)
   - O contacta directamente: ernestocisnerosmusic@gmail.com

**Qué ofrezco:**
- Coautoría en papers de validación
- Código y framework completo
- Libertad total para modificar/extender
- Crédito explícito en todas las publicaciones

**Qué necesito:**
- Acceso a Pantheon+, DESI, Planck u otros datasets
- Infraestructura computacional para MCMC
- Expertise técnica en pipelines observacionales

---

### 💻 Programadores / Desarrolladores

**Formas de contribuir:**

#### 1. Mejoras de Código
```bash
# Fork del repositorio
git clone https://github.com/TU-USUARIO/Libro5-Del-Espacio-de-Hilbert-a-la-Cosmolog-a-Estoc-sticaix.git
cd Libro5-Del-Espacio-de-Hilbert-a-la-Cosmolog-a-Estoc-sticaix

# Crea rama para tu feature
git checkout -b feature/optimizacion-simulaciones

# Haz tus cambios
# ... edita código ...

# Commit con mensaje descriptivo
git commit -m "Optimize: Euler-Maruyama integration (2x faster)"

# Push y abre Pull Request
git push origin feature/optimizacion-simulaciones
```

#### 2. Tests Unitarios
```python
# Ejemplo de test bienvenido
def test_krein_stability():
    """Verifica que el modelo Krein converge."""
    params = default_params()
    results = simulate_krein(steps=10000, **params)
    assert results['H'][-1] > 0  # No colapsa
```

#### 3. Implementaciones en Otros Lenguajes
- **Julia:** Para performance
- **Rust:** Para sistemas embebidos
- **Mathematica:** Para análisis simbólico

#### 4. Visualizaciones
- Scripts para generar figuras del paper
- Dashboards interactivos (Streamlit, Plotly Dash)
- Animaciones 3D de atractores

**Estándares de código:**
- Python: PEP 8 (usa `black` para formatear)
- Docstrings: formato NumPy
- Tests: pytest cuando sea aplicable

---

### 📐 Matemáticos / Teóricos

**Áreas de interés:**

1. **Equivalencias formales:**
   - Demostrar rigurosamente Krein ↔ PT ↔ OU
   - Generalizar a N campos
   - Explorar conexiones con teorías existentes

2. **Análisis de estabilidad:**
   - Demostrar existencia de atractores
   - Condiciones necesarias/suficientes para τ > 0
   - Bifurcaciones en espacio de parámetros

3. **Extensiones teóricas:**
   - Incorporar perturbaciones espaciales
   - Acoplar con gravitación cuántica
   - Conectar con enfoques no-canónicos (Horndeski, f(R))

**Cómo contribuir:**
- Abre Issue describiendo tu enfoque
- Comparte preprints relacionados
- Propón colaboración en papers matemáticos

---

### 🎓 Estudiantes

**Proyectos de tesis/trabajos potenciales:**

#### Nivel Pregrado:
- Implementar simulaciones en Julia/Rust
- Crear visualizaciones interactivas
- Escribir tutoriales pedagógicos

#### Nivel Maestría:
- Validación parcial con datasets reducidos
- Análisis de sensibilidad paramétrica
- Comparación con modelos alternativos

#### Nivel Doctorado:
- Validación completa con datos cosmológicos
- Extensiones teóricas rigurosas
- Conexión con observables (CMB, LSS)

**Ventajas:**
- Proyecto abierto y bien documentado
- Libertad total para modificar
- Coautoría en publicaciones resultantes
- Sin restricciones de propiedad intelectual

---

### 🌍 Traductores

**Idiomas prioritarios:**
- Inglés ↔ Español (mejoras)
- Francés
- Alemán
- Portugués
- Mandarín

**Qué traducir:**
- README completo
- Documentación en `/docs/`
- Capítulos del paper (Markdown)

**Formato:**
- Mantener estructura de archivos
- Crear carpeta por idioma: `docs/fr/`, `paper/full-text/de/`
- Preservar ecuaciones LaTeX sin traducir

---

### 🎨 Artistas / Diseñadores

**Contribuciones creativas bienvenidas:**

1. **Visualizaciones científicas:**
   - Diagramas de atractores oscilatorios
   - Infografías explicativas
   - Animaciones de evolución cosmológica

2. **Diseño editorial:**
   - Portadas para PDFs
   - Plantillas LaTeX mejoradas
   - Iconografía para diferentes modelos

3. **Interpretaciones artísticas:**
   - "La sombra taquiónica" (Modelo Krein)
   - "Resonancia PT" (Modelo II)
   - "Memoria del fluido cósmico" (Modelo III)

**Licencia:** Todo bajo CC0 (o licencia compatible de tu elección)

---

## 🐛 Reportar Errores

### Errores en Código

Abre un [Issue](https://github.com/cisnerosmusic/Libro5-Del-Espacio-de-Hilbert-a-la-Cosmolog-a-Estoc-sticaix/issues/new) con:
```markdown
**Descripción del error:**
[Qué esperabas vs qué obtuviste]

**Pasos para reproducir:**
1. Ejecuté `python code/scripts/gen_fig1_fase.py`
2. Con parámetros: `--steps 100000 --tau 2.0`
3. Obtuve error: [copiar traceback]

**Entorno:**
- OS: Ubuntu 22.04
- Python: 3.9.7
- Dependencias: [output de `pip freeze`]

**Contexto adicional:**
[Screenshots, logs, etc.]
```

### Errores Matemáticos
```markdown
**Ubicación:**
[Capítulo/Sección/Ecuación]

**Error:**
[Descripción clara del problema]

**Corrección sugerida:**
[Si tienes una]

**Referencia:**
[Papers/libros que respaldan la corrección]
```

---

## 💬 Discusiones

Para temas que no son errores ni features:

- **Preguntas conceptuales:** [GitHub Discussions](https://github.com/cisnerosmusic/Libro5-Del-Espacio-de-Hilbert-a-la-Cosmolog-a-Estoc-sticaix/discussions)
- **Ideas para extensiones:** Discussions → Ideas
- **Mostrar tu trabajo:** Discussions → Show and Tell

---

## ⚖️ Código de Conducta

### Principios básicos:

1. **Honestidad intelectual:** 
   - Reconoce las limitaciones de tu trabajo
   - Cita fuentes apropiadamente
   - Admite errores abiertamente

2. **Colaboración constructiva:**
   - Crítica las ideas, no las personas
   - Ofrece alternativas cuando criticas
   - Celebra los aportes de otros

3. **Ciencia abierta:**
   - Comparte datos y código siempre que sea posible
   - No ocultes resultados negativos
   - Facilita la reproducibilidad

4. **Respeto:**
   - Valora contribuciones de todos los niveles
   - Sé paciente con principiantes
   - Reconoce expertise ajena

---

## 🏆 Reconocimiento

### Cómo se Otorga Crédito:

**Autoría en papers derivados:**
- Contribuciones científicas sustanciales → Coautoría
- Validación empírica completa → Primera autoría (si prefieres)
- Correcciones menores → Agradecimientos

**En el repositorio:**
- Contribuidores listados en README
- Commits individuales preservan autoría Git
- Issues/PRs quedan documentados públicamente

**En publicaciones:**
- Siguiendo estándares CRediT (Contributor Roles Taxonomy)
- Transparencia total sobre qué hizo cada persona

---

## 🚀 Proceso de Pull Request

### Para cambios de código:

1. **Fork** y clona el repositorio
2. **Crea rama** descriptiva: `git checkout -b fix/stability-issue`
3. **Haz cambios** con commits atómicos y descriptivos
4. **Prueba** localmente que todo funciona
5. **Push** y abre Pull Request
6. **Describe** claramente qué cambia y por qué
7. **Responde** a comentarios de revisión

### Qué incluir en el PR:

- [ ] Descripción clara del cambio
- [ ] Tests (si aplica)
- [ ] Documentación actualizada
- [ ] Changelog entry (para cambios mayores)

---

## 📧 Contacto Directo

**Para colaboraciones mayores:**
- Email: ernestocisnerosmusic@gmail.com
- Twitter/X: [@ernestcisneros1](https://twitter.com/ernestcisneros1)

**Tiempo de respuesta esperado:**
- Issues/PRs: 2-7 días
- Emails sobre colaboración: 1-2 semanas
- Preguntas simples: 1-3 días

---

## 🙏 Agradecimiento

Este proyecto existe porque creo que:
- Las ideas deben circular libremente
- La ciencia avanza con colaboración honesta
- Los errores transparentes son mejores que los aciertos ocultos

**Gracias por considerar contribuir.**

Si este trabajo te inspira, te frustra, o simplemente te hace pensar diferente, ya cumplió parte de su propósito.

---

**Última actualización:** Octubre 2025  
**Mantenedor:** Ernesto Cisneros Cino  
**Licencia:** CC0 1.0 — Todas las contribuciones entran al dominio público

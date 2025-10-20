name: Validación o colaboración científica
description: Propuesta para validar, refutar o expandir los modelos del proyecto
title: "[Validación] Breve descripción de tu propuesta"
labels: ["validation", "collaboration", "scientific"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Gracias por tu interés en colaborar. Por favor completa los siguientes campos:

  - type: input
    id: name
    attributes:
      label: Tu nombre o alias
      placeholder: Ej. Dra. López, usuario123

  - type: textarea
    id: proposal
    attributes:
      label: ¿Qué aspecto del modelo deseas validar o expandir?
      description: Puedes referirte a un notebook, sección del paper, o idea conceptual.

  - type: textarea
    id: method
    attributes:
      label: ¿Qué método propones?
      description: Ej. simulación, análisis estadístico, comparación con datos cosmológicos, etc.

  - type: dropdown
    id: tools
    attributes:
      label: ¿Qué herramientas usarás?
      multiple: true
      options:
        - Python
        - Mathematica
        - CosmoMC
        - CAMB
        - Otro

  - type: textarea
    id: notes
    attributes:
      label: Comentarios adicionales

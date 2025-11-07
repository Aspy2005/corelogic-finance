# CoreLogic Finance 🛠️

CoreLogic Finance es una librería modular y altamente confiable para cálculos financieros y de negocios en Python. Su diseño se basa estrictamente en la **Programación Orientada a Objetos (POO)** y el **Desarrollo Guiado por Pruebas (TDD)**, garantizando precisión matemática y robustez ante errores.

## 🎯 Enfoque Arquitectónico

* **Confiabilidad por TDD:** Todos los módulos tienen una cobertura de pruebas superior al 95%, incluyendo validación de **Casos Límite** (ej. balance cero, flujos vacíos).
* **Encapsulación:** Utiliza atributos privados (`__nombre`) para proteger el estado interno de los cálculos, forzando la interacción a través de interfaces públicas.
* **Excepciones Personalizadas:** Manejo de errores específicos del dominio de negocio (ej. `TasaInvalidaError`, `FrecuenciaInvalidaError`).

## ⚙️ Instalación

La librería está disponible en PyPI:

```bash
pip install corelogic-finance
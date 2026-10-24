# 🤖 ml-lab — Aprendiendo IA/ML con Python desde cero

---

## Cómo usar este repo

- **`apuntes/`** → la teoría, numerada y en orden. Empieza por el 01.
- **`labs/`** → un ejercicio práctico por sesión, cada uno con su carpeta, sus datos de
  ejemplo y su README (objetivo, pasos, resultado y errores).

Cada lab es reproducible: clona, crea el entorno, y sigue su README.

---

## Ruta de aprendizaje

El objetivo no es ser científico de datos, sino **saber llevar un modelo a producción**: entrenarlo con datos en condiciones, servirlo en una API y mantenerlo vivo. La ruta va de los datos al despliegue.

| # | Tema | De qué va | Estado |
|---|---|---|---|
| 1 | Fundamentos de pandas | Cargar, filtrar, ordenar y agrupar: los datos como una tabla | ✅ Hecho |
| 2 | Limpieza de datos | Nulos y tipos: dejar los datos listos antes de que lleguen a un modelo | ✅ Hecho |
| 3 | Visualización (matplotlib) | Ver los datos antes de modelar: distribuciones, relaciones, valores raros | ✅ Hecho |
| 4 | Primer modelo (scikit-learn) | Entrenar, evaluar con datos que el modelo no ha visto y guardarlo | 🟢 En curso — entrenado y evaluado; falta guardarlo |
| 5 | Servir el modelo | Envolverlo en una API (`POST /predict` con FastAPI) y empaquetarlo en un contenedor | 🔜 Pendiente |
| 6 | MLOps | Registrar experimentos y modelos (MLflow), reentrenar y desplegar con un pipeline, vigilar la deriva | 🔜 Pendiente |
| 7 | Azure Machine Learning | Lo mismo, sobre la plataforma gestionada de la nube | 🔜 Pendiente |
| 8 | Proyecto final | Un modelo útil de verdad —detectar certificados anómalos— en producción junto a una aplicación real | 🔜 Pendiente |

---

## Índice

### Apuntes

| # | Apunte | De qué va |
|---|---|---|
| 01 | [Fundamentos de pandas](apuntes/01-pandas-fundamentos.md) | Los datos como una tabla; diccionario SQL → pandas |
| 02 | [Limpieza de datos](apuntes/02-limpieza-datos.md) | Nulos, tipos y duplicados; las decisiones de limpieza del Titanic |
| 03 | [Visualización con matplotlib](apuntes/03-visualizacion.md) | Figure y Axes, la interfaz explícita y qué gráfico contesta a qué pregunta |
| 04 | [El primer modelo](apuntes/04-primer-modelo.md) | fit/predict, train/test split, la línea base, por qué la accuracy engaña y la fuga de datos |

### Labs

| # | Lab | Qué se practica | Estado |
|---|---|---|---|
| 01 | [Primer vistazo a pandas](labs/01-primer-vistazo-pandas/) | Cargar un CSV y hacer head/filter/sort/groupby | ✅ Hecho |
| 02 | [Limpieza del Titanic](labs/02-limpieza-datos/) | Decidir los nulos uno por uno y arreglar tipos | ✅ Hecho |
| 03 | [Visualización](labs/03-visualizacion/) | Tres gráficos del Titanic limpio, guardados como PNG | ✅ Hecho |
| 04 | [Primer modelo](labs/04-primer-modelo/) | Regresión logística contra una línea base: 0,798 frente a 0,618 | ✅ Hecho |

---

## Entorno

- Python 3 en un entorno virtual (`.venv`, ver README de cada lab).
- Dependencias en `requirements.txt`: pandas, matplotlib y scikit-learn.
- Por ahora, scripts `.py`. Cuando lleguemos a la fase de proyecto, se valorará pasar a
  Jupyter para la parte de exploración y gráficas.

---

## Otros repos de esta serie

Este repo es uno de tres, montados con la misma estructura de "asignatura":

| Repo | De qué va |
|---|---|
| [`cloud-devops-lab`](https://github.com/Manueh9/cloud-devops-lab) | Docker, Kubernetes, Terraform, CI/CD, Azure, observabilidad |
| [`security-lab`](https://github.com/Manueh9/security-lab) | Seguridad web: PortSwigger Web Security Academy y OWASP Juice Shop |
| [`ml-lab`](https://github.com/Manueh9/ml-lab) | Este: IA/ML con Python: datos, modelos y llevarlos a producción |

---

## Licencia

[MIT](LICENSE)
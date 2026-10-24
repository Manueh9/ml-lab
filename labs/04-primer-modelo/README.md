# Lab 04 · Primer modelo con scikit-learn

> Anterior: [lab 03 · Visualización](../03-visualizacion/)
> Teoría: [apuntes/04-primer-modelo.md](../../apuntes/04-primer-modelo.md)

## Objetivo

Entrenar un clasificador sobre el Titanic limpio y, sobre todo, **ponerlo al lado de una línea base
tonta** para saber si de verdad aporta algo. El entregable no es "un modelo": es la comparación y
la frase que la interpreta.

## Cómo se ejecuta

```bash
source ../../.venv/bin/activate
python3 modelo.py
```

Necesita `titanic_limpio.csv` (el resultado del lab 02, con las columnas del Titanic de seaborn:
`survived`, `pclass`, `sex`, `age`, `fare`…) en la misma carpeta. Probado con scikit-learn 1.9.1.

## Lo que hace el script

1. **X e y.** `y` es `survived` (0/1). `X` son cuatro columnas: `pclass`, `sex` pasada a número,
   `age` y `fare`.
2. **Train/test.** 80 % para entrenar y 20 % para examinar, con `random_state=42` para que el corte
   sea siempre el mismo y `stratify=y` para que las dos partes tengan la misma proporción de
   supervivientes.
3. **La línea base primero.** Un `DummyClassifier` que predice siempre la clase mayoritaria.
4. **El modelo.** Una regresión logística.
5. **La comparación** y el `classification_report`.

## Resultado real

```
Reparto de y (lo que tiene que batir el tonto):
survived
0    0.618
1    0.382
Name: proportion, dtype: float64

Entreno con 711 filas y examino con 178

Linea base:  0.618
Mi modelo:   0.798
Aporta:      +0.180

               precision    recall  f1-score   support

No sobrevivio       0.82      0.85      0.84       110
   Sobrevivio       0.75      0.71      0.73        68

     accuracy                           0.80       178
    macro avg       0.79      0.78      0.78       178
 weighted avg       0.80      0.80      0.80       178
```

## Qué veo

- **La clase mayoritaria era "no sobrevivió", con un 61,8 %.** Esa es la nota del tonto: predecir
  "muere" para todo el mundo ya acierta el 61,8 %. Y es exactamente la accuracy que sacó.
- **Mi modelo saca un 79,8 %, es decir, aporta 18 puntos sobre el tonto.** Con solo cuatro columnas
  ha aprendido algo de verdad. Si hubiera sacado un 62 %, "suena decente" pero no habría aportado
  nada.
- **El recall de "Sobrevivió" es 0,71**: de los 68 supervivientes reales del examen, el modelo
  encontró a 7 de cada 10, unos 48. Se le escapan unos 20.
- **Acierta más con la clase mayoritaria** (recall de 0,85 en "No sobrevivió") que con la
  minoritaria. Es lo normal: tiene más ejemplos de esa clase para aprender. Y es la razón por la
  que una accuracy sola no basta: el 0,80 global esconde que con los supervivientes va peor.
- **La precision de "Sobrevivió" es 0,75**: cuando dice "este sobrevive", acierta 3 de cada 4.

## Lo que aprendí

- **`fit` / `predict`**: todos los modelos de scikit-learn se usan igual. Cambiar de modelo es
  cambiar una línea, la del constructor.
- **Train/test split**: a un modelo no se le examina con los datos que ya vio. `random_state` hace
  el experimento reproducible; `stratify=y` mantiene la proporción de clases.
- **La línea base**: una accuracy sola no dice nada. Solo significa algo comparada con "predecir
  siempre la clase mayoritaria".
- **La accuracy no basta**: el recall por clase enseña dónde falla el modelo, y en datos
  desequilibrados suele fallar en la clase pequeña, que muchas veces es la que importa.
- **Fuga de datos**: el CSV trae una columna `alive` que dice lo mismo que `survived`. Si se mete en
  `X`, el modelo saca casi un 100 % sin haber aprendido nada: copia la respuesta. Hay que mirar qué
  columnas se le dan antes de entrenar.

## Errores con los que me topé

- **`ModuleNotFoundError: No module named 'sklearn'`.** scikit-learn no estaba en el entorno
  virtual. Se instala con `python3 -m pip install scikit-learn`; el paquete se llama
  `scikit-learn` pero se importa como `sklearn`.
- **`FileNotFoundError: 'titanic-limpio.csv'`.** Mi CSV se llama `titanic_limpio.csv`, con guion
  bajo. Un carácter.
- **`KeyError: 'Survived'`.** El script estaba escrito para el Titanic de Kaggle (columnas con
  mayúscula) y mi CSV viene del de seaborn (columnas en minúscula). Se ve con
  `pd.read_csv(...).columns.tolist()` y se adapta el script a los datos, no al revés.

## Qué queda pendiente a propósito

- **Guardar el modelo entrenado** con `joblib`: es el primer paso para servirlo en una API con
  FastAPI (`POST /predict`).
- **Más columnas y codificar categorías** (`embarked`, `who`…): es ingeniería de características,
  un tema propio.
- **Ajuste de hiperparámetros y validación cruzada**: optimización. No hasta dominar lo básico.
- **La matriz de confusión dibujada**: la foto de aciertos y errores por clase, buen puente con el
  lab de visualización.
# 04 · El primer modelo: scikit-learn y la línea base

> Anterior: [03 · Visualización](03-visualizacion.md) · Siguiente: *(pendiente)*
> Lab que lo acompaña: [labs/04-primer-modelo](../labs/04-primer-modelo/)

Limpiar y mirar los datos eran los pasos de antes. Este es entrenar. Pero el objetivo, para un
perfil que va a MLOps, no es el modelo: es aprender a **medirlo con honestidad**, que es lo que
luego se vigila en producción.

## 1. fit / predict

Todos los modelos de scikit-learn comparten dos métodos: `fit(X, y)` aprende y `predict(X)`
predice. `X` son las columnas de entrada (una tabla) e `y` la columna a predecir (un vector).
Cambiar de modelo es cambiar el constructor; el resto del código no se toca.

> **Analogía (C#).** `fit`/`predict` es una interfaz que implementan todos los modelos. Se programa
> contra la interfaz, no contra la implementación: puro polimorfismo.

## 2. Train/test split

A un modelo no se le mide con los datos con los que se entrenó: se mediría su memoria. Se parte el
dataset con `train_test_split`, que según la documentación *"split[s] arrays or matrices into
random train and test subsets"*.

- `test_size=0.2`: el 20 % se reserva para examinar.
- `random_state=42`: fija el azar. *"Pass an int for reproducible output across multiple function
  calls."* Sin esto, cada ejecución da una cifra distinta y no se puede saber si un cambio mejoró el
  modelo o tuvo suerte. Reproducibilidad es MLOps.
- `stratify=y`: mantiene la proporción de clases en las dos partes. Importa cuando las clases están
  desequilibradas, como el 38 % de supervivientes del Titanic.

> **Analogía (C#).** Examinar con los datos de entrenamiento es validar el código con los mismos
> casos con los que lo escribiste: pasa todo y no has comprobado nada. El test es el test de
> integración con datos que el modelo no ha tocado, y `random_state` es la semilla fija que evita
> que el test sea *flaky*.

## 3. La línea base, y por qué la accuracy engaña

`DummyClassifier(strategy="most_frequent")` predice siempre la clase mayoritaria, sin mirar nada.
Es *"a simple baseline to compare against other more complex classifiers"*. Si un modelo no
supera a ese tonto, no ha aprendido nada, por alta que suene su accuracy.

Regla: **nunca una accuracy sola; siempre al lado de la de la línea base.**

Además de la accuracy, el `classification_report` da cuatro números por clase:

| Métrica | Qué contesta |
|---|---|
| **precision** | de lo que predije como esa clase, cuánto lo era |
| **recall** | de lo que era esa clase de verdad, cuánto encontré |
| **f1-score** | el equilibrio entre las dos (su media armónica) |
| **support** | cuántos casos reales de esa clase había |

En datos desequilibrados (fraude, anomalías), el **recall de la clase minoritaria** es el que
desenmascara un modelo que la accuracy aplaude. Es la métrica que importará en la detección de
certificados anómalos del proyecto final.

## 4. Fuga de datos (*data leakage*)

Si entre las columnas de entrada se cuela una que **ya contiene la respuesta**, el modelo saca una
nota casi perfecta sin haber aprendido nada. En el Titanic de seaborn, la columna `alive` dice lo
mismo que `survived` (`yes`/`no` frente a `1`/`0`). Meterla en `X` es darle al modelo las
soluciones del examen.

Antes de entrenar hay que preguntarse de cada columna: **¿la tendría disponible en el momento de
predecir?** Si la respuesta es no, fuera.

## 5. Mis cifras de este lab

| Dato | Valor |
|---|---|
| Filas del dataset | 889 (711 para entrenar, 178 para examinar) |
| Clase mayoritaria (la nota del tonto) | "No sobrevivió", 61,8 % |
| Accuracy de la línea base | 0,618 |
| Accuracy de mi modelo (regresión logística) | 0,798 |
| Lo que aporta | +0,180 |
| Recall de "Sobrevivió" | 0,71 |
| Recall de "No sobrevivió" | 0,85 |

## 6. Lo que costó

Lo que más tiempo llevó no fue el modelo, sino que el script encajara con mis datos: el nombre del
CSV y las columnas en minúscula. Entrenar fueron cuatro líneas.

## 7. Dónde enlaza con el resto

- Con **servir el modelo**: este es el modelo que irá dentro de un `POST /predict` con FastAPI.
  Guardarlo con `joblib` es el siguiente paso.
- Con **MLOps**: se registrará en MLflow y lo vigilará su métrica. Si en producción cae hasta el
  nivel de la línea base, hay que reentrenar.
- Con **el proyecto final**: detectar certificados anómalos es un problema de clasificación
  desequilibrado, donde el recall manda sobre la accuracy.
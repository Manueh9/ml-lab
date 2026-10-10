# Lab 02 · Limpieza de datos (Titanic)

> Anterior: [lab 01 · Primer vistazo a pandas](../01-primer-vistazo-pandas/)
> Teoría: [apuntes/02-limpieza-datos.md](../../apuntes/02-limpieza-datos.md)

## Objetivo

Contar los nulos de un dataset real, decidir de forma justificada qué hacer con cada columna
problemática (tirar filas, tirar columna o imputar), entender `to_numeric`, y guardar el dataset
limpio.

## Preparación

```bash
cd ../..                       # raiz del repo
source .venv/bin/activate
curl -sSL -o titanic.csv https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv
python3 labs/02-limpieza-datos/limpiar.py
```

## Scripts

- `explorar.py` — mira la forma, los tipos y los nulos, sin tocar nada.
- `experimento_tipos.py` — demuestra qué hace `to_numeric(errors="coerce")` con texto no numérico.
- `limpiar.py` — aplica las tres decisiones y guarda `titanic_limpio.csv`.

## Decisiones tomadas

| Columna | Nulos (nº / %) | Acción | Justificación |
|---|---|---|---|
| `deck` | 688 / 77.2 | Tirar columna | Casi vacía; imputar sería inventar el 77% |
| `age` | 177 / 19.9 | Imputar (mediana = 28.0) | Demasiadas filas para tirarlas; edad útil |
| `embarked` | 2 / 0.2 | Tirar filas | Solo 2 de 891 |
| `embark_town` | 2 / 0.2 | Se arregla con lo anterior | Misma info que `embarked` |

## Resultado real

```
$ python3 experimento_tipos.py
0    22.0
1    30.0
2     NaN     <- "desconocido" no rompe: se marca NaN
3    45.0
dtype: float64

$ python3 limpiar.py
Antes: (891, 15)
Mediana de age usada para imputar: 28.0
Despues: (889, 14)
Nulos que quedan:
ninguno
Guardado titanic_limpio.csv
```

## Qué queda pendiente a propósito

- **Visualizar** los datos limpios (histogramas, barras) con matplotlib: es la sesión siguiente.
- **Codificar** las columnas de texto a números (lo que un modelo necesita): llega con el primer modelo.
- **Imputar `age` por grupo** (mediana por clase o sexo) en vez de la global: afinado para más adelante.
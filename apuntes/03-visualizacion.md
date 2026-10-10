# 03 · Visualización con matplotlib

> Anterior: [02 · Limpieza de datos](02-limpieza-datos.md) · Siguiente: *(pendiente)*
> Lab que lo acompaña: [labs/03-visualizacion](../labs/03-visualizacion/)

Mirar los datos es el paso entre limpiarlos y modelarlos, y el que más errores evita: un gráfico de
treinta segundos enseña cosas que una tabla de estadísticos esconde — un pico artificial creado al
rellenar nulos, una categoría que domina, dos valores extremos que torcerían un modelo entero.

## 1. Figure y Axes

La **Figure** es el lienzo completo (lo que se guarda en el PNG). Cada **Axes** es un gráfico dentro,
con sus ejes, su título y sus datos. **`Axes` no significa "los ejes"**: es el área de dibujo
entera; los ejes son `Axis`.

> **Analogía (C#/WinForms).** La `Figure` es el Form y cada `Axes` es un control colocado dentro.

## 2. Las dos interfaces, y por qué la explícita

```python
fig, ax = plt.subplots()     # explícita (orientada a objetos) — la que se usa
ax.hist(datos)
fig.savefig("a.png")
```

> **Analogía (C#).** La interfaz implícita (`plt.hist`, `plt.title`) es una clase estática con
> estado global mutable: actúa sobre "el gráfico actual", que vive en una variable que no ves. La
> explícita es tener la referencia al objeto.

## 3. Qué gráfico para qué pregunta

| Pregunta | Gráfico | Método |
|---|---|---|
| ¿Cómo se reparte una columna numérica? | Histograma | `ax.hist()` |
| ¿Cómo se comparan unas categorías? | Barras | `ax.bar()` |
| ¿Hay relación entre dos columnas numéricas? | Dispersión | `ax.scatter()` |

## 4. Cuatro detalles que no son cosmética

| Detalle | Por qué |
|---|---|
| `matplotlib.use("Agg")` antes de pyplot | Dibuja a fichero sin ventana. Sin esto, el mismo script falla en un contenedor o en CI |
| `fig.savefig()` en vez de `plt.show()` | El entregable es el fichero |
| `set_ylim(0, 1)` en una proporción | Sin él, una diferencia pequeña parece enorme |
| `alpha` en una dispersión | Deja ver la densidad cuando hay puntos superpuestos |

## 5. El truco del 0 y el 1

La media de una columna binaria es la proporción. `df.groupby("pclass")["survived"].mean()` devuelve
la tasa de supervivencia de cada clase directamente.

## 6. Mirar antes de confiar en el esquema

Un CSV no siempre tiene las columnas que esperas. El dataset de seaborn usa minúsculas (`age`,
`pclass`) y el de Kaggle mayúsculas (`Age`, `Pclass`). Asumir el nombre equivocado da un `KeyError`.
Se mira primero:

```python
print(list(pd.read_csv("datos.csv").columns))
```

## 7. El entorno es parte del código

Las librerías viven en un entorno virtual (`.venv`), no en el sistema. Si no está activado,
`import pandas` falla aunque pandas "esté instalado". Y cada librería nueva se captura en
`requirements.txt` con `pip freeze`, para que el proyecto sea reproducible en otra máquina o en un
pipeline. Es el mismo principio de reproducibilidad que un contenedor, una capa más abajo.
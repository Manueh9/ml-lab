# 01 · Fundamentos de pandas: los datos como una tabla

> El primer ladrillo del track de IA/ML. Antes de tocar ningún modelo hay que saber
> **cargar, mirar y manipular datos**. La herramienta para eso en Python es **pandas**, y
> la buena noticia viniendo de SQL/.NET es que ya piensas en tablas: aquí solo cambia la
> sintaxis.

---

## 1. Por qué pandas antes que los modelos

En machine learning, el 80% del trabajo real no es el modelo: es preparar los datos —
cargarlos, limpiarlos, entenderlos, transformarlos. Esa parte se hace casi siempre con
**pandas**. Si esto no lo dominas, lo demás no se sostiene. Por eso el track empieza aquí y
no en las redes neuronales.

> pandas se apoya por debajo en **numpy** (cálculo numérico con arrays). No hace falta
> dominar numpy primero: lo iremos viendo cuando asome. Hoy, todo pandas.

---

## 2. Los dos objetos de pandas

### Series — una columna
Una **Series** es una única columna de datos con un índice (una etiqueta por fila).
Piensa en ella como un array con nombre.

### DataFrame — una tabla entera
Un **DataFrame** es el objeto estrella: una **tabla** con filas y columnas, donde cada
columna es una Series. Tiene tipos por columna, un índice de filas y nombres de columna.

> 🗂️ **Analogía directa con lo que ya sabes:**
> un DataFrame **es** una tabla SQL, o un `DataTable` de .NET, cargada en memoria.
> - Una **fila** = un registro.
> - Una **columna** = un campo.
> - El **índice** = algo parecido a la clave/posición de cada fila.
>
> Casi todo lo que sabes hacer con SQL sobre una tabla, pandas lo hace sobre un DataFrame.
> Solo cambia cómo se escribe.

---

## 3. El diccionario SQL → pandas

Esta tabla es la que de verdad te va a servir. Tenla a mano mientras practicas.

| Quiero… | En SQL | En pandas |
|---|---|---|
| Ver la tabla | `SELECT * FROM t` | `df` |
| Ver las primeras filas | `SELECT TOP 5 * FROM t` | `df.head()` |
| Elegir columnas | `SELECT nombre, salario FROM t` | `df[["nombre", "salario"]]` |
| Filtrar filas | `WHERE salario > 50000` | `df[df["salario"] > 50000]` |
| Filtro con dos condiciones | `WHERE dep='Backend' AND edad<35` | `df[(df["departamento"]=="Backend") & (df["edad"]<35)]` |
| Ordenar | `ORDER BY salario DESC` | `df.sort_values("salario", ascending=False)` |
| Agrupar y agregar | `SELECT dep, AVG(salario) ... GROUP BY dep` | `df.groupby("departamento")["salario"].mean()` |
| Contar por categoría | `SELECT ciudad, COUNT(*) ... GROUP BY ciudad` | `df["ciudad"].value_counts()` |
| Columna calculada | `salario / antiguedad AS ...` | `df["nueva"] = df["salario"] / df["antiguedad_anios"]` |

Dos cosas que chocan al principio viniendo de SQL:

1. **El filtrado por máscara booleana.** `df["salario"] > 50000` no devuelve filas: devuelve
   una columna de `True`/`False`, una por fila. Al meterla entre corchetes
   (`df[ ... ]`), pandas se queda solo con las filas onde el valor es `True`. Es raro la
   primera vez y natural a la décima.
2. **Los operadores son `&`, `|`, `~`** (no `and`, `or`, `not`), y **cada condición va entre
   paréntesis**. Si escribes `df[df["a"]>1 & df["b"]<2]` sin paréntesis, revienta.

---

## 4. Vectorización (por qué no hay bucles)

En .NET, para calcular algo por cada fila harías un `foreach`. En pandas **no**: operas
sobre la columna entera de golpe y pandas lo aplica fila a fila por debajo, en código
optimizado. A esto se le llama **operación vectorizada**.

```python
# Nada de bucles: una línea opera sobre las 18 filas a la vez
df["salario_por_anio"] = df["salario"] / df["antiguedad_anios"]
```

Es más corto, más rápido y más legible. Interiorizar "pienso en columnas, no en filas
una a una" es el cambio de chip de esta sesión.

---

## 5. Lo mínimo para arrancar un análisis

Cuando abras un dataset nuevo, estos cuatro comandos son el "hola, ¿qué eres?":

```python
df.head()       # ¿qué pinta tienen los datos?
df.shape        # ¿cuántas filas y columnas? -> (filas, columnas)
df.dtypes       # ¿de qué tipo es cada columna?
df.describe()   # media, min, max, cuartiles de las columnas numéricas
```

---

## 6. Recursos

- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) — la intro oficial, corta.
- [pandas: Comparación con SQL](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html) — hecha a medida para quien viene de SQL. i.

---

➡️ Lab de esta sesión: [labs/01-primer-vistazo-pandas](../labs/01-primer-vistazo-pandas/)

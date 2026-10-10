# 02 · Limpieza de datos: nulos y tipos

> Anterior: [01 · Fundamentos de pandas](01-pandas-fundamentos.md) · Siguiente: *(pendiente)*
> Lab que lo acompaña: [labs/02-limpieza-datos](../labs/02-limpieza-datos/)

Los datos del mundo real vienen sucios: huecos donde debería haber un valor, y columnas que son
texto cuando deberían ser números. Antes de entrenar cualquier modelo hay que arreglarlo, porque la
mayoría de algoritmos no toleran ni un solo hueco.

## 1. El valor nulo (`NaN`)

Una celda vacía es `NaN`: ausencia de dato. No es un `0` ni una cadena vacía, igual que el `null`
de C# o el `NULL` de SQL. Contagia: una operación que lo toque suele devolver `NaN`.

```python
df.isna().sum()          # cuántos nulos por columna
df.isna().mean() * 100   # qué porcentaje
```

> Analogía (C#): es `int?` (`Nullable<int>`). No vale `0`, vale "no hay valor".

## 2. Las tres decisiones ante un nulo

| Decisión | Cómo | Cuándo |
|---|---|---|
| Tirar la fila | `df.dropna(subset=["col"])` | Pocos nulos; no quieres inventar datos |
| Tirar la columna | `df.drop(columns=["col"])` | La columna está casi vacía y no aporta |
| Imputar | `df["col"].fillna(valor)` | Conservar filas con un relleno razonable |

Ninguna es gratis. Para imputar un número, la **mediana** aguanta mejor los extremos que la media.

## 3. Los tipos (`dtype`)

Un número que llega como texto no deja calcular. Se fuerza con:

```python
df["col"] = pd.to_numeric(df["col"], errors="coerce")
```

`errors="coerce"` convierte lo que puede y marca `NaN` lo que no, sin romper. Así un problema de
tipos se vuelve uno de nulos. **Pero no se transforma porque sí**: si los tipos ya están bien, se
dejan. Saber reconocerlo es parte del trabajo.

> Analogía (C#): es `int.TryParse` aplicado a la columna entera.

## 4. Mi limpieza del Titanic

Dataset de partida: **891 filas, 15 columnas**. Cuatro columnas con nulos:

| Columna | Nulos | % | Decisión | Por qué |
|---|---|---|---|---|
| `deck` | 688 | 77.2 | Tirar columna | 3 de cada 4 vacías: imputar sería inventar el 77% |
| `age` | 177 | 19.9 | Imputar (mediana = **28.0**) | Demasiadas para tirarlas; la edad es útil |
| `embarked` | 2 | 0.2 | Tirar filas | Solo 2 de 891 |
| `embark_town` | 2 | 0.2 | (se arregla sola) | Misma info que `embarked`, mismas 2 filas |

Forma del dataset: antes **(891, 15)**, después **(889, 14)**. Nulos restantes: **ninguno**.

Tipos: **no hubo que arreglar ninguno** — el dataset ya venía bien tipado (`age` y `fare` ya eran
`float`). Para ver qué hace `to_numeric`, probé aparte con `["22","30","desconocido","45"]`:
`"desconocido"` pasó a `NaN` y el resto a número, sin error.
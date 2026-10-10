import pandas as pd

df = pd.read_csv("titanic.csv")

print("Forma (filas, columnas):", df.shape)
print("\nTipos de cada columna:")
print(df.dtypes)
print("\nNulos por columna (solo las que tienen):")
print(df.isna().sum()[lambda s: s > 0])
print("\nPorcentaje de nulos (%):")
print((df.isna().mean() * 100).round(1)[lambda s: s > 0])
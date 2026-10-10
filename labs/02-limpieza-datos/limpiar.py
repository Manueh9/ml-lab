import pandas as pd

df = pd.read_csv("titanic.csv")
print("Antes:", df.shape)

# TIRAR COLUMNA: deck esta 77% vacia, no aporta
df = df.drop(columns=["deck"])

# IMPUTAR: age, ~20% nulos, columna util -> mediana (aguanta extremos mejor que la media)
mediana_edad = df["age"].median()
df["age"] = df["age"].fillna(mediana_edad)
print("Mediana de age usada para imputar:", mediana_edad)

# TIRAR FILAS: embarked (y su gemela embark_town) solo tienen 2 nulos
df = df.dropna(subset=["embarked"])

print("Despues:", df.shape)
print("Nulos que quedan:")
print(df.isna().sum()[lambda s: s > 0] if df.isna().sum().sum() else "ninguno")

df.to_csv("titanic_limpio.csv", index=False)
print("Guardado titanic_limpio.csv")
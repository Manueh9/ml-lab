"""Lab 03 - Visualizacion del Titanic limpio con matplotlib."""
import matplotlib
matplotlib.use("Agg")           # backend sin ventana: vale en un contenedor o CI
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("titanic_limpio.csv")
print(f"{len(df)} filas, {df.isna().sum().sum()} nulos")

# 1. HISTOGRAMA: como se reparte una columna numerica
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["age"], bins=20, edgecolor="white")
ax.set_title("Reparto de edades a bordo del Titanic")
ax.set_xlabel("Edad"); ax.set_ylabel("Numero de pasajeros")
fig.tight_layout(); fig.savefig("01-edades.png", dpi=120)

# 2. BARRAS: la media de una columna de 0 y 1 ES la proporcion
tasa = df.groupby("pclass")["survived"].mean()
print(tasa)
fig, ax = plt.subplots(figsize=(7, 5))
ax.bar(tasa.index.astype(str), tasa.values)
ax.set_title("Proporcion de supervivientes por clase")
ax.set_xlabel("Clase del billete"); ax.set_ylabel("Proporcion que sobrevive")
ax.set_ylim(0, 1)
fig.tight_layout(); fig.savefig("02-supervivencia-por-clase.png", dpi=120)

# 3. DISPERSION: alpha deja ver la densidad
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df["age"], df["fare"], s=12, alpha=0.5)
ax.set_title("Edad frente al precio del billete")
ax.set_xlabel("Edad"); ax.set_ylabel("Precio pagado")
fig.tight_layout(); fig.savefig("03-edad-vs-precio.png", dpi=120)

print(df.nlargest(5, "fare")[["pclass", "age", "fare", "survived"]])
print("Listo: 01-edades.png, 02-supervivencia-por-clase.png, 03-edad-vs-precio.png")

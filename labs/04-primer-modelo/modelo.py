"""
Lab 04 - Primer modelo supervisado sobre el Titanic limpio.

La gracia del lab no es el modelo: es compararlo SIEMPRE con una linea base tonta,
para no fiarse de una cifra de accuracy que suena bien y no significa nada.

Uso:  python3 modelo.py   (necesita titanic_limpio.csv en la misma carpeta)
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# --- 1. X e y ---
df = pd.read_csv("titanic_limpio.csv")
y = df["survived"]
df["sexo_num"] = (df["sex"] == "female").astype(int)  # un modelo no come texto

# OJO: la columna 'alive' dice lo mismo que 'survived' (yes/no). Si entrara en X,
# el modelo "acertaria" copiando la respuesta: eso es una fuga de datos (data leakage).
X = df[["pclass", "sexo_num", "age", "fare"]]

print("Reparto de y (lo que tiene que batir el tonto):")
print(y.value_counts(normalize=True).round(3), "\n")

# --- 2. train/test, reproducible y estratificado ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Entreno con {len(X_train)} filas y examino con {len(X_test)}\n")

# --- 3. LA LINEA BASE PRIMERO ---
tonto = DummyClassifier(strategy="most_frequent")
tonto.fit(X_train, y_train)
acc_tonto = accuracy_score(y_test, tonto.predict(X_test))

# --- 4. el modelo de verdad ---
modelo = LogisticRegression(max_iter=1000)
modelo.fit(X_train, y_train)
acc_modelo = accuracy_score(y_test, modelo.predict(X_test))

print(f"Linea base:  {acc_tonto:.3f}")
print(f"Mi modelo:   {acc_modelo:.3f}")
print(f"Aporta:      {acc_modelo - acc_tonto:+.3f}\n")

# --- 5. una metrica honesta ---
print(classification_report(
    y_test, modelo.predict(X_test),
    target_names=["No sobrevivio", "Sobrevivio"]
))
"""
Lab 01 · Primer vistazo a pandas
================================
Explora un CSV de empleados con pandas. Ejecuta el script entero con:

    python3 explorar.py

Está pensado para LEERLO de arriba abajo: cada bloque hace UNA cosa y explica
con qué instrucción SQL se parece, porque un DataFrame es básicamente una tabla.
Al final tienes una sección "TU TURNO" para que escribas tú.
"""

import pandas as pd

# ─────────────────────────────────────────────────────────────────────────────
# 1. CARGAR LOS DATOS  ·  equivale a:  SELECT * FROM empleados
# ─────────────────────────────────────────────────────────────────────────────
# read_csv lee el fichero y lo mete en un DataFrame (df): una tabla en memoria,
# con filas, columnas y sus tipos ya deducidos.
df = pd.read_csv("datos/empleados.csv")

print("== Las primeras filas (df.head) ==")
print(df.head())          # como SELECT TOP 5 * : un vistazo rápido
print()

# ─────────────────────────────────────────────────────────────────────────────
# 2. CONOCER LA TABLA  ·  como mirar el esquema + un COUNT(*)
# ─────────────────────────────────────────────────────────────────────────────
print("== Forma (filas, columnas) ==")
print(df.shape)           # (18, 6): 18 filas, 6 columnas
print()

print("== Tipos de cada columna (df.dtypes) ==")
print(df.dtypes)          # int64 para números, object para texto
print()

print("== Resumen estadístico de las columnas numéricas (df.describe) ==")
print(df.describe())      # media, min, max, cuartiles... de un vistazo
print()

# ─────────────────────────────────────────────────────────────────────────────
# 3. SELECCIONAR COLUMNAS  ·  SELECT nombre, salario FROM empleados
# ─────────────────────────────────────────────────────────────────────────────
print("== Solo nombre y salario ==")
print(df[["nombre", "salario"]].head())
print()

# ─────────────────────────────────────────────────────────────────────────────
# 4. FILTRAR FILAS  ·  WHERE salario > 50000
# ─────────────────────────────────────────────────────────────────────────────
# df["salario"] > 50000 produce una columna de True/False; al meterla entre
# corchetes, df te devuelve SOLO las filas donde es True. Esto es "boolean masking".
print("== Empleados que cobran más de 50.000 ==")
print(df[df["salario"] > 50000])
print()

# Varias condiciones: & es AND, | es OR. OJO: cada condición entre paréntesis.
print("== Backend Y menores de 35 (WHERE departamento='Backend' AND edad<35) ==")
print(df[(df["departamento"] == "Backend") & (df["edad"] < 35)])
print()

# ─────────────────────────────────────────────────────────────────────────────
# 5. ORDENAR  ·  ORDER BY salario DESC
# ─────────────────────────────────────────────────────────────────────────────
print("== Top 5 mejor pagados ==")
print(df.sort_values("salario", ascending=False).head())
print()

# ─────────────────────────────────────────────────────────────────────────────
# 6. AGRUPAR Y AGREGAR  ·  SELECT departamento, AVG(salario) ... GROUP BY departamento
# ─────────────────────────────────────────────────────────────────────────────
# Esta es la operación estrella de pandas y la que más se parece a SQL.
print("== Salario medio por departamento ==")
print(df.groupby("departamento")["salario"].mean().round(0))
print()

print("== Cuántos empleados hay por ciudad (como COUNT(*) ... GROUP BY ciudad) ==")
print(df["ciudad"].value_counts())
print()

# ─────────────────────────────────────────────────────────────────────────────
# 7. CREAR UNA COLUMNA NUEVA  ·  columna calculada
# ─────────────────────────────────────────────────────────────────────────────
# Añadimos el salario por año de antigüedad. pandas opera columna a columna
# (vectorizado): no hay que escribir un bucle.
df["salario_por_anio"] = (df["salario"] / df["antiguedad_anios"]).round(0)
print("== Con la columna nueva 'salario_por_anio' ==")
print(df[["nombre", "salario", "antiguedad_anios", "salario_por_anio"]].head())
print()


# ═════════════════════════════════════════════════════════════════════════════
# TU TURNO
# ═════════════════════════════════════════════════════════════════════════════
# Descomenta / escribe debajo. Intenta resolverlas TÚ antes de mirar la ayuda de
# los bloques de arriba. Pon el resultado en el README del lab.
# Escribe tus tres respuestas aquí:

# a) Muestra solo los empleados de Madrid.
# b) ¿Cuál es la EDAD media por departamento?
# c) Ordena la tabla por antigüedad de mayor a menor y enseña las 3 primeras filas.

# Lab 01 · Primer vistazo a pandas

**Objetivo:** cargar un CSV en un DataFrame y hacer las operaciones básicas —mirar,
filtrar, ordenar, agrupar— reconociendo en cada una su equivalente en SQL.

**Nivel:** primera vez con pandas. Requiere solo Python básico.

**Tiempo:** 60-90 min.

---

## Conceptos previos

Si no tienes claro qué es un DataFrame ni el diccionario SQL → pandas, lee primero
[apuntes/01 · Fundamentos de pandas](../../apuntes/01-pandas-fundamentos.md). Son 10 min y
todo el lab se apoya en eso.

---

## Ficheros

- `datos/empleados.csv` — 18 empleados con departamento, ciudad, edad, salario y
  antigüedad. Dataset pequeño y de juguete, a propósito.
- `explorar.py` — script comentado que recorre las operaciones básicas. Está para
  **leerlo de arriba abajo**, no solo ejecutarlo.

---

## Pasos

### 1. Preparar el entorno (una vez)

En la VM (Ubuntu Server), dentro de la carpeta del repo:

```bash
sudo apt update && sudo apt install -y python3-pip python3-venv
python3 -m venv .venv           # crea un entorno virtual aislado
source .venv/bin/activate       # actívalo (verás (.venv) en el prompt)
pip install pandas
```

> **¿Por qué un entorno virtual (venv)?** Ubuntu no deja instalar paquetes de Python
> "a lo bruto" en el sistema (te dará un error `externally-managed-environment`). El venv
> es una carpeta aislada con su propio Python y sus paquetes: instalas ahí sin tocar el
> sistema, y está en el `.gitignore` para no subirlo. Para volver a usarlo otro día:
> `source .venv/bin/activate`.

### 2. Ejecutar el script

```bash
cd labs/01-primer-vistazo-pandas
python3 explorar.py
```

Ve leyendo cada bloque del script a la vez que miras su salida. No corras a la siguiente
sección hasta entender qué hizo la anterior y con qué SQL se parece.

### 3. TU TURNO (el entregable)

Al final de `explorar.py` hay tres ejercicios. Resuélvelos tú, escribiendo el código:

- a) Solo los empleados de Madrid.
- b) La **edad** media por departamento.
- c) La tabla ordenada por antigüedad de mayor a menor, primeras 3 filas.

Pista: son variaciones de bloques que ya están resueltos más arriba en el script.

---

## Errores con los que me topé

*(Rellena mientras trabajas. Los típicos del primer día con pandas:)*

| Síntoma | Causa probable | Solución |
|---|---|---|
| `externally-managed-environment` al hacer pip | Ubuntu bloquea instalar en el Python del sistema | Usar un venv (paso 1) |
| `KeyError: 'columna'` | Nombre de columna mal escrito | Revisa `df.columns` |
| El filtro con `and` peta | Hay que usar `&` y paréntesis en cada condición | `df[(cond1) & (cond2)]` |

---

## Qué queda pendiente (para la próxima sesión de este track)

- Valores nulos y limpieza de datos (`isna`, `fillna`, `dropna`).
- Leer datos "sucios" de verdad, no un CSV de juguete.
- Primer contacto con una gráfica.

---

## Ejemplo resuelto

Intenta resolverlos tú en `explorar.py` antes de abrir esto.

<details>
<summary>a) Empleados de Madrid — ver solución</summary>

```python
print(df[df["ciudad"] == "Madrid"])
```

| nombre | departamento | ciudad | edad | salario | antiguedad_anios | salario_por_anio |
|---|---|---|---:|---:|---:|---:|
| Ana    | Backend  | Madrid | 34 | 42000 | 6  | 7000.0 |
| Carla  | Backend  | Madrid | 41 | 51000 | 12 | 4250.0 |
| Elena  | Frontend | Madrid | 37 | 45000 | 8  | 5625.0 |
| Gloria | Datos    | Madrid | 45 | 58000 | 15 | 3867.0 |
| Karla  | DevOps   | Madrid | 31 | 46000 | 5  | 9200.0 |
| Olga   | Datos    | Madrid | 50 | 65000 | 20 | 3250.0 |
| Ruben  | Frontend | Madrid | 42 | 50000 | 11 | 4545.0 |

</details>

<details>
<summary>b) Edad media por departamento — ver solución</summary>

```python
print(df.groupby("departamento")["edad"].mean().round(2))
```

| departamento | edad_media |
|---|---:|
| Backend  | 33.60 |
| Datos    | 39.25 |
| DevOps   | 35.00 |
| Frontend | 33.80 |

</details>

<details>
<summary>c) Top 3 con más antigüedad — ver solución</summary>

```python
print(df.sort_values("antiguedad_anios", ascending=False).head(3))
```

| nombre | departamento | ciudad   | edad | salario | antiguedad_anios | salario_por_anio |
|---|---|---|---:|---:|---:|---:|
| Olga   | Datos  | Madrid   | 50 | 65000 | 20 | 3250.0 |
| Gloria | Datos  | Madrid   | 45 | 58000 | 15 | 3867.0 |
| Luis   | DevOps | Valencia | 44 | 60000 | 14 | 4286.0 |

</details>



⬅️ [Volver al índice del repo](../../README.md)
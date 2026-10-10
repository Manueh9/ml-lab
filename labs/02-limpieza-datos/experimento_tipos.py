import pandas as pd

# Qué hace errors="coerce" con una columna de texto que trae un valor no numérico:
s = pd.Series(["22", "30", "desconocido", "45"])
print(pd.to_numeric(s, errors="coerce"))
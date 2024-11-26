import pandas as pd

archivo_csv = "C:/Users/bonil/OneDrive/Documentos/programacion 2/contactos.csv"
try:
    df = pd.read_csv(archivo_csv)
    print(df)
except pd.errors.EmptyDataError:
    print("El archivo está vacío o no tiene formato CSV correcto.")

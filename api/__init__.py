import pandas as pd

def cargar_datos(ruta_archivo):
    """
    Carga un archivo Excel en un DataFrame.
    
    Parámetros:
        ruta_archivo (str): Ruta del archivo Excel.
    
    Retorna:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    return pd.read_excel(ruta_archivo)

def filtrar_datos(df, condiciones):
    """
    Filtra el DataFrame según múltiples condiciones.
    
    Parámetros:
        df (pd.DataFrame): DataFrame original.
        condiciones (dict): Diccionario con pares {columna: valor}.
    
    Retorna:
        pd.DataFrame: DataFrame filtrado.
    
    Ejemplo:
        condiciones = {"Departamento": "Antioquia", "Municipio": "Medellín"}
        filtrar_datos(df, condiciones)
    """
    for columna, valor in condiciones.items():
        if columna in df.columns:
            df = df[df[columna] == valor]
        else:
            raise ValueError(f"La columna '{columna}' no existe en el DataFrame.")
    return df

def obtener_mediana_topografia(df, columna):
    """
    Obtiene la mediana de pH, Fósforo y Potasio agrupada por una columna.
    
    Parámetros:
        df (pd.DataFrame): DataFrame de entrada.
        columna (str): Columna para agrupar (ejemplo: 'Topografia').
    
    Retorna:
        pd.DataFrame: Mediana de las variables agrupadas.
    """
    variables = ["pH", "Fósforo", "Potasio"]
    faltantes = [v for v in variables if v not in df.columns]
    if faltantes:
        raise ValueError(f"Faltan columnas en los datos: {', '.join(faltantes)}")
    
    return df.groupby(columna)[variables].median()

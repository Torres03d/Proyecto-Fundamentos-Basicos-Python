from api import cargar_datos, filtrar_datos, obtener_mediana_topografia
from ui import pedir_parametros

def main():
    # Cargar Excel
    try:
        df = cargar_datos("resultado_laboratorio_suelo.xlsx")
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
        return

    # Pedir parámetros al usuario (se pasa df)
    departamento, municipio, cultivo, num_registros = pedir_parametros(df)

    # Filtrar usando condiciones
    condiciones = {
        "Departamento": departamento,
        "Municipio": municipio,
        "Cultivo": cultivo
    }
    df_filtrado = filtrar_datos(df, condiciones)

    if df_filtrado.empty:
        print("No se encontraron registros con los parámetros dados.")
        return

    # Limitar el número de registros
    df_filtrado = df_filtrado.head(num_registros)

    # Mostrar resultados
    print("\n=== Resultados filtrados ===")
    print(df_filtrado)

    # Mostrar mediana agrupada por Topografía
    print("\n=== Mediana de variables edáficas agrupada por Topografía ===")
    print(obtener_mediana_topografia(df_filtrado, "Topografia"))

if __name__ == "__main__":
    main()

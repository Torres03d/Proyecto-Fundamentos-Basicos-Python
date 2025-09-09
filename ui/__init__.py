def pedir_parametros(df):
    # === Departamento ===
    deps = sorted(df['Departamento'].dropna().unique())
    while True:
        print("Departamentos disponibles:", ", ".join(deps))
        depto = input("Ingrese Departamento: ").strip()
        if depto in deps:
            break
        print("⚠️ Departamento inválido. Intente de nuevo.\n")

    # === Municipio ===
    munis = sorted(df[df['Departamento'] == depto]['Municipio'].dropna().unique())
    while True:
        print(f"Municipios en {depto}: {', '.join(munis)}")
        muni = input("Ingrese Municipio: ").strip()
        if muni in munis:
            break
        print("⚠️ Municipio inválido. Intente de nuevo.\n")

    # === Cultivo ===
    cultivos = sorted(df[(df['Departamento'] == depto) & (df['Municipio'] == muni)]['Cultivo'].dropna().unique())
    while True:
        print(f"Cultivos en {muni}, {depto}: {', '.join(cultivos)}")
        cultivo = input("Ingrese Cultivo: ").strip()
        if cultivo in cultivos:
            break
        print("⚠️ Cultivo inválido. Intente de nuevo.\n")

    # === Número de registros ===
    while True:
        n = input("Ingrese número de registros a mostrar: ").strip()
        if n.isdigit() and int(n) > 0:
            n = int(n)
            break
        print("⚠️ Número inválido. Debe ser un entero positivo.\n")

    return depto, muni, cultivo, n

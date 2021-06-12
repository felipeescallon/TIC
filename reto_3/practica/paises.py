# Determine el pais con mas poblacion, y mostrarlo por pantalla con los datos correspondientes

def pais_mayor(datos):
    """Funcion que permite saber el pais con mayor poblacion, y lo retorna
    en una lista, en formato [pais, poblacion]

    Args:
        datos (dict): Diccionario de datos que representa los paises y su poblacion

    Returns:
        (list) : Lista de datos final, que corresponde al pais con mayor poblacion [pais, poblacion]
    """
    # Variable auxiliar que representa los valores de [pais, poblacion]
    mayor = [0, 0]

    # Iteracion sobre el contenido del diccionario 'datos'
    for pais in datos:
        # Realiza la evaluacion de valores con la variable auxiliar 'mayor'
        if datos[pais] > mayor[1]:
            # Asignacion de los valores correspondientes a la variable auxiliar
            mayor = [pais, paises[pais]]

    return mayor

# Lista de paises que representa los datos a evaluar
paises = {
    "Colombia" : 50_000_000,
    "Brazil" : 211_000_000,
    "Venezuela" : 28.52_000_000,
    "Ecuador" : 17_000_000,
    "Chile" : 18.9_000_000,
    "Bolivia" : 11.51_000_000,
    "Paraguay" : 7.45_000_000,
    "Uruguay" : 3.462_000_000,
    "Peru" : 32.51_000_000,
    "Mexico" : 127.6_000_000
}

resultado = pais_mayor(datos=paises)

print(f"El pais con mayor poblacion es {resultado[0]}, con una poblacion de {resultado[1]}")

print(help(pais_mayor))


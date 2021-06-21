from math import *

datos_dict = {
    #           lati    longi   prom
    "Trabajo": [6.124, -75.946, 1035],
    "Casa": [6.125, -75.966, 109],
    "Parque": [6.135, -75.976, 31],
    # "Ubicacion4": [6.144, -75.936, 151]
}

# Datos de la ubicaciones del usuario
ubicaciones = {
    #              lati    longi   prom
    "Ubicacion1": [6.124, -75.946, 1035],
    "Ubicacion2": [6.125, -75.966, 109],
    "Ubicacion3": [6.135, -75.976, 31],
    "Ubicacion4": [6.144, -75.936, 151]
}

ubicacion_actual = [
    [6.135, -75.976, 31],
    [6.125, -75.966, 109],
    [6.144, -75.936, 151],
    [6.124, -75.946, 1035]
]

def funcion(seleccion):

    def interna(dato):
        # el parametro 'dato' equivale al indice de posicion de la lista de ubicaciones
        # lugares = [elegido, comparado]
        radio = 6372.795477598  # Km (Radio de la tierra)

        lat1, long1 = datos_dict[seleccion][0], datos_dict[seleccion][1]
        lat2, long2 = ubicacion_actual[dato][0], ubicacion_actual[dato][1]

        latitud = lat2 - lat1
        longitud = long2 - long1

        distancia = (2 * radio * asin(sqrt((sin(latitud / 2) ** 2) + cos(lat1) * cos(lat2) * (sin(longitud / 2) ** 2))))
        distancia = round(distancia, 3)

        return distancia

    mayor = []

    for i in range(4):
        mayor.append(interna(i))

    return sorted(mayor)




print(funcion("Trabajo")[0])
print(funcion("Trabajo")[1])

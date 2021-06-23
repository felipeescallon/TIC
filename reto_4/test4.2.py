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


ubicacion_actual = [
    [6.135, -75.976, 31,2],
    [6.125, -75.966, 109, 3],
    [6.144, -75.936, 151, 6],
    [6.154, -75.946, 1035, 1]
]

# print(sorted(ubicacion_actual))
for i in sorted(ubicacion_actual):
    print(i)
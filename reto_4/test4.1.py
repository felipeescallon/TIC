from math import *

datos_dict = {
                #  lati    longi   prom
    "Trabajo": [6.124, -75.946, 1035],
    "Casa": [6.125, -75.966, 109],
    "Parque": [6.135, -75.976, 31],
    # "Ubicacion4": [6.144, -75.936, 151]
}


def lafuncion(lugares):
    # lista = [l1, l2, l3]
    #          T   C   P

    radio = 6372.795477598  # Km (Radio de la tierra)

    #   Trabajo             6.124                          -75.946
    lat1, long1 = datos_dict[lugares[0]][0], datos_dict[lugares[0]][1]
    #   Casa                6.125                          -75.966
    lat2, long2 = datos_dict[lugares[1]][0], datos_dict[lugares[1]][1]

    latitud = lat2 - lat1
    longitud = long2 - long1

    # Usando las funciones del modulo 'math' para calcular la distancia1 entre los puntos A y B
    distancia1 = (2 * radio * asin(sqrt((sin(latitud / 2) ** 2) + cos(lat1) * cos(lat2) * (sin(longitud / 2) ** 2))))
    distancia1 = round(distancia1, 3)

    print(f"la distancia es: {distancia1} metros")


    #   Trabajo             6.124                          -75.946
    lat1, long1 = datos_dict[lugares[0]][0], datos_dict[lugares[0]][1]
    #   Parque              6.135                          -75.976
    lat2, long2 = datos_dict[lugares[2]][0], datos_dict[lugares[2]][1]

    latitud = lat2 - lat1
    longitud = long2 - long1

    # Usando las funciones del modulo 'math' para calcular la distancia2 entre los puntos A y C
    distancia2 = (2 * radio * asin(sqrt((sin(latitud / 2) ** 2) + cos(lat1) * cos(lat2) * (sin(longitud / 2) ** 2))))
    distancia2 = round(distancia2, 3)

    print(f"la distancia es: {distancia2} metros")

# El lugar de 'Trabajo' es el elegido
lafuncion(lugares=["Parque", "Trabajo", "Casa"])


# "Trabajo", "Casa", "Parque" 126.016 metros - 201.515 metros
# "Casa", "Parque", "Trabajo" 89.599 metros - 126.016 metros
# "Parque", "Trabajo", "Casa" 201.515 metros - 89.599 metros
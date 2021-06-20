# Coordenadas de ubicacion del usuario, inicializadas en 0.0
dic_coords = {
    "Trabajo": [0.0, 0.0],
    "Casa": [0.0, 0.0],
    "Parque": [0.0, 0.0]
    #          lat  long
}



def restricciones(distancia, maximo, minimo):
    """Permite evaluar la validez de las coordenadas ingresadas y que cumplan con restricciones dadas

    Args:
        distancia (float): Valor equivalente a la coordenada que se quiere evaluar
        maximo (float): Valor maximo que puede alcanzar la coordenada ingresada
        minimo (float): Valor minimo que puede alcanzar la coordenada ingresada

    Returns:
        [bool]: Retorna 'True' en caso de que las restricciones se cumplan y sean validas
    """
    # if distancia >= maximo and distancia <= minimo:
    if maximo >= distancia >= minimo:
        return True

    else:
        print("\nError")
        exit()


def recorrer(opcion, cantidad=123):
    lista = [lugar for lugar in dic_coords]



seleccion = int(input("\nIngresa una opcion (1 - 3) \n>> ")) - 1
recorrer(opcion=seleccion)

# def crear_coordenadas():
#     """Permite crear y definir los diferentes valores de coordenadas correspondientes al usuario"""
#     # Inicializacion de las variables para acumular el promedio de coordenadas
#     lati_avg = 0
#     long_avg = 0

#     # Se itera sobre el contenido del diccionario 'dic_coords' que equivale a las coordenadas del usuario
#     for lugar in dic_coords:
#         # Se obtienen las coordenadas de la latitud [0] y se redondean a 3 valores decimales
#         dic_coords[lugar][0] = round(float(input(f"\nIngresa el valor decimal para latitud del {lugar} \n>> ")), 3)

#         # if 6.284 >= dic_coords[lugar][0] >= 6.077:   # 6.215
#         if restricciones(distancia=dic_coords[lugar][0], maximo=6.284, minimo=6.077):
#             # Se obtienen las coordenadas de la longitud [1] y se redondean a 3 valores decimales
#             dic_coords[lugar][1] = round(float(input(f"\nIngresa el valor decimal para longitud del {lugar} \n>> ")), 3)

#             # if -75.841 >= dic_coords[lugar][1] >= -76.049:   # -75.984
#             if restricciones(distancia=dic_coords[lugar][1], maximo=-75.841, minimo=-76.077):
#                 # Acumulacion de coordenadas para generar un promedio estimado
#                 lati_avg += dic_coords[lugar][0]
#                 long_avg += dic_coords[lugar][1]
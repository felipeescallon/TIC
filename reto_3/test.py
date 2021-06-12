# Ejemplo de una matriz de 3x2 (3 filas y 2 columnas)
coordenadas = [
    # TRABAJO
    [['1a'], ['1b']],
    # CASA
    [['2a'], ['2b']],
    # PARQUE
    [['3a'], ['3b']]
    # lati   long
]

# for i in coordenadas:
#     print(i[1])

# print(coordenadas[0][0])

dic_coords = {
    "Trabajo": [1, 2],
    "Casa": [1, 2],
    "Parque": [1, 2]
}


# def restricciones(latitud, longitud):
#     # if latitud >= 6.284 and latitud <= 6.077:
#     if 6.284 >= latitud >= 6.077:  # 6.215
#         if -75.841 >= longitud >= -76.049:  # -75.984
#             return True
#         else:
#             print("\nError coordenada")
#             exit()
#     else:
#         print("\nError coordenada")
#         exit()

# Taking multiples inputs in a single line
# a, b = input("ingresa dos valores: \n>> ").split()
#
# print(a)
# print(b)

# suma = [coord for coord in coordenadas[0]]
suma = 0
for lugar in dic_coords:
    print(dic_coords[lugar])
suma += dic_coords[lugar][1]

print(suma)


print(round(6.2543, 3))
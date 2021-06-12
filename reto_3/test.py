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
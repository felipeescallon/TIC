def carga_paises():
    mayor = 0
    pmayorp = ""  # pais mayor poblacion
    i=0
    paises={}
    while i < 10:
        nom_pais=input(f"Nombre del pais {i+1}: ")
        pob_pais=int(input(f"poblacion del pais {i+1}:"))
        paises[nom_pais]=pob_pais
        i=i+1
        for nombre in paises:
            if paises[nombre]>mayor:  # El valor de cada producto: productos[nombre]
                mayor = paises[nombre]
                pmayorp = nombre

    print("El pais con mayor poblacion es: ",pmayorp)

    return paises


def imprimir_paises(paises):
    print("======== listado de paises =======")
    for nom_pais in paises:
        print (f"pais {nom_pais} : {paises[nom_pais]}")

# prog ppal
paises=carga_paises()
imprimir_paises(paises)
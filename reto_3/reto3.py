"""Reto #3"""
import random

# Credenciales del sistema
g_username = "51612"
# 'username' reversed
g_password = g_username[::-1]

# Coordenadas de ubicacion del usuario, inicializadas en 0.0
coordenadas = [
    # TRABAJO
    [0.0, 0.0],
    # CASA
    [0.0, 0.0],
    # PARQUE
    [0.0, 0.0]
    # lati long
]

dic_coords = {
    "Trabajo": [0.0, 0.0],
    "Casa": [0.0, 0.0],
    "Parque": [0.0, 0.0]
            #  lat  long
}
coord_vacias = True


# Funcion que representa el login del ususuario en el sistema
def login():
    """Funcion que nos permite solicitar las credenciales del sistema"""

    def captcha(n1):
        operaciones = [((2 + 4) / 6), (10 * 10 - 99), (2 ** 4 - (3 * 5)), (3 - 2)]
        operacion = int(input(f"\nIngrese la suma entre {n1} + {random.choice(operaciones)} \n>> "))
        if operacion == 613:
            return True
        else:
            return False

    def login_main():
        """Retorna un valor 'bool' para determinar el flujo del programa"""
        print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

        i_user = input("\nIngresa el numero de usuario: \n>> ")

        # Comparacion con las variables globales de los datos de ingreso del usuario
        if i_user == g_username:
            i_passwd = input(f"\nIngresa la clave de {i_user}: \n>> ")

            if i_passwd == g_password:
                print("\nSolucina el Captcha para seguir: ")

                numero1 = int(g_username[2:5])
                if captcha(n1=numero1):
                    print("\nSesión iniciada")
                    return True

                else:
                    print("\nError")
                    return False

            else:
                print("\nError")
                return False

        else:
            print("\nError")
            return False

    # Retornando de la funcion 'login_main()'
    return login_main()


# Funcion para cambiar la contraseña del usuario
def cambiar_passwd():
    """Funcion que permite cambiar la contraseña del usuario actual si cumple con los parametros que se dictan"""

    def es_igual(passwd):
        """Compara la contraseña ingresada con la que ya existe
        en el sistema, y retorna 'True' en caso de serlo"""
        if passwd == g_password:
            return True

    confirmacion = input(f"\nConfirme la contraseña actual para el usuario {g_username}: \n>> ")

    # Se confirma que la contraseña sea igual o corresponda al usuario actual
    if es_igual(passwd=confirmacion):
        nueva = input(f"\nIngresa una nueva contraseña para el usuario {g_username}: \n>> ")

        # La nueva contraseña no puede ser igual que la actual
        if es_igual(passwd=nueva):
            print("\nError")
            exit()

        else:
            print(f"\nSe ha cambiado la contraseña para el usuario {g_username}")

    else:
        print("\nError")
        exit()


def definir_coordenadas():
    """Permite interactur con las coordenadas del usuario, tanto las puede llegar a mostrar como a cambiar, segun el
    flujo del programa y las preferencias del usuario"""

    def restricciones(distancia, maximo, minimo):
        """Permite evaluar la validez de las coordenadas ingresadas y que cumplan con restricciones dadas

        Args:
            distancia (float): Valor equivalente a la coordenada que se quiere evaluar (latitud || longitud)
            maximo (float): Valor maximo que puede alcanzar la coordenada ingresada
            minimo (float): Valor minimo que puede alcanzar la coordenada ingresada

        Returns:
            [bool]: Retorna 'True' en caso de que las restricciones se cumplan y sean validas
        """

        # if distancia >= maximo and distancia <= minimo:
        if maximo >= distancia >= minimo:
            return True
        else:
            print("\nError coordenada")
            exit()

    def crear_coordenadas():
        """Permite crear y definir los diferentes valores de coordenadas correspondientes al usuario"""

        # Inicializacion de las variables para acumular el promedio de coordenadas
        lati_avg = 0
        long_avg = 0

        for lugar in dic_coords:
            # Se obtienen las coordenadas de la latitud y se redondean a 3 valores decimales
            dic_coords[lugar][0] = round(float(input(f"\nIngresa el valor decimal para latitud del {lugar} \n>> ")), 3)

            # if 6.284 >= dic_coords[lugar][0] >= 6.077:   # 6.215
            if restricciones(distancia=dic_coords[lugar][0], maximo=6.284, minimo=6.077):
                # Se obtienen las coordenadas de la longitud y se redondean a 3 valores decimales
                dic_coords[lugar][1] = round(
                    float(input(f"\nIngresa el valor decimal para longitud del {lugar} \n>> ")), 3)

                # if -75.841 >= dic_coords[lugar][1] >= -76.049:   # -75.984
                if restricciones(distancia=dic_coords[lugar][1], maximo=-75.841, minimo=-76.077):
                    # Acumulacion de coordenadas para generar un promedio estimado
                    lati_avg += dic_coords[lugar][0]
                    long_avg += dic_coords[lugar][1]

        # Definicion global de la variable, para poder ser usada desde afuera y ser cambiada desde el programa
        global coord_vacias
        # Cambiando la opcion de que las coordenadas ya no estan vacias
        coord_vacias = False

        # Calculo del promedio, dividiendo la sumatoria entre el total de datos dados
        # lati_avg = lati_avg / 3
        # long_avg = long_avg / 3

    def mostrar_coordenadas():
        """Permite mostrar las cooredenadas correspondientes al usuario en caso de que estas esten presentes"""

        count = 1
        for lugar in dic_coords:
            print(f"\nCoordenadas {lugar} [latitud, longitud] {count} : [{dic_coords[lugar][0]}, {dic_coords[lugar][0]}]")

    def cambiar_coordenadas():
        """Permite cambiar las coordenadas de las diferentes que seleccione el usuario"""

        print("\nCoordenada 1 ubicada más al norte \nCoordenada 2 ubicada más al occidente")

        opcion = int(input("\nPresione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú"))

        if opcion == 1:
            dic_coords["Trabajo"][0] = round(float(input(f"\nIngresa el valor decimal para latitud de Trabajo \n>> ")), 3)
            dic_coords["Trabajo"][1] = round(float(input(f"\nIngresa el valor decimal para longitud de Trabajo \n>> ")), 3)

        elif opcion == 2:
            dic_coords['Casa'][0] = round(float(input(f"\nIngresa el valor decimal para latitud de Casa \n>> ")), 3)
            dic_coords['Casa'][1] = round(float(input(f"\nIngresa el valor decimal para longitud de Casa \n>> ")), 3)

        elif opcion == 3:
            dic_coords['Parque'][0] = round(float(input(f"\nIngresa el valor decimal para latitud de Parque \n>> ")), 3)
            dic_coords['Parque'][1] = round(float(input(f"\nIngresa el valor decimal para longitud de Parque \n>> ")), 3)

        else:
            print("\nError actualización")
            exit()

    if coord_vacias:
        print("estan vacias")
        crear_coordenadas()

    else:
        print("estan llenas")
        mostrar_coordenadas()
        cambiar_coordenadas()


# Funcion para elegir la opcion favorita del menu
def elegir_favorito():
    """Recibe como argumentos la lista global de opciones y funciones,
    para seleccionar la favorita y ser movida a la primera posicion

    :returns -> bool"""

    def adivinanzas():
        """Funcion interna de adivinanzas para poder confirmar la seleccion de la opcion favorita"""

        print("\nConfirma tu seleccion:")
        n1 = int(input("\nque le falta al cero para ser mayor que nueve? \n>> "))
        n2 = int(input("\n'X' y 'X' son cuatro, y cuatro y 'X' son seis, cual es el valor de 'X? \n>> "))

        if (n1 + n2) == 3:
            return True
        else:
            return False

    # Se le resta una unidad para poder adaptarse a la posicion dle indice de lista
    seleccion = int(input("\nSeleccione opción favorita ")) - 1

    if seleccion > 4 or seleccion < 0:
        print("\nError")
        exit()
    else:
        if adivinanzas():
            opcion = lista_funciones[seleccion]
            lista_funciones.pop(seleccion)

            lista_funciones.insert(0, opcion)
            print(f"\nHas elegido la opcion '{opcion[0]}' como tu favorita")

        else:
            print("\nError")
            exit()


# Funcion que permite cerrar sesion y finalizar con la ejecucion del programa
def cerrar_sesion():
    """Funcion que permite salir del programa y terminar con la ejecucion del mismo"""

    print("\nHasta pronto")
    exit()


# Lista con las opciones y sus correspondientes funciones (pasadas como objetos), que van a ser usadas en la ejecucion
# Del programa y pueden cambiar de indice de posicion dependiendo las preferencias del usuario
lista_funciones = [
    ["Cambiar contraseña", cambiar_passwd],
    ["Igresar coordenadas actuales", definir_coordenadas],
    ["Ubicar zona wifi más cercana", exit],
    ["Guardar archivo con ubicación cercana", exit],
    ["Actualizar registros de zonas wifi desde archivo", exit],
    ["Elegir opción de menú favorita", elegir_favorito],
    ["Cerrar sesión", cerrar_sesion]
]


# Funcion principal del programa
def main():
    """Funcion principal del programa que determina el flujo y las acciones a relaizar"""

    # Variable de contador, que nos permite acumular los fallos de seleccion del usuario (fuera del 'while')
    errores = 0
    while True:
        print("\nM E N U : \n")

        # Se itera sobre la lista global de opciones, y sus respectivas funciones que se tienen en el menu
        for i in range(7):
            print(f"{i + 1}.) {lista_funciones[i][0]}")

        opcion = int(input("\nElija una opción "))

        # Evalua la seleccion del usuario, y determina la opcion a ejecutar, la cual puede cambiar de posicion
        # Dependiendo si la escoge como favorita, y en cada posicion se ejecuta la que se solicita
        if opcion == 1:
            print("\nUsted ha elegido la opción número 1")
            lista_funciones[0][1]()

        elif opcion == 2:
            print("\nUsted ha elegido la opción 2")
            lista_funciones[1][1]()

        elif opcion == 3:
            print("\nUsted ha elegido la opción 3")
            lista_funciones[2][1]()

        elif opcion == 4:
            print("\nUsted ha elegido la opción 4")
            lista_funciones[3][1]()

        elif opcion == 5:
            print("\nUsted ha elegido la opción 5")
            lista_funciones[4][1]()

        elif opcion == 6:
            lista_funciones[5][1]()

        elif opcion == 7:
            lista_funciones[6][1]()

        else:
            print("\nError")
            errores += 1

            # Terminar la ejecucion del programa cuando se falla mas de 3 veces
            if errores > 3:
                cerrar_sesion()


if __name__ == '__main__':
    # Se evaluan los datos de ingreso preesablecidos, para poder ingresar
    if login():
        # Llamado de la funcion principal
        main()

    else:
        print("\nError")
        exit()

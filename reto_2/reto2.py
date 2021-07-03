"""Reto #2"""
import random

# Credenciales del sistema
username = "51612"
# 'username' reversed
password = username[::-1]


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
        if i_user == username:
            i_passwd = input(f"\nIngresa la clave de {i_user}: \n>> ")

            if i_passwd == password:
                print("\nSolucina el Captcha para seguir: ")

                numero1 = int(username[2:5])
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


# Funcion para elegir la opcion favorita del menu
def elegir_favorito():
    """Recibe como argumentos la lista global de opciones y funciones,
    para seleccionar la favorita y ser movida a la primera posicion
    :eturns -> bool"""

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
    ["Cambiar contraseña", exit],
    ["Igresar coordenadas actuales", exit],
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

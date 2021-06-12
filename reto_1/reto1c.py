import random

# Credeciales del sistema
username = "51612"
# 'username' reversed
password = username[::-1]


def login():
        # Definicion de la funcion que representa el Captcha
    def captcha(n1, n2):
        operacion = int(input(f"\nIngrese la suma entre {n1} + {n2} \n>> "))
        if operacion == (n1 + n2):
            return True
        else:
            return False

    i_user = input("\nIngresa el numero de usuario: \n>> ")
    i_passwd = input(f"\nIngresa la clave de {i_user}: \n>> ")

    # Comparacion con las variables globales de los datos de usuario
    if i_user == username:
        if i_passwd == password:
            print("\nSolucina el Captcha para seguir: ")

            # Numeros aleatorios para el Captcha
            numero1 = random.randint(1, 100)
            numero2 = int(username[2:5])

            if captcha(n1=numero1, n2=numero2):
                return "\nSesión iniciada"
            else:
                return "\nERROR"
    else:
        return "\nERROR, los datos no coinciden, \nIntenta de nuevo"


def principal():
    print("\nBienvenido al sistema de ubicación para zonas públicas WIFI")
    print("\n\tM E N U ")
    print("""
    1.) Ingesar
    2.) Salir
    """)

    opcion = int(input("Que opcion desea realizar? \n>> ").strip())

    if opcion == 1:
        print("Solicitud de datos de ingreso:\n")
        print(login())

    elif opcion == 2:
        print("Has decidido salir :D \nHasta pronto")
        exit()

    else:
        print("\nDato incorrecto o deconocido, intente de nuevo")


if __name__ == '__main__':
    # Ejecucion de la funcion principal
    while True:
        principal()

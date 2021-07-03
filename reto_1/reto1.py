"""Reto #1"""
import random

# Credeciales del sistema
username = "51612"
# 'username' reversed
password = username[::-1]

def captcha(n1):
    """Permite general un captcha de seguridad al usuario para autenticarse en el sistema

    Args:
        n1 (int): Representa los ultimos 3 digitos del numero del usuario

    Returns:
        [bool]: Estado de resultado de las operaciones resueltas por el usuario
    """

    operaciones = [((2 + 4) / 6 ), (10 * 10 - 99), (2 **  4 - (3 * 5)), (3 - 2)]
    operacion = int(input(f"\nIngrese la suma entre {n1} + {random.choice(operaciones)} \n>> "))
    if operacion == 613:
        return True
    else:
        return False


def main():
    """Funcion principal del programa que determina el flujo y las acciones a relaizar"""

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

            else:
                print("\nError")

        else:
            print("\nError")
    else:
        print("\nError")


if __name__ == '__main__':
    # Ejecucion de la funcion principal
    main()

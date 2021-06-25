"""Reto #5"""
import random
from math import *

# Credenciales del sistema
g_username = "51612"
# 'username' reversed
g_password = g_username[::-1]

# Coordenadas de ubicacion del usuario, inicializadas en 0.0
dic_coords = {
    #          lat  long
    "Trabajo": [0.0, 0.0],
    "Casa": [0.0, 0.0],
    "Parque": [0.0, 0.0]
}

# Variables que determinan el flujo del programa y se inicializan en 'True'
coord_vacias = True
ubicacion_vacia = True

# Datos de la ubicaciones de zonas WIFI
ubicaciones_wifi = [
#   dist   lat    long   usrs
    [0.0, 6.135, -75.976, 31],
    [0.0, 6.125, -75.966, 109],
    [0.0, 6.144, -75.936, 151],
    [0.0, 6.124, -75.946, 1035]
]

# Se almacena la informacion correspondiente en un diccionario de datos
informacion = {
    #           lat long
    "actual": [0.0, 0.0],
    #           lat  long usrs
    "zonawifi1":[0.0, 0.0, 0],
    #           dist   transporte   prom
    "recorrido":[0.0, "<UNKNOWN>", 0.0]
    }


def error(frase, salir=False):
    """Genera un mensaje de error, y en caso de ser necesario sale del programa

    Args:
        frase (str): Mensaje de error correspondiente
        salir (bool, optional): Indicador que determina si se finaliza el programa. Por defecto es 'False'
    """

    print(f"\n{frase}")
    if salir:
        exit()


def login():
    """Funcion que nos permite solicitar las credenciales del usuario en el sistema"""

    def captcha(n1):
        """Permite general un captcha de seguridad al usuario para autenticarse en el sistema

        Args:
            n1 (int): Representa los ultimos 3 digitos del numero del usuario

        Returns:
            [bool]: Estado de resultado de las operaciones resueltas por el usuario
        """
        operaciones = [((2 + 4) / 6), (10 * 10 - 99), (2 ** 4 - (3 * 5)), (3 - 2)]
        operacion = int(input(f"\nIngrese la suma entre {n1} + {random.choice(operaciones)} \n>> "))

        if operacion == 613:
            return True

        else:
            return False

    def login_main():
        """Permite determinar el flujo del programa obteniendo las crecendiales del usuario para poder autenticarse en el sistema

        Returns:
            [bool]: Estado de resultado que determina el futuro flujo del programa
        """

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
                    return False

            else:
                return False

        else:
            return False

    # Retornando de la funcion 'login_main()' para ser usada
    return login_main()


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
            error(frase="Error", salir=True)

        else:
            print(f"\nSe ha cambiado la contraseña para el usuario {g_username}")

    else:
        error(frase="Error", salir=True)


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
            error(frase="Error coordenada", salir=True)

    def set_coords(seleccion):
        """Permite establecer las coordenadas del usuario, y a su vez evaluando su valides y restricciones correspondientes,
        independiente si han sido creadas o no en el sistema

        Args:
            lugar (str): Corresponde al tipo de ubicacion al que corresponden las coordenadas que se definen
        """

        # Lista con los lugares correspondientes a las coordenadas del usuario
        lugares = [lugar for lugar in dic_coords]
        # lugares = ['Trabajo', 'Casa', 'Parque']

        # Se obtiene el valor decimal de la LATITUD
        dic_coords[lugares[seleccion]][0] = round(float(input(f"\nIngresa el valor decimal para latitud de {lugares[seleccion]} \n>> ")), 3)
        # Evaluacion de las restricciones tanto de latitud como de longitud, con los valores especificados
        # if latitud >= 6.284 and distancia <= 6.077
        if restricciones(distancia=dic_coords[lugares[seleccion]][0], maximo=6.284, minimo=6.077):  # LATITUD [0]
            # Se obtiene el valor decimal de la LONGITUD
            dic_coords[lugares[seleccion]][1] = round(float(input(f"\nIngresa el valor decimal para longitud de {lugares[seleccion]} \n>> ")), 3)
            # if longitud >= -75.841 and longitud <= -76.077
            restricciones(distancia=dic_coords[lugares[seleccion]][1], maximo=-75.841, minimo=-76.077)  # LONGITUD [1]

    def crear_coordenadas():
        """Permite crear y definir los diferentes valores de coordenadas correspondientes al usuario"""

        # Se pasa como argumento el indice correspondiente al lugar del usuario (Trabajo, Casa, Parque)
        set_coords(seleccion=0)
        set_coords(seleccion=1)
        set_coords(seleccion=2)
        # Estableciendo la variable como global, para poder ser accesible desde afuera y ser cambiada desde el programa
        global coord_vacias
        # Cambiando la opcion de que las coordenadas indicando que ya no estan vacias
        coord_vacias = False

    def mostrar_coordenadas():
        """Permite mostrar las cooredenadas correspondientes al usuario en caso de que estas esten presentes"""

        count = 1
        for lugar in dic_coords:
            print(f"Coordenadas {lugar} [latitud, longitud] {count} : [{dic_coords[lugar][0]}, {dic_coords[lugar][1]}]")
            count += 1

    def cambiar_coordenadas():
        """Permite cambiar las coordenadas de las diferentes que seleccione el usuario"""

        print("\nCoordenada 1 ubicada más al norte \nCoordenada 2 ubicada más al occidente")

        opcion = int(
            input("\nPresione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú "))

        # Evalua la seleccion del usuario para procesar el set_coords a realizar
        if opcion == 0:
            # Llamado de la funcion principal que representa el menu de opciones
            main()

        # Pasa la opcion del usuario como parametro de la funcion que actualiza el par de coordenadas correspondientes
        elif opcion == 1:
            set_coords(seleccion=(opcion - 1))

        elif opcion == 2:
            set_coords(seleccion=(opcion - 1))

        elif opcion == 3:
            set_coords(seleccion=(opcion - 1))

        else:
            error(frase="Error actualización", salir=True)

    if coord_vacias:
        crear_coordenadas()

    else:
        mostrar_coordenadas()
        cambiar_coordenadas()


def ubicar_zona_wifi():
    """Permite ubicar la zona WIFI mas cercana al usuario, mostrandole las diferentes opciones y datos relacionados 
    con las mismas, como las coordenadas de ubicacion y la distancia entre las mismas
    """

    def calcular_distancia(seleccion):
        """Calculo de distancia entre dos puntos, y determina los dos puntos mas cercanos a la ubicacion del usuario
        Recibe como parametro el lugar de ubicacion actual del usuario (str) para ser operado en el calculo

        Args:
            seleccion (str): Seleccion del usuario correspondiente a la ubicacion actual, para realizar el calculo
            con las zonas mas cercanas
        """

        def interna(dato):
            """Calculo interno de distancias

            Permite calcular la distancia entre dos puntos, es dacir, la ubicacion actual y las zonas wifi cercanas disponibles

            Args:
                dato (int): Numero que indica el indice del valor de coordenadas en la lista de ubicaciones
                actuales de WIFI disponibles para el calculo

            Returns:
                (float): Distancia que hay entre los dos puntos que se comparan [ubicacion actual, zona wifi]
            """

            # el parametro 'dato' equivale al indice de posicion de la lista de ubicaciones
            radio = 6372.795477598  # Km (Radio de la tierra)
            # Valor a comparar escogido por el usuario (ubicacion actual)
            lat1, long1 = dic_coords[seleccion][0], dic_coords[seleccion][1]
            # Valores de las zonas wifi cercanas, correspondiente al indice en la lista
            lat2, long2 = ubicaciones_wifi[dato][1], ubicaciones_wifi[dato][2]

            latitud = lat2 - lat1
            longitud = long2 - long1

            # Usando las funciones del modulo 'math' para calcular la distancia entre los 2 puntos que se indican
            distancia = (2 * radio * asin(sqrt((sin(latitud / 2) ** 2) + cos(lat1) * cos(lat2) * (sin(longitud / 2) ** 2))))
            distancia = round(distancia, 2)

            return distancia

        def calc_tiempo(distancia):
            """Calcula el tiempo promedio desde la ubicacion del usuario hasta el punto WIFI seleccionado

            tambien permite actualizar el diccionario general de 'informacion' del usuario con los datos
            correspondientes al mismo, como la ubicacion actual, la zona WIFI, y el recorrido

            Args:
                distancia (float): Distancia en metros entre la ubicacion del usuario y la zona WIFI
            """
            # Velocidad promedio de BUS
            vel_bus = 16.67 - 0.483
            # Velocidad promedio de AUTO
            vel_auto = 20.83
            # Calculo del tiempo promedio
            tiempo_bus = distancia / vel_bus
            tiempo_auto = distancia / vel_auto

            print(f"\nEl tiempo promedio en AUTO es de {round(tiempo_auto, 2)}")
            print(f"El tiempo promedio en BUS es de {round(tiempo_bus, 2)}")

            # Cambiando el valor de la variable de ubicacion vacia como 'False' puesto  que ya han sido inngresados los datos
            global ubicacion_vacia
            ubicacion_vacia = False

            # Actualizando la informacion de ubicacion actual del usuario [latitud, longitud]
            informacion["actual"] = [dic_coords[seleccion][0], dic_coords[seleccion][1]]
            # Actualizando la informacion de la primera zona wifi [latitud, longitud, prom_usrs]
            informacion["zonawifi1"] = [zonas_wifi[0][1], zonas_wifi[0][2], zonas_wifi[0][3]]
            # Actualizando la informacion del recorrido del usuario [distancia, tipo, tiempo]
            informacion["recorrido"] = [distancia, "Auto", round(tiempo_auto, 2)]

            salir = int(input("\nIngrese 0 para salir "))

            if salir == 0:
                main()

        # Se actualiza el valor de la distancia entre la zona WIFI y la ubicacion escogida por el usuario
        for lugar in range(4):
            # Se asigna en la posicion de lista correspondiente al valor de la distancia entre puntos [0]
            ubicaciones_wifi[lugar][0] = interna(lugar)

        print("\nZonas wifi cercanas con menos usuarios")

        count = 1
        # Lista para almmacenar las dos zonas WIFI mas cercanas al usuario
        zonas_wifi = []
        # Se itera sobre las zonas wifi ordenadas de menor a mayor distancia
        for data in sorted(ubicaciones_wifi):
            print(f"La zona wifi {count}: ubicada en [{data[1]}, {data[2]}]: a {data[0]} metros, tiene en promedio {data[3]} usuarios")
            # Se agrega la zona wifi en orden de distancia a la lista de zonas wifi
            zonas_wifi.append(data)
            count += 1
            # Se termina con el ciclo limitando la salida a dos zonas WIFI unicamente
            if count > 2:
                break

        respuesta = int(input("\nElija 1 o 2 para recibir indicaciones de llegada "))
        print(f"Su respuesta fue {respuesta}")

        # Se pasan los valores de la lista de zonas WIFI
        # al ejecutar la funcion de 'calc_tiempo()' se actualizan las variables globales de 'informacion {}'
        if respuesta == 1:
            calc_tiempo(distancia=zonas_wifi[0][0])

        elif respuesta == 2:
            calc_tiempo(distancia=zonas_wifi[1][0])

        else:
            error(frase="Error zona wifi", salir=True)

    # Se comprueba si las coordenadas del usuario estan dadas
    if coord_vacias:
        error(frase="Error sin registro de coordenadas", salir=True)

    else:
        # Se listan las coordenadas actuales asociadas al usuario, iterando sobre ellas
        count = 1
        for lugar in dic_coords:
            print(f"Coordenadas {count} [latitud, longitud] {lugar} : [{dic_coords[lugar][0]}, {dic_coords[lugar][1]}]")
            count += 1

        opcion = int(input("\nPor favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión "))

        # Se pasan los diferentes lugares, en funcion de la seleccion del usuario, para ser calculadas sus distancias
        if opcion == 1:
            calcular_distancia(seleccion="Trabajo")

        elif opcion == 2:
            calcular_distancia(seleccion="Casa")

        elif opcion == 3:
            calcular_distancia(seleccion="Parque")

        else:
            error(frase="Error ubicación", salir=True)


def guardar_ubicacion():
    """Muestra la informacion general del usuario permitiendo la confirmacion de la misma
    y termina la ejecucion del programa"""

    # Evalua si las coordenadas del usuario y la ubicacion actual fueron dadas
    if coord_vacias or ubicacion_vacia:
        error(frase="Error de alistamiento", salir=True)

    else:
        print(informacion)

        respuesta = int(input("\n¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal"))

        if respuesta == 0:
            main()

        elif respuesta == 1:
            error(frase="Exportando archivo", salir=True)


def actualizar_zona_wifi():
    """Actualiza los datos de registro de las zonas WIFI del usuario usando un archivo exerno"""

    if ubicacion_vacia:
        error(frase="Hasta pronto", salir=True)

    else:
        respuesta = int(input("\nDatos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal "))

        if respuesta == 0:
            main()


def elegir_favorito():
    """Permite elegir una opcin favorita y recibe como argumentos la lista global de opciones y funciones,
    para seleccionar la favorita y ser removida y movida a la primera posicion de dicha lista"""

    def adivinanzas():
        """Funcion interna de adivinanzas para poder confirmar la seleccion de la opcion favorita

        Returns:
            [bool]: estado de respuesta del usuario para la adivinanza
        """

        print("\nConfirma tu seleccion:")
        n1 = int(input("\nque le falta al cero para ser mayor que nueve? \n>> "))
        n2 = int(input("\n'X' y 'X' son cuatro, y cuatro y 'X' son seis, cual es el valor de 'X? \n>> "))

        if (n1 + n2) == 3:
            return True

        else:
            return False

    # Se le resta una unidad para poder adaptarse a la posicion del indice de lista
    seleccion = int(input("\nSeleccione opción favorita ")) - 1

    if seleccion > 4 or seleccion < 0:
        error(frase="Error", salir=True)

    else:
        if adivinanzas():
            opcion = lista_funciones[seleccion]
            lista_funciones.pop(seleccion)
            lista_funciones.insert(0, opcion)
            print(f"\nHas elegido la opcion '{opcion[0]}' como tu favorita")

        else:
            error(frase="Error", salir=True)


def cerrar_sesion():
    """Funcion que permite salir del programa y terminar con la ejecucion del mismo"""

    error(frase="Hasta pronto", salir=True)


# Lista con las opciones y sus correspondientes funciones (pasadas como objetos), que van a ser usadas en la ejecucion
# Del programa y pueden cambiar de indice de posicion dependiendo las preferencias del usuario
lista_funciones = [
    ["Cambiar contraseña", cambiar_passwd],
    ["Igresar coordenadas actuales", definir_coordenadas],
    ["Ubicar zona wifi más cercana", ubicar_zona_wifi],
    ["Guardar archivo con ubicación cercana", guardar_ubicacion],
    ["Actualizar registros de zonas wifi desde archivo", actualizar_zona_wifi],
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
            print("\nUsted ha elegido la opción 1\n")
            lista_funciones[0][1]()

        elif opcion == 2:
            print("\nUsted ha elegido la opción 2\n")
            lista_funciones[1][1]()

        elif opcion == 3:
            print("\nUsted ha elegido la opción 3\n")
            lista_funciones[2][1]()

        elif opcion == 4:
            print("\nUsted ha elegido la opción 4\n")
            lista_funciones[3][1]()

        elif opcion == 5:
            print("\nUsted ha elegido la opción 5\n")
            lista_funciones[4][1]()

        elif opcion == 6:
            lista_funciones[5][1]()

        elif opcion == 7:
            lista_funciones[6][1]()

        else:
            error(frase="Error")
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
        error(frase="Error", salir=True)

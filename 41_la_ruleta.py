'''
Simulador de Ruleta
Crea un programa en Python que simule una ruleta de casino. La ruleta 
tiene números del 0 al 36, y el programa debe:

Pedir al usuario que elija una de las siguientes opciones de apuesta:

Un número específico del 0 al 36.
Apostar por "rojo" o "negro".
Apostar por "par" o "impar".
Apostar por "bajo" (1-18) o "alto" (19-36).
Girar la ruleta generando un número aleatorio entre 0 y 36.

El programa asignará un color al número según las reglas de la ruleta 
(por ejemplo, 0 es verde, números rojos y negros alternados).
Determinar si la apuesta del usuario ganó o perdió.

Mostrar el resultado de la ruleta (número y color) y si el usuario ganó o perdió su apuesta.
'''

import random

def obtener_color(numero):
    # En la ruleta, los números rojos y negros se alternan
    rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    if numero == 0:
        return "verde"
    elif numero in rojos:
        return "rojo"
    else:
        return "negro"

def ruleta():
    print("¡Bienvenido al simulador de ruleta!")
    print("Opciones de apuesta:")
    print("1. Número específico (0-36)")
    print("2. Color ('rojo' o 'negro')")
    print("3. Par o impar ('par' o 'impar')")
    print("4. Bajo o alto ('bajo' 1-18 o 'alto' 19-36)")

    apuesta = input("Elige una opción de apuesta (1/2/3/4): ")

    if apuesta == "1":
        try:
            numero_elegido = int(input("Elige un número del 0 al 36: "))
            if numero_elegido < 0 or numero_elegido > 36:
                print("Número no válido. Debe estar entre 0 y 36.")
                return
        except ValueError:
            print("Entrada no válida. Debes introducir un número.")
            return

    elif apuesta == "2":
        color_elegido = input("Elige un color ('rojo' o 'negro'): ").lower()
        if color_elegido not in ["rojo", "negro"]:
            print("Color no válido. Debe ser 'rojo' o 'negro'.")
            return

    elif apuesta == "3":
        paridad_elegida = input("Elige 'par' o 'impar': ").lower()
        if paridad_elegida not in ["par", "impar"]:
            print("Paridad no válida. Debe ser 'par' o 'impar'.")
            return

    elif apuesta == "4":
        rango_elegido = input("Elige 'bajo' (1-18) o 'alto' (19-36): ").lower()
        if rango_elegido not in ["bajo", "alto"]:
            print("Rango no válido. Debe ser 'bajo' o 'alto'.")
            return

    else:
        print("Opción no válida. Intenta de nuevo.")
        return

    # Girar la ruleta
    numero_ruleta = random.randint(0, 36)
    color_ruleta = obtener_color(numero_ruleta)

    print(f"\nLa ruleta ha girado y cayó en el número {numero_ruleta} ({color_ruleta}).")

    # Evaluar resultado
    if apuesta == "1":
        if numero_elegido == numero_ruleta:
            print("¡Felicidades! Has acertado el número.")
        else:
            print("Lo siento, no acertaste el número.")

    elif apuesta == "2":
        if color_elegido == color_ruleta:
            print("¡Felicidades! Has acertado el color.")
        else:
            print("Lo siento, no acertaste el color.")

    elif apuesta == "3":
        if numero_ruleta == 0:
            print("Lo siento, el 0 no cuenta como par ni impar.")
        elif (numero_ruleta % 2 == 0 and paridad_elegida == "par") or \
             (numero_ruleta % 2 != 0 and paridad_elegida == "impar"):
            print("¡Felicidades! Has acertado la paridad.")
        else:
            print("Lo siento, no acertaste la paridad.")

    elif apuesta == "4":
        if numero_ruleta == 0:
            print("Lo siento, el 0 no cuenta como bajo ni alto.")
        elif (1 <= numero_ruleta <= 18 and rango_elegido == "bajo") or \
             (19 <= numero_ruleta <= 36 and rango_elegido == "alto"):
            print("¡Felicidades! Has acertado el rango.")
        else:
            print("Lo siento, no acertaste el rango.")

# Ejecutar el programa
if __name__ == "__main__":
    ruleta()

'''

Memorama

Crea un programa en Python que simule un juego de memoria (Memorama) en la consola. El juego debe:

Mostrar un tablero oculto con pares de elementos (números, letras, o palabras).
Permitir al usuario seleccionar dos posiciones en el tablero (por ejemplo, "A1" y "B2").
Mostrar los elementos seleccionados. Si coinciden, se quedan descubiertos; si no, se vuelven a ocultar.
Finalizar cuando el usuario encuentre todos los pares.
Mostrar el número de intentos realizados al final del juego.

'''

import random

def crear_tablero():
    """Crea el tablero con pares de elementos ocultos."""
    elementos = list("ABCDEFGH")  # 8 pares de letras
    elementos *= 2  # Duplicar para crear los pares
    random.shuffle(elementos)  # Mezclar los elementos
    
    # Crear un tablero 4x4
    tablero = [elementos[i:i+4] for i in range(0, len(elementos), 4)]
    return tablero

def mostrar_tablero(tablero, descubiertos):
    """Muestra el tablero actual, con elementos descubiertos o '?'."""
    print("\n   1  2  3  4")
    print("  -------------")
    for i, fila in enumerate(tablero):
        linea = [f"{cel if (i, j) in descubiertos else '?'}" for j, cel in enumerate(fila)]
        print(f"{chr(65+i)} | {'  '.join(linea)} |")
    print("  -------------")

def obtener_posicion(descubiertos):
    """Solicita una posición al usuario y la valida."""
    while True:
        entrada = input("Selecciona una posición (ejemplo: A1): ").upper()
        if len(entrada) == 2 and entrada[0] in "ABCD" and entrada[1] in "1234":
            fila = ord(entrada[0]) - 65
            columna = int(entrada[1]) - 1
            if (fila, columna) not in descubiertos:
                return fila, columna
            else:
                print("Esa carta ya está descubierta. Elige otra posición.")
        else:
            print("Entrada inválida. Inténtalo de nuevo.")

def memorama():
    print("¡Bienvenido al Memorama!")
    tablero = crear_tablero()
    descubiertos = set()
    intentos = 0

    while len(descubiertos) < 16:  # Mientras no se descubran todos los pares
        mostrar_tablero(tablero, descubiertos)
        
        print("\nSelecciona la primera carta:")
        f1, c1 = obtener_posicion(descubiertos)
        
        print("\nSelecciona la segunda carta:")
        f2, c2 = obtener_posicion(descubiertos | {(f1, c1)})
        
        intentos += 1
        
        # Mostrar las cartas seleccionadas temporalmente
        print("\nTablero actual:")
        descubiertos_temporales = descubiertos | {(f1, c1), (f2, c2)}
        mostrar_tablero(tablero, descubiertos_temporales)
        
        # Comprobar si hay coincidencia
        if tablero[f1][c1] == tablero[f2][c2]:
            print("¡Es un par!")
            descubiertos.add((f1, c1))
            descubiertos.add((f2, c2))
        else:
            print("No coinciden. Inténtalo de nuevo.")
    
    print("\n¡Felicidades! Has encontrado todos los pares.")
    print(f"Número total de intentos: {intentos}")

# Ejecutar el juego
if __name__ == "__main__":
    memorama()



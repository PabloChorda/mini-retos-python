'''

Desarrollar un Escape Room Virtual en Python en el que el jugador 
debe superar tres salas con acertijos para escapar de un edificio misterioso.

Introducción:

Presenta la historia del escape y espera que el usuario inicie 
la aventura con Enter.
Sala 1 – Habitación del Misterio:
Acertijo:
"Soy algo que puede correr, pero nunca caminar; tengo boca pero nunca 
hablar; tengo cabeza pero nunca llorar. ¿Qué soy?"
Respuesta correcta: "río" (aceptando "río" o "rio").
Máximo 3 intentos.
Sala 2 – Pasillo de las Sombras:
Acertijo:
Secuencia: 3, 1, 4, 1, 5, 9, 2, ?
Respuesta correcta: "6".
Máximo 3 intentos.
Sala 3 – La Sala Final:
Acertijo:
Descifra el mensaje "URYYB JBEYQ" (en ROT13).
Respuesta correcta: "HELLO WORLD".
Máximo 3 intentos.

Lógica del Juego:
Si el jugador falla en cualquier sala, el juego termina; 
si supera las tres, se muestra un mensaje de éxito.

'''


import time
import sys

def intro():
    """Muestra la introducción del juego."""
    print("Bienvenido al Escape Room Virtual.\n")
    time.sleep(1)
    print("Estás atrapado en un edificio misterioso y deberás resolver varios acertijos para escapar.\n")
    input("Presiona Enter para comenzar tu aventura...\n")

def room_1():
    """Primera sala: Habitación del Misterio con una adivinanza."""
    print("\n--- Habitación del Misterio ---")
    print("La puerta se cierra tras de ti. En la pared, encuentras un mensaje grabado:")
    print('"Soy algo que puede correr, pero nunca caminar; tengo boca pero nunca hablar; tengo cabeza pero nunca llorar. ¿Qué soy?"')
    attempts = 3
    while attempts:
        answer = input("Tu respuesta: ").strip().lower()
        if answer in ("río", "rio"):
            print("¡Correcto! El acertijo se resuelve y una puerta secreta se abre.\n")
            return True
        else:
            attempts -= 1
            print(f"Respuesta incorrecta. Te quedan {attempts} intento(s).")
    print("Has fallado el acertijo. La habitación se oscurece y pierdes la oportunidad de avanzar.")
    return False

def room_2():
    """Segunda sala: Pasillo de las Sombras con una secuencia numérica."""
    print("\n--- Pasillo de las Sombras ---")
    print("Avanzas por un pasillo oscuro. En el suelo, ves números dispersos: 3, 1, 4, 1, 5, 9, 2, ?")
    print("Parece que la secuencia es el comienzo de los dígitos de pi. ¿Cuál es el siguiente número?")
    attempts = 3
    while attempts:
        answer = input("Tu respuesta: ").strip()
        if answer == "6":
            print("¡Exacto! Has descubierto la clave para abrir una puerta oculta.\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrecto. Te quedan {attempts} intento(s).")
    print("No logras descifrar la secuencia. El pasillo se oscurece y quedas atrapado.")
    return False

def room_3():
    """Tercera sala: La Sala Final con un mensaje cifrado en ROT13."""
    print("\n--- La Sala Final ---")
    print("Finalmente, llegas a una gran sala con una caja fuerte en el centro.")
    print("En la caja, un mensaje cifrado: 'URYYB JBEYQ'.")
    print("Parece un mensaje en código ROT13. ¿Cuál es el mensaje descifrado?")
    attempts = 3
    while attempts:
        answer = input("Tu respuesta: ").strip().upper()
        if answer == "HELLO WORLD":
            print("¡Correcto! La caja se abre y encuentras la llave que te permite salir.\n")
            return True
        else:
            attempts -= 1
            print(f"Respuesta incorrecta. Te quedan {attempts} intento(s).")
    print("No logras descifrar el mensaje y la sala se cierra para siempre.")
    return False

def final():
    """Mensaje final de éxito."""
    print("\n--- ¡Felicidades! ---")
    print("Has logrado superar todos los desafíos y escapar del edificio misterioso.")
    print("Gracias por jugar al Escape Room Virtual.")

def main():
    """Función principal que coordina el flujo del juego."""
    intro()
    if not room_1():
        sys.exit("Fin del juego. Inténtalo de nuevo.")
    time.sleep(1)
    if not room_2():
        sys.exit("Fin del juego. Inténtalo de nuevo.")
    time.sleep(1)
    if not room_3():
        sys.exit("Fin del juego. Inténtalo de nuevo.")
    final()

if __name__ == '__main__':
    main()

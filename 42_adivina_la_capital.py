'''

Adivina la Capital

Crea un programa en Python que proponga al usuario adivinar la capital de un 
país aleatorio. El programa debe:

Contener al menos 10 países y sus respectivas capitales en un diccionario.
Seleccionar un país aleatorio y pedirle al usuario que adivine su capital.
Verificar si la respuesta es correcta o incorrecta.
Permitirle al usuario jugar varias rondas hasta que decida salir.
Mostrar un contador de respuestas correctas e incorrectas al final de cada ronda.

'''

import random

def adivina_la_capital():
    # Diccionario de países y sus capitales
    paises_capitales = {
        "España": "Madrid",
        "Francia": "París",
        "Alemania": "Berlín",
        "Italia": "Roma",
        "Portugal": "Lisboa",
        "Reino Unido": "Londres",
        "Japón": "Tokio",
        "Canadá": "Ottawa",
        "Australia": "Canberra",
        "Brasil": "Brasilia"
    }

    print("¡Bienvenido al juego 'Adivina la Capital'!")
    print("Intenta adivinar la capital del país que te voy a proponer.")
    
    # Variables para contar respuestas correctas e incorrectas
    respuestas_correctas = 0
    respuestas_incorrectas = 0
    
    while True:
        # Selecciona un país aleatorio
        pais = random.choice(list(paises_capitales.keys()))
        capital_correcta = paises_capitales[pais]

        # Pide al usuario que adivine la capital
        print(f"\n¿De qué país es la capital {capital_correcta}?")
        respuesta_usuario = input("Escribe tu respuesta (o 'salir' para terminar): ").strip()

        # Condición de salida
        if respuesta_usuario.lower() == "salir":
            break
        
        # Verificar respuesta
        if respuesta_usuario.lower() == pais.lower():
            print("¡Correcto!")
            respuestas_correctas += 1
        else:
            print(f"Incorrecto. La respuesta correcta es {pais}.")
            respuestas_incorrectas += 1

        # Mostrar las estadísticas al final de cada ronda
        print(f"\nRespuestas correctas: {respuestas_correctas}")
        print(f"Respuestas incorrectas: {respuestas_incorrectas}")
    
    # Mensaje final cuando el jugador decida salir
    print("\n¡Gracias por jugar! Aquí están tus estadísticas finales:")
    print(f"Respuestas correctas: {respuestas_correctas}")
    print(f"Respuestas incorrectas: {respuestas_incorrectas}")

# Ejecutar el juego
adivina_la_capital()

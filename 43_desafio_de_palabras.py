'''

Desafío de Palabras

Crea un programa en Python que permita al usuario introducir una palabra inicial y, 
utilizando las letras de esa palabra, genere otras palabras válidas. El programa debe:

Pedir al usuario una palabra base (mínimo 3 letras).
Generar todas las posibles combinaciones de las letras de esa palabra.
Comprobar si las combinaciones generadas son palabras válidas utilizando un archivo de palabras 
en español (puedes proporcionar una lista predefinida de palabras para simplificar).
Mostrar al usuario las palabras válidas encontradas.
Contar cuántas palabras válidas se generaron.

'''

import itertools

def cargar_diccionario():
    """Carga un diccionario de palabras en español."""
    # Lista simplificada de palabras válidas en español (puedes ampliar esta lista o usar un archivo externo)
    return [
        "casa", "saca", "asa", "saco", "cosa", "ocas", "caso", "oso", 
        "oso", "as", "sa", "acaso", "casas", "ocasos", "cosa", "caso"
    ]

def generar_palabras_validas(palabra_base, diccionario):
    """Genera todas las palabras válidas usando las letras de la palabra base."""
    palabras_validas = set()
    for i in range(1, len(palabra_base) + 1):
        combinaciones = itertools.permutations(palabra_base, i)
        for combinacion in combinaciones:
            posible_palabra = "".join(combinacion)
            if posible_palabra in diccionario:
                palabras_validas.add(posible_palabra)
    return palabras_validas

def desafio_palabras():
    print("¡Bienvenido al Desafío de Palabras!")
    palabra_base = input("Introduce una palabra base (mínimo 3 letras): ").strip().lower()
    
    # Validar longitud de la palabra base
    while len(palabra_base) < 3:
        palabra_base = input("La palabra debe tener al menos 3 letras. Inténtalo de nuevo: ").strip().lower()
    
    diccionario = cargar_diccionario()
    palabras_validas = generar_palabras_validas(palabra_base, diccionario)
    
    print("\nPalabras válidas generadas:")
    for palabra in sorted(palabras_validas):
        print(f"- {palabra}")
    
    print(f"\nTotal de palabras válidas encontradas: {len(palabras_validas)}")
    print("¡Gracias por jugar!")

# Ejecutar el desafío
desafio_palabras()



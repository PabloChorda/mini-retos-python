'''
Simulador de Ecosistema de Abejas y Flores

Descripción del ejercicio:
Diseña una simulación en la que un jardín (una cuadrícula de 10x10) contiene flores y abejas.

Flores: Aparecen en posiciones aleatorias y cada una tiene una cantidad de néctar.
Abejas: Se mueven aleatoriamente por el jardín. Si una abeja se encuentra en la misma celda que una flor, 
“chupa” parte del néctar y gana energía, mientras la flor lo pierde.
Dinámica: Si una flor se queda sin néctar, se “regenera” automáticamente con un nuevo valor aleatorio.
Salida: Cada iteración se muestra el estado del jardín en ASCII, indicando la posición de flores y abejas, durante 20 ciclos de simulación.
'''

import random
import time

# Configuración del jardín
GRID_SIZE = 10
ITERACIONES = 20

# Clase para representar una Flor
class Flor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.regenerar()
    
    def regenerar(self):
        self.nectar = random.randint(3, 8)  # Cantidad de néctar disponible

# Clase para representar una Abeja
class Abeja:
    def __init__(self, id):
        self.id = id
        self.x = random.randint(0, GRID_SIZE - 1)
        self.y = random.randint(0, GRID_SIZE - 1)
        self.energia = 5

    def mover(self):
        # Movimiento aleatorio: se mueve en una dirección (arriba, abajo, izquierda o derecha)
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        self.x = (self.x + dx) % GRID_SIZE
        self.y = (self.y + dy) % GRID_SIZE

# Crear flores y abejas
flores = [Flor(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)) for _ in range(10)]
abejas = [Abeja(i) for i in range(3)]

def dibujar_jardin():
    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    # Colocar flores (si hay varias, mostrar número de néctar)
    for f in flores:
        grid[f.y][f.x] = str(f.nectar)
    # Colocar abejas (si coincide con flor, se ve la abeja en mayúscula)
    for a in abejas:
        grid[a.y][a.x] = 'A'
    # Mostrar cuadrícula
    print('\n'.join(' '.join(celda for celda in fila) for fila in grid))

# Simulación
for t in range(ITERACIONES):
    print(f"\nIteración {t+1}")
    # Cada abeja se mueve y busca flores en su posición
    for abeja in abejas:
        abeja.mover()
        for f in flores:
            if abeja.x == f.x and abeja.y == f.y:
                if f.nectar > 0:
                    abeja.energia += 1
                    f.nectar -= 1
                    print(f"Abeja {abeja.id} recoge néctar en ({f.x},{f.y}). Energía: {abeja.energia}")
                if f.nectar == 0:
                    f.regenerar()
                    print(f"Flor en ({f.x},{f.y}) se regenera.")
    dibujar_jardin()
    time.sleep(0.8)

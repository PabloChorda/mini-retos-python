
'''
Simulador de Gestión de Tráfico Aéreo con IA

¡Diseña un sistema que optimice el tráfico aéreo en un aeropuerto virtual usando algoritmos de planificación 
inteligente! Los aviones deben aterrizar/despegar de manera segura y eficiente, evitando colisiones y minimizando tiempos de espera.

* Requisitos:

Entorno del Aeropuerto:
Pista única con capacidad limitada (solo 1 avión puede usar la pista a la vez).
Zona de espera aérea (holding pattern) para aviones en cola.
Condiciones climáticas dinámicas (viento, tormentas) que afectan las operaciones.

* Aviones:

Cada avión tiene: ID, tipo (comercial, carga, emergencia), combustible restante, prioridad (emergencia > carga > comercial).
Consumo de combustible por avion: 1 unidad por minuto en espera.
* Algoritmo de Planificación (Tú lo implementas):

* Decide el orden de aterrizaje/despegue considerando:

Prioridad del vuelo.
Combustible restante (aviones con <10 unidades tienen prioridad crítica).
Condiciones climáticas (ej: retrasos por tormenta).
Debe minimizar el tiempo total de espera y evitar colapsos.

* Simulación en Tiempo Real:

Interfaz ASCII/gráfica que muestre:
Aviones en vuelo, espera y en pista.
Tiempo transcurrido y métricas de eficiencia.
Generación aleatoria de eventos (emergencias, cambios climáticos).

'''

import heapq
import random
import time
from collections import deque

class Avion:
    def __init__(self, id, tipo, combustible):
        self.id = id
        self.tipo = tipo
        self.combustible = combustible
        self.tiempo_espera = 0
        self.prioridad = 0
        self._calcular_prioridad()

    def _calcular_prioridad(self):
        prioridades = {"emergencia": 3, "carga": 2, "comercial": 1}
        self.prioridad = prioridades[self.tipo]
        if self.combustible < 10:
            self.prioridad += 3  # Prioridad crítica

    def actualizar(self):
        self.combustible = max(self.combustible - 1, 0)
        self.tiempo_espera += 1
        self._calcular_prioridad()

    def __lt__(self, other):
        return self.prioridad > other.prioridad  # Ordenar por prioridad descendente

class TorreControl:
    def __init__(self):
        self.cola_espera = []
        self.pista_libre = True
        self.tiempo = 0
        self.aviones_atendidos = 0
        self
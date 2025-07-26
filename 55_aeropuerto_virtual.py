
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

TIPOS_AVION = {
    "emergencia": 3,
    "carga": 2,
    "comercial": 1
}

CLIMAS = ["despejado", "viento", "tormenta"]

class Avion:
    def __init__(self, id, tipo, combustible):
        self.id = id
        self.tipo = tipo
        self.combustible = combustible
        self.prioridad_base = TIPOS_AVION[tipo]

    def prioridad(self):
        if self.combustible < 10:
            return 100  # prioridad crítica
        return self.prioridad_base * 10 - self.combustible

    def __lt__(self, other):
        return self.prioridad() > other.prioridad()

    def __repr__(self):
        return f"[{self.id} | {self.tipo} | fuel: {self.combustible}]"

class Aeropuerto:
    def __init__(self):
        self.minuto = 0
        self.clima = "despejado"
        self.zona_espera = []
        self.en_pista = None
        self.log = []

    def generar_avion(self):
        tipos = ["comercial", "carga", "emergencia"]
        id = f"A{random.randint(100,999)}"
        tipo = random.choices(tipos, weights=[6,3,1])[0]
        combustible = random.randint(5, 50)
        avion = Avion(id, tipo, combustible)
        heapq.heappush(self.zona_espera, avion)
        print(f"🛬 Nuevo avión en espera: {avion}")

    def actualizar_clima(self):
        self.clima = random.choices(CLIMAS, weights=[6,2,2])[0]
        print(f"🌤️  Clima actual: {self.clima}")

    def procesar_turno(self):
        self.minuto += 1
        print(f"\n⏱️  Minuto {self.minuto}")
        self.actualizar_clima()

        # Todos los aviones consumen combustible
        for avion in self.zona_espera:
            avion.combustible -= 1

        # Retirar aviones sin combustible
        self.zona_espera = [a for a in self.zona_espera if a.combustible > 0]
        heapq.heapify(self.zona_espera)

        # Si pista libre y clima permite, aterriza uno
        if not self.en_pista and self.clima != "tormenta" and self.zona_espera:
            avion = heapq.heappop(self.zona_espera)
            self.en_pista = avion
            print(f"🛩️  Aterriza: {avion}")
        else:
            print("🛑 Pista ocupada o clima adverso.")

        # Libera pista tras 1 turno
        if self.en_pista and self.minuto % 2 == 0:
            print(f"✅ {self.en_pista.id} ha aterrizado.")
            self.log.append((self.en_pista.id, self.minuto))
            self.en_pista = None

    def mostrar_estado(self):
        print("\n✈️ Aviones en espera:")
        for avion in sorted(self.zona_espera, reverse=True):
            critico = "‼️" if avion.combustible < 10 else ""
            print(f"  {avion} {critico}")

def simular():
    aeropuerto = Aeropuerto()

    for _ in range(20):  # minutos de simulación
        if random.random() < 0.6:
            aeropuerto.generar_avion()
        aeropuerto.procesar_turno()
        aeropuerto.mostrar_estado()
        time.sleep(0.5)  # para efecto visual, quitar si no se desea

    print("\n📊 Resumen:")
    for entrada in aeropuerto.log:
        print(f"{entrada[0]} aterrizó en minuto {entrada[1]}")

if __name__ == "__main__":
    simular()
'''

Crear una versión básica del juego de Blackjack.

Requisitos:

Se genera un mazo de 52 cartas (con palos y valores).
Se reparten dos cartas al jugador y dos al crupier (una oculta).
El jugador puede "pedir" (recibir otra carta) o "plantarse".
Si el jugador supera 21, pierde automáticamente (bust).
Una vez que el jugador se planta, el crupier revela su carta 
oculta y pide cartas hasta alcanzar 17 o más.
Se compara el valor de las manos para determinar al ganador 
(se aplican las reglas de Blackjack, considerando que el As vale 11 o 1).

'''

import random

def create_deck():
    """Crea un mazo de 52 cartas (sacos y valores)."""
    palos = ['♠', '♥', '♦', '♣']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [(v, p) for p in palos for v in valores]

def deal_card(deck):
    """Extrae una carta del mazo de forma aleatoria y la elimina."""
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_hand_value(hand):
    """Calcula el valor total de una mano, manejando la flexibilidad del As."""
    value = 0
    aces = 0
    for card in hand:
        v = card[0]
        if v in ['J', 'Q', 'K']:
            value += 10
        elif v == 'A':
            value += 11
            aces += 1
        else:
            value += int(v)
    # Ajustar los As si el total supera 21
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def print_hand(hand, hidden=False):
    """Muestra las cartas de una mano; si hidden=True, oculta la primera carta."""
    if hidden:
        return "[oculta], " + ", ".join(f"{v}{p}" for v, p in hand[1:])
    else:
        return ", ".join(f"{v}{p}" for v, p in hand)

def blackjack():
    deck = create_deck()
    random.shuffle(deck)
    
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    print("¡Bienvenido al Blackjack Simplificado!\n")
    
    # Turno del jugador
    while True:
        player_value = calculate_hand_value(player_hand)
        print(f"Tu mano: {print_hand(player_hand)} (Valor: {player_value})")
        print(f"Mano del crupier: {print_hand(dealer_hand, hidden=True)}")
        
        if player_value > 21:
            print("¡Te pasaste de 21! Pierdes.")
            return
        
        choice = input("¿Quieres [H]it (pedir carta) o [S]tand (plantarte)? ").strip().lower()
        if choice.startswith('h'):
            player_hand.append(deal_card(deck))
        elif choice.startswith('s'):
            break
        else:
            print("Opción no válida, intenta de nuevo.")
    
    # Turno del crupier
    dealer_value = calculate_hand_value(dealer_hand)
    print("\nAhora es el turno del crupier.")
    print(f"Mano del crupier: {print_hand(dealer_hand)} (Valor: {dealer_value})")
    while dealer_value < 17:
        card = deal_card(deck)
        dealer_hand.append(card)
        dealer_value = calculate_hand_value(dealer_hand)
        print(f"El crupier pide: {card[0]}{card[1]} -> Valor total: {dealer_value}")
    
    # Resultados finales
    print("\n--- Resultado Final ---")
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"Tu mano: {print_hand(player_hand)} (Valor: {player_value})")
    print(f"Mano del crupier: {print_hand(dealer_hand)} (Valor: {dealer_value})")
    
    if dealer_value > 21:
        print("¡El crupier se pasó de 21! Ganaste.")
    elif player_value > dealer_value:
        print("¡Ganaste!")
    elif player_value < dealer_value:
        print("Perdiste.")
    else:
        print("Empate.")

if __name__ == "__main__":
    blackjack()

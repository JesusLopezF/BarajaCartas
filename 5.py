"""
Card que simule una carta de naipes. Un naipe tiene un palo (de un conjunto de palos) y un valor (de un conjunto de valores).

CardPlayer que simule un jugador de naipes. Un jugador tiene un conjunto de naipes.
Puede robar una carta de una baraja. Una vez robada el jugador tiene una carta más y la baraja una menos.
Puede deshacerse de una carta.
Puede recibir cartas.

Deck que simula un conjunto de cartas de naipes.
Inicialmente tiene las cartas que le llegan con el constructor.
Puede repartir un conjunto de cartas a un jugador. En la baraja dejan de existir esas cartas.
Le pueden quitar la primera carta (robar).
Puede barajarse.

Baraja Española e Inglesa (SpanishDeck e EnglishDeck) que heredan de Deck.
"""
import random

class Card:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class CardPlayer:
    def __init__(self):
        self.cartas = []

    def robar_carta(self, deck):
        if deck.tiene_cartas():
            carta_robada = deck.robar_carta()
            self.cartas.append(carta_robada)
            print(f"Jugador robó: {carta_robada}")
        else:
            print("No hay más cartas en la baraja")

    def recibir_cartas(self, cartas):
        self.cartas.extend(cartas)

    def deshacerse_de_carta(self, carta):
        if carta in self.cartas:
            self.cartas.remove(carta)
            print(f"Jugador se deshizo de: {carta}")
        else:
            print("La carta no está en la mano del jugador")

class Deck:
    def __init__(self, cartas):
        self.cartas = cartas

    def repartir_cartas(self, jugador, cantidad):
        cartas_repartidas = []
        for i in range(cantidad):
            if self.tiene_cartas():
                carta = self.robar_carta()
                cartas_repartidas.append(carta)
                jugador.recibir_cartas([carta])
            else:
                print("No hay más cartas en la baraja")

        return cartas_repartidas

    def robar_carta(self):
        if self.tiene_cartas():
            carta_robada = self.cartas.pop(0)
            print(f"Se robó la carta: {carta_robada}")
            return carta_robada
        else:
            print("No hay más cartas en la baraja")

    def tiene_cartas(self):
        return len(self.cartas) > 0

    def barajarse(self):
        random.shuffle(self.cartas)

class SpanishDeck(Deck):
    def __init__(self):
        palos = ['Oros', 'Copas', 'Espadas', 'Bastos']
        valores = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']
        cartas_espanolas = []
        for palo in palos:
            for valor in valores:
                carta = Card(palo, valor)
                cartas_espanolas.append(carta)
        super().__init__(cartas_espanolas)

class EnglishDeck(Deck):
    def __init__(self):
        palos = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        cartas_inglesas = []
        for palo in palos:
            for valor in valores:
                carta = Card(palo, valor)
                cartas_inglesas.append(carta)
        super().__init__(cartas_inglesas)

# Ejemplo de uso
jugador = CardPlayer()

# Crear una baraja española
baraja_espanola = SpanishDeck()

# Repartir 5 cartas al jugador
baraja_espanola.repartir_cartas(jugador, 5)

# Mostrar las cartas del jugador
print("Cartas del jugador:", [str(carta) for carta in jugador.cartas])

# Robar una carta de la baraja
jugador.robar_carta(baraja_espanola)

# Deshacerse de una carta
carta_a_deshacer = jugador.cartas[0]
jugador.deshacerse_de_carta(carta_a_deshacer)

# Mostrar las cartas actualizadas del jugador
print("Cartas del jugador después de deshacerse:", [str(carta) for carta in jugador.cartas])

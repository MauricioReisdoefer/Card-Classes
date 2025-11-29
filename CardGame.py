from CardClasses import Store
from CardClasses import Card
from CardClasses import Location
from CardClasses import Player
from CardClasses import Combat

import os

class Game:
    def __init__(self):
        self.cards = self.create_cards()
        self.starter_decks = self.create_starter_decks()
        self.store = Store(self.create_store_cards())
        self.locations = []
        self.create_locations()
        self.player = None

    def create_cards(self):
        return {
            "sword": Card("Espada", "Vence Escudos e Adagas. Perde para Arco e Espada Grande", 5),
            "shield": Card("Escudo", "Vence Adagas e Arcos. Perde para Espada e Espada Grande", 5),
            "bow": Card("Arco", "Vence Espadas e Adagas. Perde para Escudo", 15),
            "greatsword": Card("Espada Grande", "Vence Espadas e Escudos. Perde para Arco", 30)
        }

    def create_starter_decks(self):
        c = self.cards
        return [
            [c["sword"], c["shield"]],
            [c["shield"], c["sword"]]
        ]

    def create_store_cards(self):
        c = self.cards
        return [c["bow"], c["sword"], c["shield"], c["greatsword"]]

    def create_locations(self):
        c = self.cards
        # locais originais
        self.locations.append(Location(
            "Masmorra Sombria", 
            "Carrasco Imaculado",
            [c["sword"], c["shield"]],
            2,
            10
        ))
        self.locations.append(Location(
            "Castelo Sombrio", 
            "Rei Perdido",
            [c["sword"], c["greatsword"]],
            5,
            40
        ))
        self.locations.append(Location(
            "Floresta Negra", 
            "Urso Ancião",
            [c["shield"], c["sword"]],
            3,
            20
        ))

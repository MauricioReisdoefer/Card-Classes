from classes import Store
from classes import Card
from classes import Location
from classes import Player
from classes import Combat

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
    def create_player(self):
            os.system('cls')
            print("Bem-vindo ao Card RPG!")

            while True:
                name = input("Insira seu nome: ")
                if not name.isdigit():
                    break
                print("Nome inválido!")
            
            print("Escolha seu deck inicial:")
            for i, deck in enumerate(self.starter_decks, 1):
                print(f"{i} - {deck}")

            while True:
                choice = input("Deck: ")
                if choice.isdigit() and 1 <= int(choice) <= len(self.starter_decks):
                    chosen_deck = self.starter_decks[int(choice)-1]
                    break
                print("Escolha inválida!")

            self.player = Player(name, chosen_deck)
            print(f"Bem-vindo, {self.player.name}!")
        
    def manage_deck(self):
            while True:
                print("\nGerenciar Deck: LISTAR | DISCARTAR | LOJA | SAIR")
                choice = input("> ").upper()

                if choice == "SAIR":
                    break
                elif choice == "LISTAR":
                    self.player.show_deck()
                elif choice == "DISCARTAR":
                    self.player.show_deck()
                    choice = input("Qual carta descartar? ")
                    if choice.isdigit():
                        idx = int(choice)-1
                        if 0 <= idx < len(self.player.deck.cards):
                            card = self.player.deck.remove_card(idx)
                            print(f"Você recebeu {card.price} coins.")
                            self.player.coins += card.price
                elif choice == "LOJA":
                    self.store.show()
                    buy = input("Comprar qual carta? (numero ou SAIR): ").upper()
                    if buy.isdigit():
                        index = int(buy)-1
                        if 0 <= index < len(self.store.cards):
                            self.player.buy_card(self.store, index)

    def choose_location(self):
            print("\nLocais disponíveis:")
            for i, loc in enumerate(self.locations, 1):
                print(f"{i} - {loc.name}")

            while True:
                choice = input("Escolha o local: ")
                if choice.isdigit() and 1 <= int(choice) <= len(self.locations):
                    return self.locations[int(choice)-1]
                print("Escolha inválida!")

    def start_location(self):
            location = self.choose_location()
            combat = Combat(self.player, location)
            combat.start()

    def start(self):
            self.create_player()

            while True:
                print("\nEscolha: GERENCIAR | AVENTURA | SAIR")
                choice = input("> ").upper()

                if choice == "GERENCIAR":
                    self.manage_deck()
                elif choice == "AVENTURA":
                    self.start_location()
                elif choice == "SAIR":
                    break

game = Game()
game.start()
from .deck import Deck

class Player:
    def __init__(self, name, starting_deck):
        self.name = name 
        self.deck = Deck(starting_deck) 
        self.coins = 15 
        self.health = 4

    def show_deck(self):
        print("Seu Deck:")
        for i, card in enumerate(self.deck.cards, 1):
            print(f"{i} - {card}")

    def buy_card(self, store, index): 
        card = store.cards[index] 
        if self.deck.is_full(): 
            print("Inventário cheio!")
            return False 

        if self.coins >= card.price:
            self.coins -= card.price
            self.deck.add_card(card)
            print(f"Você comprou {card.name}")
            return True
        else:
            print("Coins insuficientes!")
            return False
class Deck:
    def __init__(self, cards=None): 
        self.cards = cards if cards else [] 

    def add_card(self, card): 
        self.cards.append(card)

    def remove_card(self, index):
        return self.cards.pop(index)

    def is_full(self): 
        return len(self.cards) >= 3

    def __repr__(self):
        return f"{self.cards}"

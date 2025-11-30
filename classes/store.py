class Store: 
    def __init__(self, cards): 
        self.cards = cards 

    def show(self):
        print("|   CARTA   |   FUNÇÃO   |   PREÇO   | ")
        for i, card in enumerate(self.cards, 1): 
            print(f"{i} - {card}")
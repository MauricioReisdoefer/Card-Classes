class Card:
    def __init__(self, name, effect, price):
        self.name = name 
        self.effect = effect 
        self.price = price 

    def __repr__(self):
        return f"{self.name} | {self.effect} | {self.price} coins"

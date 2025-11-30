class Location: 
    def __init__(self, name, enemy_name, enemy_deck, enemy_life, reward):
        self.name = name
        self.enemy_name = enemy_name 
        self.enemy_deck = enemy_deck 
        self.enemy_life = enemy_life 
        self.reward = reward 

    def __repr__(self):
        return f"{self.name}"
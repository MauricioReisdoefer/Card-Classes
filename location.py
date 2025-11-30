class Location: ## classe das localizações de onde o player pode ir
    def __init__(self, name, enemy_name, enemy_deck, enemy_life, reward):
        self.name = name # nome
        self.enemy_name = enemy_name # nome do inimigo da area
        self.enemy_deck = enemy_deck # deck do bixo
        self.enemy_life = enemy_life # vida do bixo
        self.reward = reward # recompensa por vencer o bixo

    def __repr__(self): # retorna uma string mutcho loka com o nome da area
        return f"{self.name}"
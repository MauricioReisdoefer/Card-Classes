import os
import random

class Combat:
    def __init__(self, player, location):
        self.player = player 
        self.enemy_name = location.enemy_name 
        self.enemy_life = location.enemy_life
        self.enemy_deck = location.enemy_deck
        self.reward = location.reward
        self.player_life = player.health

    def show_scene(self, pa, ea):
        os.system('cls')
        print(f"| VIDA: {self.player_life} | vs | {self.enemy_life} :VIDA |")
        print(f"Sua ação: {pa} | Ação inimiga: {ea}")

    def get_player_action(self): 
        self.player.show_deck()
        while True: 
            choice = input("Escolha sua carta: ") 
            if choice.isdigit() and 1 <= int(choice) <= len(self.player.deck.cards):
                return self.player.deck.cards[int(choice)-1].name 
            print("Escolha inválida!")

    def get_enemy_action(self):
        return random.choice(self.enemy_deck).name 
    
    def resolve_round(self, action1, action2): 
        win_map = { 
            "Espada": ["Escudo"],
            "Escudo": ["Arco"],
            "Arco": ["Espada", "Espada Grande"],
            "Espada Grande": ["Espada", "Escudo"]
        }

        if action1 == action2:
            print("Empate!")
            return

        if action2 in win_map.get(action1, []):
            self.enemy_life -= 1
            print("Você venceu a rodada!")
        else: 
            self.player_life -= 1 
            print("Você perdeu a rodada!")

    def start(self):
        print(f"Você entrou em combate contra {self.enemy_name}!")

        while self.player_life > 0 and self.enemy_life > 0:
            pa = self.get_player_action()
            ea = self.get_enemy_action()

            self.show_scene(pa, ea)
            self.resolve_round(pa, ea)

        if self.enemy_life <= 0:
            print("Você derrotou o inimigo!")
            print(f"Recompensa: {self.reward} coins")
            self.player.coins += self.reward
        else:
            print("Você morreu...")
            exit()

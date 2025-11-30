import os
import random

class Combat: ## SISTEMA DE COMBATEEE!
    def __init__(self, player, location): # pede o player e a localização | Area
        self.player = player # player
        self.enemy_name = location.enemy_name # pega as informaçoes do inimigo
        self.enemy_life = location.enemy_life
        self.enemy_deck = location.enemy_deck
        self.reward = location.reward
        self.player_life = player.health

    def show_scene(self, pa, ea): # mostra a cena e limpa o terminal
        ## pa = playerAction | ea EnemyAction
        os.system('cls')
        print(f"| VIDA: {self.player_life} | vs | {self.enemy_life} :VIDA |") ## cria um display no terminal
        print(f"Sua ação: {pa} | Ação inimiga: {ea}")

    def get_player_action(self): ## pega a ação do jogador
        self.player.show_deck() ## mostra o deck do jogador
        while True: ## looping enquanto a batalha durar
            choice = input("Escolha sua carta: ") # input de escolha de carta
            if choice.isdigit() and 1 <= int(choice) <= len(self.player.deck.cards): # verificação de integridade da escolha
                return self.player.deck.cards[int(choice)-1].name 
            print("Escolha inválida!")

    def get_enemy_action(self): ## ação do inimigo
        return random.choice(self.enemy_deck).name #aleatoriza a carta do inimigo e retorna o nome da messsssssssma carta!

    def resolve_round(self, action1, action2): #calculo de batalha
        win_map = { # basicamente é o mesmo calculo que acontece no pedrao papeu tesoura, exemplo:
            # papel vence de? Pedra!
            "Espada": ["Escudo"],
            "Escudo": ["Arco"],
            "Arco": ["Espada", "Espada Grande"],
            "Espada Grande": ["Espada", "Escudo"]
        }

        # ve se eles fizeram a mesma coisa
        if action1 == action2:
            print("Empate!")
            return

        # ve se a carta do inimigo (action2) esta na lista de derrotadas pela carta do jogador (action1).
        if action2 in win_map.get(action1, []):
            self.enemy_life -= 1 # voce da um de dano no inimigo
            print("Você venceu a rodada!")
        else: ## caso contraaario :D
            self.player_life -= 1 # inimigo da 1 de dano no jogador
            print("Você perdeu a rodada!")

    def start(self): # inicia a batalha
        print(f"Você entrou em combate contra {self.enemy_name}!") # texto inicial

        while self.player_life > 0 and self.enemy_life > 0: # repete enquanto os dois estiverem vivos
            pa = self.get_player_action() # pega ação do jogador
            ea = self.get_enemy_action() # pega ação do inimigo

            # mostra a cena e calcula seu resultado
            self.show_scene(pa, ea)
            self.resolve_round(pa, ea)

        ## conclusao da batalha com a verificação de resultado
        if self.enemy_life <= 0:
            print("Você derrotou o inimigo!")
            print(f"Recompensa: {self.reward} coins")
            self.player.coins += self.reward
        else:
            print("Você morreu...")
            exit()

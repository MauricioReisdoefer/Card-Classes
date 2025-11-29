import os
import random

#  CLASSES BASES  #

#classe que sera herdada pelos objetos cartas

class Card:
    def __init__(self, name, effect, price):
        self.name = name # nome
        self.effect = effect # efeito
        self.price = price # preço

    def __repr__(self):
        return f"{self.name} | {self.effect} | {self.price} coins"
    # retorna uma string mutcho loka, (eu acho).

# classe de gerenciamento dos baralhos

class Deck:
    def __init__(self, cards=None): # inicia :)  / permite iniciar o deck ja com cartas ou vazio.
        self.cards = cards if cards else [] # se ele mandou o valor de cards, entao ele vai usar o valor de cards, caso nao. recebe lista vaziaaaaaa!

    def add_card(self, card): ## adiciona cartas ao baralho
        self.cards.append(card)

    def remove_card(self, index): #retira a cartas do baraio
        return self.cards.pop(index)

    def is_full(self): # vereifica se ta cheio ou nao, retornando uma bool (true or false miojo :)
        return len(self.cards) >= 3

    def __repr__(self): # retorna string mutch loka que é imprimida
        return f"{self.cards}"


class Player: # classe do jogador
    def __init__(self, name, starting_deck):
        self.name = name # seu nome
        self.deck = Deck(starting_deck) # o deck que ele recebe é o inicial
        self.coins = 15 # denero
        self.health = 4 # vida

    def show_deck(self): # isso faz com que ele mostre os itens do deck dele de forma numerada
        print("Seu Deck:")
        for i, card in enumerate(self.deck.cards, 1): ## for que busca todos os itens dentro de cards.
            print(f"{i} - {card}")

    ## escrever a documentação dessa forma talvez de problema.

    def buy_card(self, store, index): # compra cartas
        card = store.cards[index] # card, no caso, a carta escolhida na posição definida pelo index
        if self.deck.is_full(): # verifica se o deck do jogador ta chei
            print("Inventário cheio!")
            return False 

        if self.coins >= card.price: # se tiver dinhheiro o suficiente
            self.coins -= card.price ## remove o custo da carta do denero do jogador
            self.deck.add_card(card) # adiciona ela ao seu deck
            print(f"Você comprou {card.name}")
            return True
        else:
            print("Coins insuficientes!")
            return False


class Store: ## loja!!!
    def __init__(self, cards): 
        self.cards = cards ## cartas do jogador

    def show(self): ## mostra as cartas disponiveis e um display bacanudo
        print("|   CARTA   |   FUNÇÃO   |   PREÇO   | ")
        for i, card in enumerate(self.cards, 1): # for que busca cartas disponiveis pra venda na loja
            print(f"{i} - {card}")

#  SISTEMA DE LOCAIS  #

class Location: ## classe das localizações de onde o player pode ir
    def __init__(self, name, enemy_name, enemy_deck, enemy_life, reward):
        self.name = name # nome
        self.enemy_name = enemy_name # nome do inimigo da area
        self.enemy_deck = enemy_deck # deck do bixo
        self.enemy_life = enemy_life # vida do bixo
        self.reward = reward # recompensa por vencer o bixo

    def __repr__(self): # retorna uma string mutcho loka com o nome da area
        return f"{self.name}"


#  SISTEMA DE COMBATE DAHORA  #


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

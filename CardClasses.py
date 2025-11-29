import os
import random

#  CLASSES BASES  #

class Card:
    def __init__(self, name, effect, price):
        self.name = name
        self.effect = effect
        self.price = price

    def __repr__(self):
        return f"{self.name} | {self.effect} | {self.price} coins"


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


class Store:
    def __init__(self, cards):
        self.cards = cards

    def show(self):
        print("|   CARTA   |   FUNÇÃO   |   PREÇO   | ")
        for i, card in enumerate(self.cards, 1):
            print(f"{i} - {card}")

#  SISTEMA DE LOCAIS  #

class Location:
    def __init__(self, name, enemy_name, enemy_deck, enemy_life, reward):
        self.name = name
        self.enemy_name = enemy_name
        self.enemy_deck = enemy_deck
        self.enemy_life = enemy_life
        self.reward = reward

    def __repr__(self):
        return f"{self.name}"


#  SISTEMA DE COMBATE DAHORA  #


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

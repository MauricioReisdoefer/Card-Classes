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
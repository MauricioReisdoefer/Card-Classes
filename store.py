class Store: ## loja!!!
    def __init__(self, cards): 
        self.cards = cards ## cartas do jogador

    def show(self): ## mostra as cartas disponiveis e um display bacanudo
        print("|   CARTA   |   FUNÇÃO   |   PREÇO   | ")
        for i, card in enumerate(self.cards, 1): # for que busca cartas disponiveis pra venda na loja
            print(f"{i} - {card}")
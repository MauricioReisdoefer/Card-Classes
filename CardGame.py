## IMPORT DAS CLASSES CRIADAS NO CADRCLASSES.PY ##

from CardClasses import Store
from CardClasses import Card
from CardClasses import Location
from CardClasses import Player
from CardClasses import Combat

## SISTEMA OPERACIONAL PARA MEXER NO TERMINAL :)
import os

## CLASSE GAME, CONTROLA TODO O FLUXO DE GAMEPLAY LEGAL ##

class Game: ## cria classe controladora do jogo :)
    
    def __init__(self):
        self.cards = self.create_cards() 
        self.starter_decks = self.create_starter_decks()
        self.store = Store(self.create_store_cards())
        self.locations = []
        self.create_locations()
        self.player = None

    ## retorna as cartas disponiveis no jogo, com suas caracteristicas respectivas aos atributos da classe.
    def create_cards(self):
        return {
            "sword": Card("Espada", "Vence Escudos e Adagas. Perde para Arco e Espada Grande", 5),
            "shield": Card("Escudo", "Vence Adagas e Arcos. Perde para Espada e Espada Grande", 5),
            "bow": Card("Arco", "Vence Espadas e Adagas. Perde para Escudo", 15),
            "greatsword": Card("Espada Grande", "Vence Espadas e Escudos. Perde para Arco", 30)
        }

    ## cria os baralhos iniciais, sendo eles cada um uma lista.
    def create_starter_decks(self): 
        c = self.cards 
        return [
            [c["sword"], c["shield"]],
            [c["shield"], c["sword"]]
        ]

    ## Cartas disponiveis para a compra. retorna uma lista dos itens
    def create_store_cards(self):
        c = self.cards
        return [c["bow"], c["sword"], c["shield"], c["greatsword"]]

    ## cria as localizaçoes, passando os atributos da classe LOCATION.
    def create_locations(self):
        c = self.cards
        ## locais originais ##
        self.locations.append(Location( ## local da masmorra
            "Masmorra Sombria",  
            "Carrasco Imaculado", # inimigo da area
            [c["sword"], c["shield"]], ## armas do inimigo
            2, # vida do inimigo
            10# recompensa
        ))
        self.locations.append(Location( ## local de castelo
            "Castelo Sombrio", 
            "Rei Perdido", # inimigo da area
            [c["sword"], c["greatsword"]], ## armas do inimigo
            5, # vida do inimigo
            40# recompensa
        ))
        self.locations.append(Location( ## local da floresta
            "Floresta Negra", 
            "Urso Ancião", # inimigo da area
            [c["shield"], c["sword"]], ## urso com escudo e espada maneiro.
            3, # vida do inimigo
            20 # recompensa
        ))

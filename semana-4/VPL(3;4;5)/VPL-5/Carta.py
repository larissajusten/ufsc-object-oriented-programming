from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        pass#implementar

    '''
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    '''
    def valor_total_carta(self) -> int:
        pass#implementar

    @property
    def personagem(self) -> Personagem:
        pass#implementar

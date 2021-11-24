from AbstractMesa import *


class Mesa(AbstractMesa):

    #Construtor fornecido, nao deve ser alterado
    def __init__(self, jogador1: Jogador, jogador2: Jogador,
                 cartaJogador1: Carta, cartaJogador2: Carta):
        pass#implementar

    @property
    def jogador1(self) -> Jogador:
        pass#implementar

    @property
    def jogador2(self) -> Jogador:
        pass#implementar

    @property
    def carta_jogador1(self) -> Carta:
        pass#implementar

    @property
    def carta_jogador2(self) -> Carta:
        pass#implementar

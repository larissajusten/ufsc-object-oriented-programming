from abc import ABC, abstractmethod
from Carta import *


class AbstractJogador(ABC):

    '''
    Retorna o nome do jogador
    @return nome do jogador
    '''
    @property
    @abstractmethod
    def nome(self) -> str:
        pass

    '''
    Retira uma das cartas do Jogador. Esta operacao eh utilizada para realizar uma jogada (baixar uma carta na mesa)
    A carta sai da mao (ou seja, a carta sai da lista das cartas que o jogador possui)
    @return Retorna a Carta que foi retirada da mao do jogador (lista das cartas que ele possui)
    '''
    @abstractmethod
    def baixa_carta_da_mao(self):
        pass

    '''
    @return Retorna a mao atual do jogador (lista das cartas que ele possui)
    '''
    @property
    @abstractmethod
    def mao(self) -> list:
        pass

    '''
    Inclui na mao do jogador a carta passada como parametro
    @param carta Carta que sera incluida na mao do jogador
    '''
    @abstractmethod
    def inclui_carta_na_mao(self, carta: Carta):
        pass

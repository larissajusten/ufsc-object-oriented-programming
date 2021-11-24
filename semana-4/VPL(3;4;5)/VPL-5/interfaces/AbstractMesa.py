from abc import ABC, abstractmethod
from Carta import *
from Jogador import *


class AbstractMesa(ABC):

    '''
    Retorna o Jogador 1
    @return o Jogador 1
    '''
    @property
    @abstractmethod
    def jogador1(self) -> Jogador:
        pass

    '''
    Retorna o Jogador 2
    @return o Jogador 2
    '''
    @property
    @abstractmethod
    def jogador2(self) -> Jogador:
        pass

    '''
    Retorna a carta que o jogador 1 baixou
    @return carta do jogador 1
    '''
    @property
    @abstractmethod
    def carta_jogador1(self) -> Carta:
        pass

    '''
    Retorna a carta que o jogador 2 baixou
    @return carta do jogador 2
    '''
    @property
    @abstractmethod
    def carta_jogador2(self) -> Carta:
        pass

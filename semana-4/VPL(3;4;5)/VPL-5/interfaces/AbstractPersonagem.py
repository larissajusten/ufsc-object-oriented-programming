from abc import ABC, abstractmethod
from enum import Enum


class Tipo(Enum):
    agua = 0
    terra = 1
    ar = 2
    fogo = 3


class AbstractPersonagem(ABC):

    '''
    @return Retorna o tipo do personagem
    '''
    @property
    @abstractmethod
    def tipo(self) -> Tipo:
        pass

    '''
    @return Retorna a energia do personagem
    '''
    @property
    @abstractmethod
    def energia(self) -> int:
        pass

    '''
    @return Retorna a habilidade do personagem
    '''
    @property
    @abstractmethod
    def habilidade(self) -> int:
        pass

    '''
    @return Retorna a velocidade do personagem
    '''
    @property
    @abstractmethod
    def velocidade(self) -> int:
        pass

    '''
    @return Retorna a resistencia do personagem
    '''
    @property
    @abstractmethod
    def resistencia(self) -> int:
        pass

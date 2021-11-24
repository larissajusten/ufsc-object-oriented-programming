from abc import ABC, abstractmethod
from Personagem import *


class AbstractCarta(ABC):

    '''
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    '''
    @abstractmethod
    def valor_total_carta(self) -> int:
        pass

    '''
    Retorna para o personagem da carta
    @return personagem da carta
    '''
    @property
    @abstractmethod
    def personagem(self) -> Personagem:
        pass

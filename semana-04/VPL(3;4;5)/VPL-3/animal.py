from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, tamanho_passo: int):
        self.__tamanho_passo = tamanho_passo

    @property
    def tamanho_passo(self):
        return self.__tamanho_passo

    @tamanho_passo.setter
    def tamanho_passo(self, tamanho_passo):
        self.__tamanho_passo = tamanho_passo

    @abstractmethod
    def produzir_som(self):
        pass

    def mover(self):
        return f'ANIMAL: DESLOCOU {self.tamanho_passo}'

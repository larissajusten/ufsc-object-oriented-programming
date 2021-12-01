from abc import ABC, abstractmethod
from animal import Animal


class Ave(Animal):
    def __init__(self, tamanho_passo, altura_voo):
        super().__init__(tamanho_passo)
        self.__altura_voo = altura_voo

    @property
    def altura_voo(self):
        return self.__altura_voo

    @altura_voo.setter
    def altura_voo(self, altura_voo):
        self.__altura_voo = altura_voo

    @abstractmethod
    def produzir_som(self):
        pass

    def mover(self):
        return f'ANIMAL: DESLOCOU {self.tamanho_passo} VOANDO'

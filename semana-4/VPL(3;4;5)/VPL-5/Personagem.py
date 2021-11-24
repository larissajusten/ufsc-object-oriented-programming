from AbstractPersonagem import *


class Personagem(AbstractPersonagem):
    #Construtor fornecido, nao deve ser alterado
    def __init__(self, energia: int, habilidade: int,
                 velocidade: int, resistencia: int, tipo: Tipo):
        pass#implementar

    @property
    def tipo(self) -> Tipo:
        pass#implementar

    @property
    def energia(self) -> int:
        pass#implementar

    @property
    def habilidade(self) -> int:
        pass#implementar

    @property
    def velocidade(self) -> int:
        pass#implementar

    @property
    def resistencia(self) -> int:
        pass#implementar

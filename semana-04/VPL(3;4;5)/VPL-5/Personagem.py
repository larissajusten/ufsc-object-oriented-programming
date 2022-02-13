from AbstractPersonagem import *


class Personagem(AbstractPersonagem):
    def __init__(self, energia: int, habilidade: int,
                 velocidade: int, resistencia: int, tipo: Tipo):
        self.__energia = energia
        self.__habilidade = habilidade
        self.__velocidade = velocidade
        self.__resistencia = resistencia
        self.__tipo = tipo

    @property
    def tipo(self) -> Tipo:
        return self.__tipo

    @property
    def energia(self) -> int:
        return self.__energia

    @property
    def habilidade(self) -> int:
        return self.__habilidade

    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @property
    def resistencia(self) -> int:
        return self.__resistencia

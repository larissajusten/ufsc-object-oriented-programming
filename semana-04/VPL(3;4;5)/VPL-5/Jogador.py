from abc import ABC, abstractmethod
from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):
    def __init__(self, nome: str):
        self.__nome = nome
        self.__cartas = []

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def mao(self) -> list:
        return self.__cartas

    def baixa_carta_da_mao(self) -> Carta:
        return self.__cartas.pop()

    def remove_carta_da_mao(self, carta: Carta) -> Carta:
        return self.__cartas.remove(carta)

    def inclui_carta_na_mao(self, carta: Carta):
        if isinstance(carta, Carta):
            self.__cartas.append(carta)

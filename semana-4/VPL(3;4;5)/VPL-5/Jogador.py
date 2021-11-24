from abc import ABC, abstractmethod
from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):

    def __init__(self, nome: str):
        pass#implementar

    '''
    @return Retorna o nome do jogador
    '''
    @property
    def nome(self) -> str:
        pass#implementar

    '''
    Retira uma das cartas do Jogador. Esta operacao eh utilizada para realizar uma jogada (baixar uma carta na mesa)
    A carta sai da mao (ou seja, a carta sai da lista das cartas que o jogador possui)
    @return Retorna a Carta que foi retirada da mao do jogador (lista das cartas que ele possui)
    '''
    def baixa_carta_da_mao(self) -> Carta:
        pass#implementar

    '''
    @return Retorna a mao atual do jogador (lista das cartas que ele possui)
    '''
    @property
    def mao(self) -> list:
        pass#implementar

    '''
    Inclui na mao do jogador a carta passada como parametro
    @param carta Carta que sera incluida na mao do jogador
    '''
    def inclui_carta_na_mao(self, carta:Carta):
        pass#implementar

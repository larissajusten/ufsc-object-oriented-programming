from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagens = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagens

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        existe_personagem = next((personagem for personagem in self.personagens
                                  if personagem.tipo == tipo), False)
        if not existe_personagem:
            novo_personagem = Personagem(
                energia, habilidade, velocidade, resistencia, tipo)
            self.__personagens.append(novo_personagem)
            return novo_personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        existe_carta = next((carta for carta in self.baralho
                            if carta.personagem == personagem), False)
        if not existe_carta:
            novo_carta = Carta(personagem)
            self.__baralho.append(novo_carta)
            return novo_carta

    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador):
        indexs = random.sample(range(0, len(self.__baralho)-1), 3)
        self.__preencher_jogador(indexs[:4], jogador1)
        self.__preencher_jogador(indexs[5:], jogador2)

    def __preencher_jogador(index_valores, jogador):
        if isinstance(jogador, Jogador):
            for i in index_valores:
                jogador.inclui_carta_na_mao(self.baralho[i])

    def jogada(self, mesa: Mesa) -> Jogador:
        compacao_jogadores = mesa.cartaJogador1.valor_total_carta - \
            mesa.cartaJogador2.valor_total_carta
        if compacao_jogadores == 0:
            mesa.jogador1.inclui_carta_na_mao(
                mesa.cartaJogador1.valor_total_carta)
            mesa.jogador2.inclui_carta_na_mao(
                mesa.cartaJogador2.valor_total_carta)
            return None
        elif compacao_jogadores < 0:
            mesa.jogador2.inclui_carta_na_mao(
                mesa.cartaJogador1.valor_total_carta)
            mesa.jogador2.inclui_carta_na_mao(
                mesa.cartaJogador2.valor_total_carta)
            mesa.jogador1.remove_carta_da_mao(mesa.cartaJogador1)
            return mesa.jogador2
        else:
            mesa.jogador1.inclui_carta_na_mao(
                mesa.cartaJogador1.valor_total_carta)
            mesa.jogador1.inclui_carta_na_mao(
                mesa.cartaJogador2.valor_total_carta)
            mesa.jogador2.remove_carta_da_mao(mesa.cartaJogador2)
            return mesa.jogador1

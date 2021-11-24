from abc import ABC, abstractmethod
from Carta import *
from Personagem import *
from Jogador import *
from Mesa import *


class AbstractControladorJogo(ABC):
    '''
    Retorna a lista de personagems
    @return a lista de personagems
    '''
    @property
    @abstractmethod
    def personagems(self) -> list:
        pass

    '''
    Retorna o baralho
    @return o baralho
    '''
    @property
    @abstractmethod
    def baralho(self) -> list:
        pass

    '''
     Permite incluir um novo Personagem na lista de personagens do jogo
     @param energia Energia do novo Personagem
     @param habilidade Habilidade do novo Personagem
     @param velocidade Velocidade do novo Personagem
     @param resistencia Resistencia do novo Personagem
     @param tipo TipoPersonagem (Enum) do novo Personagem.
     Deve ser utilizado TipoPersonagem.TIPO
     @return Retorna o Personagem incluido na lista
    '''
    @abstractmethod
    def inclui_personagem_na_lista(self, energia: int, habilidade: int,
                                velocidade: int, resistencia: int,
                                tipo: Tipo) -> Personagem:
        pass

    '''
     Permite incluir uma nova Carta no baralho do jogo
     @param personagem Personagem da nova carta que sera incluida
     @return Retorna a Carta que foi incluida no baralho
    '''
    @abstractmethod
    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        pass

    '''
     Realiza uma jogada, ou seja:
     1. Recebe a mesa onde estao as cartas lancadas pelo Jogador 1
     e pelo Jogador 2
     2. Compara os valores totais das cartas dos jogadores que estao
     na mesa
     3. Apos comparacao:

     O jogador que ganhar a rodada recebe a carta do jogador perdedor
     sendo assim ele deve chamar o metodo inclui_carta_na_mao para as
     duas cartas que estao na mesa

     Caso ocorra empate ambos os jogadores devem chamar o metodo
     inclui_carta_na_mao com suas respectivas cartas da mesa

     4.Ao final do metodo o jogador que estiver com a mao vazia
     perde o jogo, caso ambos ainda tenham cartas na mao retorne
     None para indicar que por enquanto ninguem venceu o jogo.

     @param mesa Mesa atual, contendo: Jogador 1, Jogador 2,
     Carta do Jogador 1 e Carta do Jogador 2
     @return Retorna o Jogador vencedor da rodada.
     Caso ocorra empate entre os jogadores, retorna None
    '''
    @abstractmethod
    def jogada(self, mesa: Mesa) -> Jogador:
        pass

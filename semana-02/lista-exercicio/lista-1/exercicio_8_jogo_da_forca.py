"""
    Reimplemente o jogo da forca completamente orientado a objetos
"""
import os
import random

palavras = [
    'museu', 'casa', 'aviao', 'computador',
    'Alan Turing', 'notebook', 'impressora',
    'mouse', 'teclado', 'celular', 'controle',
    'fone de ouvido', 'tesoura', 'caneta', 'mouse pad',
    'sofa', 'alcool em gel', 'covid', 'pendrive'
]

class Jogador:
    def __init__(self, vidas: int) -> None:
        self.__vidas = vidas

    @property
    def vidas(self):
        return self.__vidas

    @vidas.setter
    def vidas(self, novo_numero_vidas):
        self.__vidas = novo_numero_vidas

    def DiminuirVida(self, vidas_perdidas):
        vidas_restantes = self.vidas - vidas_perdidas
        self.vidas = vidas_restantes
        return vidas_restantes

    def PrintarVidas(self):
        print(f'# Você tem {self.vidas} vidas')

class Forca:
    def __init__(self, palavra: str) -> None:
        self.__palavra = palavra.lower()
        self.__letras_usadas = []

    @property
    def palavra(self):
        return self.__palavra

    @property
    def letras_usadas(self):
        return self.__letras_usadas

    @palavra.setter
    def palavra(self, nova_palavra):
        self.__palavra = nova_palavra.lower()
        
    @letras_usadas.setter
    def letras_usadas(self, letras_usadas):
        self.__letras_usadas = letras_usadas

    def PrintarPalavra(self):
        print('# Palavra: ', end='')
        for i in self.palavra:
            if i in self.letras_usadas:
                print(f'{i}', end='')
            elif not i.isalpha():
                print(f'{i}', end='')
            else:
                print(' _', end='')
        print('')

    def PrintarLetrasUsadas(self):
        print('# Letras ja digitadas: [', end='')
        for i in self.letras_usadas:
            print(i, end=', ')
        print(']')

    def PrintarForca(self, vidas):
        if vidas == 6:
            print('            ______         ')
            print('           /      |        ')
            print('           |               ')
            print('           |               ')
            print('           |               ')
            print('           |               ')
            print('                           ')

        elif vidas == 5:
            print('            ______         ')
            print('           /      |        ')
            print('           |      O        ')
            print('           |               ')
            print('           |               ')
            print('           |               ')
            print('                           ')

        elif vidas == 4:
            print('            ______         ')
            print('           /      |        ')
            print('           |      O        ')
            print('           |      I        ')
            print('           |      I        ')
            print('           |               ')
            print('                           ')

        elif vidas == 3:
            print('            ______         ')
            print('           /      |        ')
            print('           |      O        ')
            print('           |    / I        ')
            print('           |      I        ')
            print('           |               ')
            print('                           ')

        elif vidas == 2:
            print('            ______         ')
            print('           /      |        ')
            print('           |      O        ')
            print('           |    / I \      ')
            print('           |      I        ')
            print('           |               ')
            print('                           ')

        elif vidas == 1:
            print('            ______         ')
            print('           /      |        ')
            print('           |      O        ')
            print('           |    / I \      ')
            print('           |      I        ')
            print('           |    /          ')
            print('                           ')

        elif vidas == 0:
            print('            ______         ')
            print('           /      |        ')
            print('           |      O        ')
            print('           |    / I \      ')
            print('           |      I        ')
            print('           |    /   \      ')
            print('                           ')
    
    def AdicionaNovaPalavra(self, nova_palavra):
        self.palavra = nova_palavra
        self.letras_usadas = []

    def AdicionaNovaLetraUsada(self, nova_letra_usada):
        self.__letras_usadas.append(nova_letra_usada)

    def CheckPalavraInLetrasUsadas(self):
        palavra = self.__palavra.replace(" ", "")
        numero = [1 for letra in palavra if letra in self.letras_usadas]
        return sum(numero) == len(palavra)

    def CheckLetraInLetrasUsadas(self, letra):
        return letra in self.letras_usadas
    
    def CheckLetraInPalavra(self, letra):
        return letra in self.palavra

class Jogo:
    def __init__(self) -> None:
        self.__forca = None
        self.__jogador = None

    @property
    def forca(self):
        return self.__forca

    @property
    def jogador(self):
        return self.__jogador
    
    @forca.setter
    def forca(self, forca):
        self.__forca = forca

    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador

    def DigitarLetra(self):
        print('')
        letra = input('> Digite uma letra: ')[0].lower()
        if letra.isalpha() and not self.forca.CheckPalavraInLetrasUsadas() and self.jogador.vidas > 0:
            if self.forca.CheckLetraInPalavra(letra) and not self.forca.CheckLetraInLetrasUsadas(letra):
                self.forca.AdicionaNovaLetraUsada(letra)
            elif self.forca.CheckLetraInLetrasUsadas(letra):
                print('# Letra ja utilizada!')
                self.DigitarLetra()
            else:
                self.forca.AdicionaNovaLetraUsada(letra)
                self.jogador.DiminuirVida(1)
        else:
            print('# Caracter invalido!')
            self.DigitarLetra()

    def PrintarInformacoes(self):
        print('# FORCA')
        self.forca.PrintarForca(self.jogador.vidas)
        self.forca.PrintarPalavra()
        self.forca.PrintarLetrasUsadas()
        self.jogador.PrintarVidas()

    def DinamicaJogo(self):
        self.PrintarInformacoes()
        self.DigitarLetra()

    def TentarNovamente(self):
        escolha = input('# Deseja tentar novamente: [S/N] ')
        if escolha == 's':
            self.IniciarJogo()
        if escolha == 'n':
            return None
        else:
            self.TentarNovamente()

    def IniciarJogo(self):
        index_palavra_aleatoria = random.randint(0, len(palavras)-1)
        self.forca = Forca(palavras[index_palavra_aleatoria])
        self.jogador = Jogador(6)

        while not self.forca.CheckPalavraInLetrasUsadas() and self.jogador.vidas > 0:
            self.DinamicaJogo()
        self.PrintarInformacoes()

        print('')
        if self.jogador.vidas == 0:
            print('# Acabaram suas vidas!')
            self.TentarNovamente()
        else:
            print('# Parabens! Voce ganhou o jogo!')
            self.TentarNovamente()

def main():
    print('# Exercicio 8 - Jogo da Forca')
    jogo = Jogo()
    jogo.IniciarJogo()

if __name__ == '__main__':
    main()

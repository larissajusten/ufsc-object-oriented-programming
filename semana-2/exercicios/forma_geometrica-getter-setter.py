"""
  Considere a seguinte solução do exercício das formas geométricas proposto na Notebook 1-Objetos e Classes. 
  Note que se fosse necessário obter a área de uma figura várias vezes no decorrer do programa, não seria necessário recalcular a área toda vez, 
    bastaria criar um atributo __area que seria inicializado com o valor correto no momento da construção do objeto. 
  Implemente esta modificação e os conceitos de encapsulamento no seu programa, respondendo às seguintes questões:

  - Por quê o atributo __area deve ser privado?
  - Quais outros atributos devem ser privados?
  - O método area() será usado apenas para iniciar o atributo __area e, portanto, pode ser um método privado. Você sabe como fazer isso?
  - Acrescente ao seu programa as funcionalidades de perímetro, diâmetro e diagonal.
"""

import math
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    @abstractmethod
    def __calc_area(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass


class Quadrado(FormaGeometrica):
    def __init__(self, lado: float):
        self.__lado = lado
        self.__area = self._FormaGeometrica__calc_area()

    @property
    def lado(self):
        return self.__lado

    @property
    def area(self):
        return self.__area
    
    def _FormaGeometrica__calc_area(self): 
        return math.pow(self.lado, 2)
    


class Retangulo(FormaGeometrica):
    def __init__(self, base: float, altura: float):
        self.__base = base
        self.__altura = altura
        self.__area = self._FormaGeometrica__calc_area()

    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura

    @property
    def area(self):
        return self.__area
    
    def _FormaGeometrica__calc_area(self): 
        return self.base * self.altura


class Circulo(FormaGeometrica):
    def __init__(self, raio: float):
        self.__raio = raio
        self.__area = self._FormaGeometrica__calc_area()

    @property
    def raio(self):
        return self.__raio

    @property
    def area(self):
        return self.__area

    def _FormaGeometrica__calc_area(self): 
        return math.pi * math.pow(self.raio, 2)


def main():
    tipo = input('Digite a figura:')
    fig = None
    
    if tipo == 'quadrado':
        lado = float(input('Digite o lado do quadrado: '))
        fig = Quadrado(lado)
    elif tipo == 'retangulo':
        base = float(input('Digite a base do retangulo: '))
        altura = float(input('Digite a altura do retangulo: '))
        fig = Retangulo(base, altura)
    elif tipo == 'circulo':
        raio = float(input('Digite o raio do circulo: '))
        fig = Circulo(raio)
    
    print('Area do', tipo, ':', fig.area)

main()
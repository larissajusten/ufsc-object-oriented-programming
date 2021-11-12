"""
  Faça um programa que leia uma string s indicando um tipo de forma geométrica (considere que s pode ser 'quadrado', 'retangulo' ou 'circulo'). 
  Conforme a forma geométrica lida, seu programa deve ler também a(s) sua(s) dimensão(ões), sendo lado para o quadrado, base e altura para o retângulo e raio para o circulo. 
  Seu programa deve mostrar qual a área da forma geométrica lida. 
  Para resolver este problema, pense quais são os objetos envolvidos e qual o nível de abstração adequado. 
  O que seria um objeto nesse caso? E o que seria uma classe? 
  Defina classes adequadas, com os respectivos atributos e métodos, e instancie seus objetos no programa principal.
"""

import math
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass


class Quadrado(FormaGeometrica):
    def __init__(self, lado: float):
        self.lado = lado
    
    def area(self): 
        return math.pow(self.lado, 2)


class Retangulo(FormaGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
    
    def area(self): 
        return self.base * self.altura

class Circulo(FormaGeometrica):
    def __init__(self, raio: float):
        self.raio = raio
    
    def area(self): 
        return math.pi * math.pow(self.raio, 2)

def main():
    quadrado = Quadrado(2)
    retangulo = Retangulo(2,3)
    circulo = Circulo(1.2)

    print('Area do quadrado: ', quadrado.area())
    print('Area do retangulo: ', retangulo.area())
    print('Area do circulo: ', circulo.area())

main()
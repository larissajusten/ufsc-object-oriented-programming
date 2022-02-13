from abc import ABC, abstractmethod
import math


class FormaGeometrica(ABC):
    def __init__(self):
        self.__area = 0

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area: float):
        self.__area = area

    @abstractmethod
    def calcula_area(self):
        pass


class Quadrado(FormaGeometrica):
    def __init__(self, lado: float):
        super().__init__()
        self.__lado = lado

    def calcula_area(self):
        self.area = self.__lado * self.__lado


class Retangulo(FormaGeometrica):
    def __init__(self, base: float, altura: float):
        super().__init__()
        self.__base = base
        self.__altura = altura

    def calcula_area(self):
        self.area = self.__base * self.__altura


class Circulo(FormaGeometrica):
    def __init__(self, raio: float):
        super().__init__()
        self.__raio = raio

    def calcula_area(self):
        self.area = math.pi * self.__raio**2


figuras = [Quadrado(2), Retangulo(2, 3), Circulo(2), Circulo(
    3), Quadrado(3), Quadrado(2), Retangulo(1, 3)]

for fig in figuras:
    fig.calcula_area()
    print(fig.area)

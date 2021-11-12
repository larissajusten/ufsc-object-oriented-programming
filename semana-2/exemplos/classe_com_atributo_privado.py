class Carro:
    def __init__(self, modelo: str, cor: str, placa: str):
        self.__modelo = modelo
        self.__cor = cor
        self.__placa = placa
        self.__velocidade = 0
        
    def buzinar(self):
        print('carro', self.__modelo, 'buzinou')
        
    def acelerar(self, valor: int):
        self.__velocidade += valor
        if self.__velocidade > 100:
            return 'cuidado!'
        else:
            return 'velocidade aceitável.'
        
    def frear(self):
        self.__velocidade -= 10
        if self.__velocidade < 0:
            self.__velocidade = 0
            
            
carro1 = Carro('Gol', 'Vermelho', 'ABC-1234')
carro2 = Carro('Fox', 'Prata', 'XYZ-1234')

carro1.buzinar()
print(carro2.acelerar(80))
print(carro1.__modelo)
print(carro2.__velocidade, 'km/h')
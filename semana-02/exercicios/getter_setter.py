class Carro:
    def __init__(self, modelo: str, cor: str, placa: str):
        self.__modelo = modelo
        self.__cor = cor
        self.__placa = placa
        self.__velocidade = 0

    # Getters
    @property
    def modelo(self):
        return self.__modelo

    @property
    def cor(self):
        return self.__cor

    @property
    def placa(self):
        return self.__placa

    @property
    def velocidade(self):
        return self.__velocidade

    # Setters
    @cor.setter
    def cor(self, cor: str):
        self.__cor = cor
    
    @placa.setter
    def placa(self, placa: str):
        self.__placa = placa

    # Metodos    
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
print(carro1.modelo)
print(carro2.velocidade, 'km/h')
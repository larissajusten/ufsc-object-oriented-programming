class Carro:
    def __init__(self, modelo: str, cor: str, placa: str):
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.velocidade = 0
        
    def buzinar(self):
        print('carro', self.modelo, 'buzinou')
        
    def acelerar(self, valor: int):
        self.velocidade += valor
        if self.velocidade > 100:
            return 'cuidado!'
        else:
            return 'velocidade aceitável.'
        
    def frear(self):
        self.velocidade -= 10
        if self.velocidade < 0:
            self.velocidade = 0
            
            
def main():
    carro1 = Carro('Gol', 'Vermelho', 'ABC-1234')
    carro2 = Carro('Fox', 'Prata', 'XYZ-1234')
    
    carro1.buzinar()
    print(carro2.acelerar(80))
    print(carro2.velocidade, 'km/h')
    
main()
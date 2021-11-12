"""
class NotaFiscal:
    def __init__(self):
        self.__valor_de_venda = 0

    @property
    def valor_de_venda(self):
        return self.__valor_de_venda

    @valor_de_venda.setter
    def valor_de_venda(self, valor: float):
        if valor >= 0:
            self.__valor_de_venda = valor

    def emite_nota_fiscal(self):
        print('Emitindo nota fiscal no valor de R$', self.__valor_de_venda)


def main():

    nf = NotaFiscal()
    nf.valor_de_venda = 100
    nf.emite_nota_fiscal()

main()
"""

class NotaFiscal:
    def __init__(self):
        self.__valor_de_venda = 0

    def set_valor_de_venda(self, valor: float):
        if valor >= 0:
            self.__valor_de_venda = valor

    def emite_nota_fiscal(self):
        print('Emitindo nota fiscal no valor de R$', self.__valor_de_venda)


def main():
    
    nf = NotaFiscal()
    nf.valor_de_venda = 100
    nf.emite_nota_fiscal()
    
main()
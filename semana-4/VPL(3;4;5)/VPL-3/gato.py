from mamifero import Mamifero


class Gato(Mamifero):
    def __init__(self):
        super().__init__(2, 2)

    def produzir_som(self):
        return f'MAMIFERO: PRODUZ SOM: {self.volume_som} SOM: MIAU'

    def miar(self):
        return self.produzir_som()

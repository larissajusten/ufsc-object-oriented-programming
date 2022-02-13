from mamifero import Mamifero


class Cachorro(Mamifero):
    def __init__(self):
        super().__init__(3, 3)

    def produzir_som(self):
        return f'MAMIFERO: PRODUZ SOM: {self.volume_som} SOM: AU'

    def latir(self):
        return self.produzir_som()

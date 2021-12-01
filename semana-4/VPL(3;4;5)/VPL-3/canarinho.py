from ave import Ave


class Canarinho(Ave):
    def __init__(self, tamanho_passo, altura_voo):
        super().__init__(tamanho_passo, altura_voo)

    def produzir_som(self):
        return 'AVE: PRODUZ SOM: PIU'

    def cantar(self):
        return self.produzir_som()

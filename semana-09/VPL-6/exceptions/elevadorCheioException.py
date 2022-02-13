class ElevadorCheioException(Exception):
    def __init__(self):
        super().__init__("Elevador está com capacidade máxima!")

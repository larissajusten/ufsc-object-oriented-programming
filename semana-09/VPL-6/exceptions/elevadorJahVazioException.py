class ElevadorJahVazioException(Exception):
    def __init__(self):
        super().__init__("Elevador está vazio!")

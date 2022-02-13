class ElevadorJahNoUltimoAndarException(Exception):
    def __init__(self):
        super().__init__("Elevador se encontra no último andar!")

class Produto:

    def __init__(self, codigo, descricao, categoria):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria = categoria
        self.__quantidade = 0
        self.__preco_unitario = 0.0
        self.__cliente = None

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria_produto):
        self.__categoria = categoria_produto

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    def preco_total(self):
        return self.quantidade * self.preco_unitario

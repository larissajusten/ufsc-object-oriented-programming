from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora,
                 autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__numeroCapitulo = numeroCapitulo
        self.__tituloCapitulo = tituloCapitulo
        self.__lista_capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def ano(self) -> int:
        return self.__ano

    @property
    def editora(self) -> Editora:
        return self.__editora

    @property
    def autores(self):
        return self.__autores

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self.__titulo = titulo

    @ano.setter
    def ano(self, ano: int) -> None:
        self.__ano = ano

    @editora.setter
    def editora(self, editora: Editora) -> None:
        self.__editora = editora

    def incluirAutor(self, autor: Autor) -> None:
        if autor not in self.autores and isinstance(autor, Autor):
            self.__autores.append(autor)
        else:
            print('Falha ao inserir autor!')

    def excluirAutor(self, autor: Autor) -> None:
        if autor in self.autores and isinstance(autor, Autor):
            self.autores.remove(autor)
        else:
            print('Falha ao excluir autor!')

    def incluirCapitulo(self, numeroCapitulo: int,
                        tituloCapitulo: str) -> None:
        existe_capitulo = next((capitulo for capitulo in self.__lista_capitulos
                                if capitulo.numero == numeroCapitulo), False)
        if not existe_capitulo:
            novo_capitulo = Capitulo(numeroCapitulo, tituloCapitulo)
            self.__lista_capitulos.append(novo_capitulo)
        else:
            print('Falha ao inserir Capitulo!')

    def excluirCapitulo(self, tituloCapitulo: str) -> None:
        capitulo = next((capitulo for capitulo in self.__lista_capitulos
                         if capitulo.titulo == tituloCapitulo), False)
        if capitulo:
            self.__lista_capitulos.remove(capitulo)
        else:
            print('Falha ao excluir Capitulo!')

    def findCapituloByTitulo(self, tituloCapitulo: str) -> Capitulo:
        capitulo = next((capitulo for capitulo in self.__lista_capitulos
                         if capitulo.titulo == tituloCapitulo), False)
        return capitulo if capitulo else None

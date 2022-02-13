"""
    Crie as classes necessárias para um sistema de gerenciamento de uma biblioteca. 
    Os bibliotecários deverão preencher o sistema com o título do livro, os autores, o ano, a editora, a edição e o volume.
    A biblioteca também terá um sistema de pesquisa (outro software), portanto será necessário conseguir acessar os atributos
        típicos de pesquisa (nome, autor, ...).
"""
from collections import defaultdict


class Autor:
    def __init__(self, codigo: int, nome: str) -> None:
        self.__codigo = codigo
        self.__nome = nome

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome


class Editora:
    def __init__(self, cnpj: str, nome: str) -> None:
        self.__cnpj = cnpj
        self.__nome = nome

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @property
    def nome(self) -> str:
        return self.__nome


class Livro:
    def __init__(self, isbn: str, titulo: str, ano: str, editora: Editora, edicao: int, volume: int, autores: list = []) -> None:
        self.__isbn = isbn
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__edicao = edicao
        self.__volume = volume
        self.__autores = autores

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def ano(self) -> str:
        return self.__ano

    @property
    def editora(self) -> Editora:
        return self.__editora

    @property
    def edicao(self) -> int:
        return self.__edicao

    @property
    def volume(self) -> int:
        return self.__volume

    @property
    def autores(self) -> list:
        return self.__autores

    def adicionar_novo_autor(self, novo_autor: Autor) -> Autor:
        if isinstance(novo_autor, Autor):
            existe_autor = next(
                (autor for autor in self.autores if autor.codigo == novo_autor.codigo), False)
            if not existe_autor:
                self.__autores.append(novo_autor)
                return novo_autor


class Biblioteca:
    def __init__(self, nome: str = 'Biblioteca') -> None:
        self.__nome = nome
        self.__livros = defaultdict(lambda: "Not Present")

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def livros(self) -> list:
        return self.__livros.values()

    def adicionar_livro(self, novo_livro: Livro):
        if isinstance(novo_livro, Livro):
            self.__livros[novo_livro.isbn]: livro

    def remover_livro(self, isbn: str):
        return self.livros.pop(isbn)


class PesquisaBiblioteca:
    @staticmethod
    def pesquisa_autor_nome(biblioteca: Biblioteca, nome: str):
        autores = [
            autor for livro in biblioteca.livros for autor in livro.autores if autor.nome == nome]
        return autores[0]

    @staticmethod
    def pesquisa_autor_codigo(biblioteca: Biblioteca, codigo: int):
        autores = [
            autor for livro in biblioteca.livros for autor in livro.autores if autor.codigo == codigo]
        return autores[0]

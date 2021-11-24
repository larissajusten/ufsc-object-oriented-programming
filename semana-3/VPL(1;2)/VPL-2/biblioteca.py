from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    @property
    def livros(self) -> Livro:
        return self.__livros

    def incluirLivro(self, livro: Livro) -> None:
        if livro not in self.livros and isinstance(livro, Livro):
            self.__livros.append(livro)
        else:
            print('Falha ao inserir livro na Biblioteca!')

    def excluirLivro(self, livro: Livro) -> None:
        if livro in self.livros:
            self.livros.remove(livro)
        else:
            print('Falha ao excluir livro da Biblioteca!')

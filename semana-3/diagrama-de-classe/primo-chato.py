"""
    Primo Chato

    Seu primo possui muitos livros, todos em papel, e vive emprestando aos amigos dele. 
    Entretanto, muitas vezes ele esquece a quem emprestou e já perdeu diversos Livros por causa disso. 
    No almoço da família, no último final de semana, ele não parou de falar e se lamentar a respeito até que, cansado de ouvir suas lamentações, 
        você decidiu ajudá-lo desenvolvendo um programa para resolver este problema. 
    Conversando com ele a respeito vocês decidiram que sistema deve permitir o cadastro dos amigos, incluindo: nome, número do telefone e e-mail 
        e também cadastrar os Livros, com: título, resumo, autor, personagem principal, gênero (comédia, romance ou aventura, etc) e faixa etária. 
    Deve ser possível cadastrar os empréstimos e obter a lista de Livros emprestados incluindo quais amigos estão com quais Livros.

    Assim, como um bom desenvolvedor, antes de começar a programar você decidiu modelar o sistema usando um diagrama de classes que:
    1. Identifique e modele as classes do problema
    2. Identifique e modele os atributos e métodos das classes
    3. Identifique e modele as associações existentes entre as classes
"""

# Abrir em: https://mermaid.live/

classDiagram
    direction RL
    class Genero {
        <<enumeration>>
        Comedia
        Romance
        Terror
        Aventura
    }

    Amigo "1" o-- "0..n" Livro
    Livro "1" --> "1..*" Genero

    class Amigo {
        -id
        -String nome
        -String numero
        -String email
        -List~Livro~ livro
        +getNome()
        +setNome(nome)
        +getNumero()
        +setNumero(numero)
        +getEmail()
        +setEmail(email)
        +addLivro()
        +removeLivro()
        +getListaLivros()
    }

    class Livro {
        -id
        -String titulo
        -String resumo
        -String autor
        -String personagem_principal
        -List~Genero~ genero
        -int faixa_etaria
        -id_amigo
        +getStatusLivro()
        +setStatusLivro(status)
        +isEmprestado()
    }

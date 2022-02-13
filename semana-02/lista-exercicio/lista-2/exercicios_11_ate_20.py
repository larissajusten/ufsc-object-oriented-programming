# Exercício 11. ​Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

"""<->"""

# Exercício 12. ​Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média dealtura desses alunos.

"""<->"""

# Exercício 13. ​Faça um programa que receba a temperatura média de cada mês do anoe armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas emostre todas as temperaturas acima da média anual, e em que mês
#     elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

"""<->"""

# Exercício 14. ​Utilizando listas faça um programa que faça 5 perguntas para umapessoa sobre um crime. As perguntas são:
#   ○ "Telefonou para a vítima?"
#   ○ "Esteve no local do crime?"
#   ○ "Mora perto da vítima?"
#   ○ "Devia para a vítima?"
#   ○ "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa nocrime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificadacomo "Suspeita",
#     entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário,ele será classificado como "Inocente".

"""<->"""

# Exercício 15.​ Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado umvalor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
#   ○ Mostre a quantidade de valores que foram lidos;
#   ○ Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#   ○ Exiba todos os valores na ordem inversa à que foram informados, um abaixo dooutro;
#   ○ Calcule e mostre a soma dos valores;
#   ○ Calcule e mostre a média dos valores;
#   ○ Calcule e mostre a quantidade de valores acima da média calculada;
#   ○ Calcule e mostre a quantidade de valores abaixo de sete;
#   ○ Encerre o programa com uma mensagem;

"""<->"""

# Exercício 16.​ Utilize uma lista para resolver o problema a seguir. Uma empresa pagaseus vendedores com base em comissões.
# O vendedor recebe R$200 por semanamais 9 por cento de suas vendas brutas daquela semana.
# Por exemplo, um vendedorque teve vendas brutas de R$3000 em uma semana recebe R$200 mais 9 por cento deR$3000,
#     ou seja, um total de R$470.
# Escreva um programa (usando uma lista decontadores) que determine quantos vendedores receberam salários nos seguintes
#    intervalos de valores:
#   ○ R$200 - R$299
#   ○ R$300 - R$399
#   ○ R$400 - R$499
#   ○ R$500 - R$599
#   ○ R$600 - R$699
#   ○ R$700 - R$799
#   ○ R$800 - R$899
#   ○ R$900 - R$999
#   ○ R$1000 em diante
# Desafio:​ Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ​ifs​ aninhados.

"""<->"""

# Exercício 17.​ Em uma competição de salto em distância cada atleta tem direito a cincosaltos.
# O resultado do atleta será determinado pela média dos cinco valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
#     depois informe o nome, os saltos e a média dos saltos.
# O programa deve ser encerrado quando não for informado o nome do atleta.
# A saída doprograma deve ser conforme o exemplo abaixo:
"""
Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

"""<->"""

# Exercício 18.​ Uma grande emissora de televisão quer fazer uma enquete entre osseus telespectadores para saber qual o melhor
#     jogador após cada jogo.
# Para isto,faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos.
# Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++.
# Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa dojogador.
# Um número de jogador igual zero, indica que a votação foi encerrada.
# Se umnúmero inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número.
# Após o final da votação, oprograma deverá exibir:
#   ○ a) O total de votos computados;
#   ○ b) Os números e respectivos votos de todos os jogadores que receberam votos;
#   ○ c) O percentual de votos de cada um destes jogadores;
#   ○ d) O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos
#            e o percentual de votos dados a ele.Observe que os votos inválidos e o zero final não devem ser computadoscomo votos.
#        O resultado aparece ordenado pelo número do jogador.
#        O programa deve fazer uso de arrays.
#        O programa deverá executar o cálculo do percentual de cada jogador através de uma função.
#        Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos.
#        A função calculará o percentual e retornará o valor calculado.
#        Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.
#        Os dados são fictícios e podem mudar a cada execução do programa.
#        Ao final, oprograma deve ainda gravar os dados referentes ao resultado davotação em um arquivo texto no disco,
#            obedecendo a mesma disposiçãoapresentada na tela.
"""
Enquete: Quem foi o melhor jogador?
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:
Foram computados 8 votos.
Jogador        Votos        %
9               4          50,0%
10              3          37,5%
11              1          12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
"""

"""<->"""

# Exercício 19​. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
#     "Qual o melhor Sistema Operacional para uso em servidores?"
#     As possíveis respostas são:
#     1- Windows Server
#     2- Unix
#     3- Linux
#     4- Netware
#     5- Mac OS
#     6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
# O programa deverá ler os valores até ser minformado o valor 0, que encerra a entrada dos dados.
# Não deverão ser aceitos valoresalém dos válidos para o programa (0 a 6).
# Os valores referentes a cada uma dasopções devem ser armazenados numa lista.
# Após os dados terem sido completamenteinformados, o programa deverá calcular a percentual de cada um dos concorrentes e informar
#     o vencedor da enquete.
# O formato da saída foi dado pela empresa, e é o seguinte:
"""
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----   ---
Total                    8800O   -
Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

"""<->"""

# Exercício 20​. Criar um tipo de dado (classe) MinhaLista que possui o comportamentode uma lista builtin mas é implementada usando tuplas.
# O novo tipo de dado deve permitir atribuição e acesso aos elementos da lista, e conter os seguintes métodos:
#     append()
#     remove(element)
#     sort()
#     reverse()
#     pop(index=-1)
# *dica: usar magic methods

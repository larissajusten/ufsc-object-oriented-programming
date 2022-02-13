## Exercício VPL 5 - Jogo de Cartas (03/12)
**Data de entrega:** Friday, 3 Dec 2021, 23:59 <br/>
**Arquivos requeridos:** Personagem.py, Mesa.py, Jogador.py, ControladorJogo.py, Carta.py <br/>
**Número máximo de arquivos:** 8 <br/>
**Tipo de trabalho:** Trabalho individual <br/>
**Exercício VPL 5 - Jogo de Cartas:** <br/>
> Um jogo de cartas possui em cada carta o tipo de um personagem (Água, Terra, Ar, Fogo) e seus atributos: energia, habilidade, velocidade e resistência, que variam de 0 a 100.
No jogo participam dois jogadores. Cada jogador possui cinco cartas na mão.
Em cada rodada, cada jogador coloca uma carta na mesa. As duas cartas são então comparadas.
Ganha a rodada o jogador que tiver maior valor total na sua carta na mesa, somando-se os valores de todos os atributos da carta.
O jogador vencedor da rodada fica com a carta do adversário, devolvendo para sua mão a sua própria carta e a do adversário.
Caso ocorra empate dos valores das cartas, ambos mantém suas respectivas cartas, colocando de volta cada um na sua mão.
Caso um jogador fique sem cartas ao final de uma rodada, considere o jogo ganho pelo jogador que ainda possui cartas na mão.
Observe que o jogo pode terminar em empate pois as somas dos atributos das cartas pode ser igual, sendo assim o número de rodadas foi limitado a 50.

**IMPORTANTE:** Implemente o exercício seguindo exatamente as Classes e Interfaces disponibilizadas pelo professor.

Leve em consideração os comentários disponibilizados pelo código pois eles descrevem o que precisa ser implementado.
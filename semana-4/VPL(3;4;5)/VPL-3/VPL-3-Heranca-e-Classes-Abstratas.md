## Exercício VPL 3 - Herança e Classes Abstratas (03/12)
**Data de entrega:** Friday, 3 Dec 2021, 23:59 <br/>
**Arquivos requeridos:** animal.py, mamifero.py, ave.py, cachorro.py, gato.py, canarinho.py <br/>
**Número máximo de arquivos:** 7 <br/>
**Tipo de trabalho:** Trabalho individual <br/>
**Exercício VPL 3 - Herança e Classes Abstratas** <br/>
Escreva um programa em Python que possua cinco classes: Animal, Mamifero, Ave, Cachorro, Gato e Canarinho. Defina uma hierarquia de herança entre essas classes.

**A implementação deve atender às seguintes regras:** <br/>

- Não existem instâncias de Animal, Mamifero e Ave, somente dos seus sub-tipos
- Todos os animais possuem um tamanho de passo e quando se movem, retornam a mensagem: "ANIMAL: DESLOCOU " tamanhoPasso
- As aves quando se movem, retornam a mensagem: "ANIMAL: DESLOCOU "+tamanhoPasso+" VOANDO"
- Todos os animais produzem algum tipo de som com um volume, mas cada um do seu jeito:
  - Gato (miar): "MAMIFERO: PRODUZ SOM: "+volumeSom+ " SOM: MIAU"
  - Cachorro (latir): "MAMIFERO: PRODUZ SOM: "+volumeSom+ " SOM: AU"
  - Canarinho (cantar): "AVE: PRODUZ SOM: PIU"
- Somente as aves voam (que é a mesma coisa que mover para uma ave)
- Somente os canarinhos cantam 
- Cachorros tem tamanhoPasso = 3 e volumeSom = 3
- Gatos tem tamanhoPasso = 2 e volumeSom = 2
- Aves tem tamanhoPasso e alturaVoo parametrizáveis no construtor

**Observação:** <br/>

**Ordem de parâmetros dos construtores:** <br/>

- Ave(int tamanhoPasso, int alturaVoo)
- Mamifero(int volumeSom, int tamanhoPasso)
- Canarinho(int tamanhoPasso, int alturaVoo)
- Siga o exemplo anexo e complete com o seu código.

Utilize exatamente os mesmos nomes de classe e das operações.

Veja no anexo a modelagem UML [(diagrama de classes)](https://github.com/larissajusten/ufsc-object-oriented-programming/tree/main/semana-4/VPL(3;4;5)/VPL-3/Modelo_Ex_05.png).
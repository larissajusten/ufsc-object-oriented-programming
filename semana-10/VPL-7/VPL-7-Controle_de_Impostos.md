## VPL 7 - Controle de Impostos (20/02)
**Data de entrega:** Sunday, 20 Feb 2022, 23:59 <br/>
**Arquivos requeridos:** imposto.py, incidencia_imposto.py, ipi.py, irpj.py, iss.py, empresa.py, icms.py, empresa_duplicada_exception.py, controlador_sistema_empresas.py, empresa_dao.py <br/>
**Tipo de trabalho:** Trabalho individual <br/>
**Descrição do Exercício:** <br/>
Implementação de um sistema de controle de impostos. O sistema permite o cadastro de empresas e impostos.

Impostos têm uma alíquota (percentual com que um tributo incide sobre o valor de algo tributado) que é aplicada sobre um determinado valor para que seja calculado o imposto a pagar. Por exemplo, se um determinado imposto possui alíquota de 15% e o valor de faturamento sobre o qual ele incide é de R$ 2.000,00, o valor do imposto a pagar seria de R$ 300,00.

Cada imposto tem ainda uma regra de cálculo diferente, sendo que alguns são aplicados somente sobre o faturamento de serviços, outros somente sobre o faturamento de produção, outros sobre o faturamento de vendas e outros ainda são aplicados sobre o faturamento total.

A partir da informação do faturamento de serviços, produção e vendas, o sistema permite calcular o valor total de impostos a pagar.

### **Pontuação:**
`Questão 01 (01 PONTO)` - Definição de Classes, Enum, Exceções e Associações: 
> A estrutura das Classes, Enum, Exceções e Associações deve estar exatamente igual ao modelo de classes. Qualquer diferença de nomes de atributos, herança, tipos de dados, assinaturas de operações, etc. serão descontadas. Siga exatamente o que está definido no diagrama de classes.

`Questão 02 (01 PONTO)` - Instanciar Controlador, Empresas e Impostos: 
> O Controlador, Empresas e Impostos devem poder ser instanciados seguindo as assinaturas dos construtores definidos no diagrama de classes. Os atributos devem ser implementados para receber os parâmetros dos construtores definidos.

`Questão 03 (03 PONTOS)` - Incluir, Excluir e Listar Empresas e Impostos: 
> Deve ser possível Incluir, Excluir e Listar tanto Empresas no Controlador, quanto os Impostos de uma Empresa. Prestar muita atenção quanto a inclusão de valores NULL, tratar tentativa de inserir entidades duplicadas. Não podem ser cadastradas duas Empresas com o mesmo CNPJ.

`Questão 04 (01 PONTO)` - Tratamento de Exceção: 
> Para o caso da tentativa de incluir uma Empresa com o mesmo CNPJ de outra Empresa já cadastrada, deve ser disparada uma exceção correspondente. Veja no diagrama de classes os detalhes da Exceção.

`Questão 05 (02 PONTOS)` - Cálculo dos Impostos:
> Os impostos devem ser calculados corretamente. Algumas regras devem ser levadas em conta:

- Cada Imposto (ISS, ICMS, IPI ou IRPJ) possui a informação de IncidenciaImposto, que indica se o imposto se aplica a PRODUCAO, SERVICOS, VENDAS e TODOS. Ou seja, se o imposto IPI possuir a indicação de IncidenciaImposto.PRODUCAO, a alíquota do IPI somente será aplicada sobre o faturamentoProducao.
- O **imposto IPI** leva em conta se existe "aliquotaAdicional". 
Se existir aliquotaAdicional, a alíquota é aumentada em 10%.
Por exemplo, se a alíquota informada no construtor for 10.0 e existe "aliquotaAdicional", então a alíquota calculada será de 11.0.

- O **imposto ICMS** leva em conta a "diferencaEstado". 
O valor de "diferencaEstado" deve ser somado a alíquota informada.
Por exemplo, se a alíquota informada no construtor for 10.0 e a "diferencaEstado" for 2, então a alíquota calculada sera de 12.0

- O **imposto IRPJ** leva em conta o "desconto". 
O valor de "desconto" deve ser subtraído da alíquota informada.
Por exemplo, se a alíquota informada no construtor for 10.0 e o "desconto" for 1, então a alíquota calculada sera de 9.0

- O **imposto ISS** leva em a lista de Serviços cadastrados no ISS. 
Para cada serviço cadastrado na lista de Serviços do ISS, é reduzido 10% no imposto (0,10% da Alíquota).
Por exemplo, se a alíquota informada no construtor for 10.0 e tiverem sido incluídos 2 serviços na lista, então a alíquota calculada sera de 9.8

`Questão 06 (01 PONTO)` - Persistência:
> As empresas cadastradas, com todos os seus dados, devem ser corretamente armazenadas pelo ControladorSistemaEmpresas em um arquivo (empresa.pkl) utilizando a classe EmpresaDAO.

`Questão 07 (01 PONTO)` - Estilo de código:
> O estilo do código de todas as classes deve estar de acordo com o pep8.

***IMPORTANTE:***
- Comece implementando todas as operações exigidas no diagrama de classes e deixe o código compilando;
- Em seguida inclua os atributos necessários definidos no diagrama de classes;
- Retire acentos e caracteres especiais antes de submeter;
- Leia atentamente as mensagens de erro.
- Implemente todos os códigos solicitados e não esqueça de clicar em Avaliar.
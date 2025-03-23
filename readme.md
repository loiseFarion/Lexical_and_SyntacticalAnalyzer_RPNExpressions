# PROJETO CALCULADORA - FASE 2
  Este é um programa em Python implementado para a realização da validação léxica e sintática das expressões contidas nos arquivos de teste disponivéis. Para que o programa realizasse de forma correta a análise sintática, criou-se uma máquina de estados finitos baseada em um padrão válido de expressões aritméticas e não aritméticas.

## Execução do programa
Caso só estejam disponíveis os arquivos: <br />
analisador.py <br />
formulas1.txt <br />
formulas2.txt <br />
formulas3.txt <br />
MEFAnalisadorLexico.png <br />
readme.md <br />
TabelaDerivacao.png <br />
Rode o comando: antlr4 -Dlanguage=Python3 Sintatico.g4<br><br> 
Caso contrário apenas faça:<br />
--- Replit Shell <br />
python analisador.py 'formulasn' <br />
Onde n pode assumir os valores de: 1, 2 e 3. <br />

### Exemplo de um padrão válido de expressões
(8 16 -) <br />
(48 (16 1 -) |) <br />
((5 RES) MEM) <br />
(MEM 2 *) <br />
((5.8 4.2 +) (2 3 *) +) <br />
(4 (2 3 *) +) <br />
(2 RES) <br />
(2 (2 (2 (2 (2 2 *) *) *) *) *) <br />
(if MEM >= 5: MEM = 10) <br />
(if MEM < 3: MEM = 1 else: MEM = 5) <br />
(for i in range(MEM): MEM -= 10) <br />
(2 MEM +) <br />

  Ademais, as expressões válidas são separdas em tokens, os quais são utilizados para gerar uma string de tokens.
  
  Após a realização da análise léxica o programa faz a validação sintática das expressões que não apresentaram erro léxico. Para uma análise correta o analisador sintático foi desenvolvido através das regras de produção criadas e da tabela LL(1).

  Além disso, o programa gera a respectiva árvore sintática para as regras de produção criadas e validadas com FIRST e FOLLOW para LL(1).
  
## Analisador léxico com máquina de estados finitos
### - Diagrama de transição da máquina de estados finitos
<img src="MEFAnalisadorLexico.png"><br>
  A máquina de estados finitos criada para o analisador léxico usa de base a estrutura de expressões válidas citada anteriormente. Sua funcionalidade consiste em:

#### 1º estado:
Verifica se o dado consiste em um parênteses aberto '('

#### 2º estado:
Verifica se o dado consiste em um parênteses fehcado ')'

#### 3º estado:
Verifica se o dado consiste em um número (int ou float)

#### 4º estado:
Verifica se o dado consiste em um operador aritmético ('+', '-', '*', '|', '/', '%', '^')

#### 5º estado:
Verifica se o dado consiste em 'MEM'

#### 6º estado:
Verifica se o dado consiste em 'RES'

#### 7º estado:
Verifica se o dado consiste em 'if'

#### 8º estado:
Verifica se o dado consiste em 'else:'

#### 9º estado:
Verifica se o dado consiste em 'for'

#### 10º estado:
Verifica se o dado consiste em comparador ('==', '<', '>', '<=', '>=', '!=' ou 'in', 'not in' ou '=', '+=', '-=', '*=', '/=', '%=', '^=', '|=')

#### 11º estado:
Verifica se o dado consiste em uma constante ('i', 'range', ':')

  A verificação é realizada de forma linear, onde a máquina verifica o estado 1, se não for válido passa para o estado 2, dessa forma, se ela chegar até o estado 11 e o mesmo também não for válido ela vai para o estado de erro apontando assim, o erro léxico. Caso a validação seja feita em algum estado, a máquina vai para o estado de resto, onde é verificado se a expressão ainda tem algo a ser analisado. Se a string chegou ao fim a máquina é finalizada, mas se a expressão é aninhada a máquina volta para as verificações novamente.

## Analisador sintático
### Regras de produção

E → (op op operando)<br><br>
operando → + OR - OR * OR / OR | OR % OR ^ OR M OR R OR F OR I <br><br>
F → for i ob range ( M ) : M oat n <br><br> 
I → if M opr n : M oat n e <br><br>
e → else : M oat n | $ <br><br>
opr → == OR < OR > OR <= OR >= OR != <br><br>
ob → in OR notIn <br><br>
oat → = OR += OR -= <br><br> 
op → n OR E OR M OR $ <br><br> 
n → num <br><br> 
M → mem <br><br> 
R → res <br><br> 

Signicado de siglas:<br><br> 
E: Expressao<br>
oat: Operador de atribuição<br>
ob: Operador de busca<br>
opr: Operador relacional<br>
num: [0..9]+ OR [0-9]+\.[0-9]+ <br>

### Conjuntos de FIRST E FOLLOW
FIRST(S) = {(}<br>
FIRST(E) = {(}<br>
FIRST(operando) = {+, -, *, /, |, %, ^, mem, res, for, if}<br>
FIRST(F) = {for}<br>
FIRST(I) = {if}<br>
FIRST(e) = {else, $}<br>
FIRST(opr) = {==, <, >, <=, >=, !=}<br>
FIRST(ob) = {in, notin}<br>
FIRST(oat) = {=, +=, -=}<br>
FIRST(op) = {(, $, num, mem}<br>
FIRST(n) = {num}<br>
FIRST(M) = {mem}<br>
FIRST(R) = {res}<br>

FOLLOW(S) = {$}<br>
FOLLOW(E) = {+, -, *, /, |, %, ^, mem, res, for, if, (, $, num}<br>
FOLLOW(operando) = {)}<br>
FOLLOW(F) = {)}<br>
FOLLOW(I) = {)}<br>
FOLLOW(e) = {)}<br>
FOLLOW(opr) = {num}<br>
FOLLOW(ob) = {range}<br>
FOLLOW(oat) = {num}<br>
FOLLOW(op) = {+, -, *, /, |, %, ^, mem, res, for, if, (, $, num}<br>
FOLLOW(n) = {), else, $, :, +, -, *, /, |, %, ^, mem, res, for, if, (, num}<br>
FOLLOW(M) = {), =, +=, -=, ==, <, >, <=, >=, !=, +, -, *, /, |, %, ^, mem, res, for, if, (, $, num}<br>
FOLLOW(R) = {)}<br>

### Tabela de derivação
<img src="TabelaDerivacao.png"><br>
  Após a criação das regras de produção com o First e Follow para o LL(1) e da tabela de derivação, foi desenvolvido um analisador sintático através do ANTLR, dessa forma, o mesmo respeita a gramática criada.

  Ademais, foram feito tratamentos para preencher os espaços vazios entre parêntese com $, pois assim, o analisador sintático pode realizar a validação de forma correta.
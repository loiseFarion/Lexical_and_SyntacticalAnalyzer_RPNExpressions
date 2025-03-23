# CALCULATOR PROJECT - PHASE 2
This is a Python program implemented to perform lexical and syntactical validation of the expressions contained in the available test files. To ensure correct syntactical analysis, a finite state machine was created based on a valid pattern of arithmetic and non-arithmetic expressions.

## Program Execution
If the following files are available: <br />
analisador.py <br />
formulas1.txt <br />
formulas2.txt <br />
formulas3.txt <br />
MEFAnalisadorLexico.png <br />
readme.md <br />
TabelaDerivacao.png <br />
Run the command: `antlr4 -Dlanguage=Python3 Sintatico.g4`<br><br> 
Otherwise, just run:<br />
--- Replit Shell <br />
`python analisador.py 'formulasn'` <br />
Where n can be: 1, 2, or 3. <br />

### Example of a valid expression pattern
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

Additionally, valid expressions are separated into tokens, which are used to generate a string of tokens.

After performing lexical analysis, the program validates the syntax of expressions that have no lexical errors. For correct analysis, the syntactical analyzer was developed based on the production rules created and the LL(1) table.

Furthermore, the program generates the corresponding syntax tree for the production rules created and validated with FIRST and FOLLOW for LL(1).

## Lexical Analyzer with Finite State Machine
### - Finite State Machine Transition Diagram
<img src="MEFAnalisadorLexico.png"><br>
The finite state machine created for the lexical analyzer uses the valid expression structure mentioned earlier. Its functionality is as follows:

#### State 1:
Checks if the input is an open parenthesis '('.

#### State 2:
Checks if the input is a close parenthesis ')'.

#### State 3:
Checks if the input is a number (int or float).

#### State 4:
Checks if the input is an arithmetic operator ('+', '-', '*', '|', '/', '%', '^').

#### State 5:
Checks if the input is 'MEM'.

#### State 6:
Checks if the input is 'RES'.

#### State 7:
Checks if the input is 'if'.

#### State 8:
Checks if the input is 'else:'.

#### State 9:
Checks if the input is 'for'.

#### State 10:
Checks if the input is a comparison operator ('==', '<', '>', '<=', '>=', '!=' or 'in', 'not in' or '=', '+=', '-=', '*=', '/=', '%=', '^=', '|=').

#### State 11:
Checks if the input is a constant ('i', 'range', ':').

The verification is performed linearly, where the machine checks state 1, and if invalid, moves to state 2. If it reaches state 11 and the expression is still invalid, it transitions to the error state, indicating a lexical error. If a state is validated, the machine moves to the rest state, where it checks if the expression still has something to be analyzed. If the string reaches the end, the machine finishes, but if the expression is nested, the machine returns to the checks again.

## Syntactical Analyzer
### Production Rules

E → (op op operand)<br><br>
operand → + OR - OR * OR / OR | OR % OR ^ OR M OR R OR F OR I <br><br>
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

Meaning of acronyms:<br><br> 
E: Expression<br>
oat: Assignment operator<br>
ob: Search operator<br>
opr: Relational operator<br>
num: [0..9]+ OR [0-9]+\.[0-9]+ <br>

### FIRST and FOLLOW Sets
FIRST(S) = {(}<br>
FIRST(E) = {(}<br>
FIRST(operand) = {+, -, *, /, |, %, ^, mem, res, for, if}<br>
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
FOLLOW(E) = {+, -, *, /, |, %, ^, mem, res, for, if, (, $, num}<br>
FOLLOW(operand) = {)}<br>
FOLLOW(F) = {)}<br>
FOLLOW(I) = {)}<br>
FOLLOW(e) = {)}<br>
FOLLOW(opr) = {num}<br>
FOLLOW(ob) = {range}<br>
FOLLOW(oat) = {num}<br>
FOLLOW(op) = {+, -, *, /, |, %, ^, mem, res, for, if, (, $, num}<br>
FOLLOW(n) = {), else, $, :, +, -, *, /, |, %, ^, mem, res, for, if, (, num}<br>
FOLLOW(M) = {), =, +=, -=, ==, <, >, <=, >=, !=, +, -, *, /, |, %, ^, mem, res, for, if, (, $, num}<br>
FOLLOW(R) = {)}<br>

### Derivation Table
<img src="TabelaDerivacao.png"><br>
After creating the production rules with First and Follow for LL(1) and the derivation table, a syntactical analyzer was developed using ANTLR, which respects the created grammar.

Additionally, treatments were done to fill the empty spaces between parentheses with $, allowing the syntactical analyzer to perform the validation correctly.

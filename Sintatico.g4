grammar Sintatico;

LPAREN: '(';
RPAREN: ')';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '|';
PERCENT: '%';
POWER: '^';
MEM: 'MEM';
RES: 'RES';
FOR: 'for';
I: 'i';
IF: 'if';
IN: 'in';
NOT_IN: 'not in';
EQUALS: '==';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN_OR_EQUAL: '>=';
NOT_EQUALS: '!=';
ASSIGN: '=';
INCREMENT: '+=';
DECREMENT: '-=';
NUM: [0-9]+('.'[0-9]+)? | '.' [0-9]+ ;
RANGE: 'range';
DOISPONTOS: ':';

// Define parser rules
program: expression EOF;

expression: LPAREN op op operando RPAREN;

operando: PLUS | MINUS | MULTIPLY | DIVIDE | MODULO | POWER | PERCENT | MEM | RES | FOR I (IN | NOT_IN) RANGE LPAREN MEM RPAREN DOISPONTOS MEM (ASSIGN | INCREMENT | DECREMENT) NUM | IF MEM (EQUALS | LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL | NOT_EQUALS) NUM DOISPONTOS MEM (ASSIGN | INCREMENT | DECREMENT) NUM (ELSE DOISPONTOS MEM (ASSIGN | INCREMENT | DECREMENT) NUM)?;

op: NUM | expression | MEM | VAZIO;

ELSE: 'else';

VAZIO: '$';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

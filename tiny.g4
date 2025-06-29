grammar tiny;
// (very) tiny version of tiny language
// no pointer, function as value and records

program: fun*;

fun_head: ID '(' id_list? ')';
fun: fun_head '{' (VAR id_list SEMI)? stm* RETURN exp SEMI '}';

id_list: ID (',' ID)*;
exp_list: exp (',' exp)*;

stm: ID '=' exp SEMI
	| OUTPUT exp SEMI
	| IF '(' exp ')' '{' stm* '}' else?
	| WHILE '(' exp ')' '{' stm* '}';

else: ELSE '{' stm* '}';

exp: INT
	| ID
	| exp MUL exp
	| exp DIV exp
	| exp ADD exp
	| exp SUB exp
	| exp GR exp
	| exp EQ exp
	| '('exp')'
	| INPUT
	| fun_call;

fun_call: ID'('exp_list?')';

ADD:'+';
SUB:'-';
MUL:'*';
DIV:'/';
EQ:'==';
GR:'>';

RETURN: 'return';
VAR: 'var';
OUTPUT: 'output';
INPUT: 'input';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
SEMI: ';';
ID: [a-z]+;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;

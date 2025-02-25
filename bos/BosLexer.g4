lexer grammar BosLexer;

options {
    caseInsensitive = true;
}

channels {
    COMMENTS,
    PREPROCESSOR,
    LINE_MACRO
}

// SYMBOLS
COMMA: ',';
L_PAREN: '(';
R_PAREN: ')';
L_BRACE: '{';
R_BRACE: '}';
L_SQUARE_BRACKET: '[';
R_SQUARE_BRACKET: ']';
SEMICOLON: ';';
EQUAL_ASSIGN: '=';

// OPERATORS
OP_ADD: '+';
OP_MINUS: '-';
OP_MULT: '*';
OP_DIV: '/';
OP_MOD: '%';

OP_INCREMENT: '++';
OP_DECREMENT: '--';

BITWISE_AND: '&';
BITWISE_OR: '|';
BITWISE_XOR: '^';
//BITWISE_NOT: '~';

COMP_EQUAL: '==';
COMP_NOT_EQUAL: '!=';
COMP_LESS: '<';
COMP_LESS_EQUAL: '<=';
COMP_GREATER: '>';
COMP_GREATER_EQUAL: '>=';

LOGICAL_AND: '&&' | 'and';
LOGICAL_OR: '||' | 'or';
LOGICAL_NOT: '!' | 'not';
LOGICAL_XOR: '^^' | 'xor';

// FLOW CONTROL
IF: 'if';
ELSE: 'else';           
WHILE: 'while';          
FOR: 'for';

// KEYWORDS
STATIC_VAR: 'static-var';
VAR: 'var';         

PIECE: 'piece';

TURN: 'turn';
AROUND: 'around';

MOVE: 'move';
ALONG: 'along';

TO: 'to';
FROM: 'from';
NOW: 'now';
SPEED: 'speed';

SPIN: 'spin';
ACCELERATE: 'accelerate';
STOP_SPIN:  'stop' '-'? 'spin';
DECELERATE: 'decelerate';     

WAIT_FOR_TURN: 'wait' '-'? 'for' '-'? 'turn';
WAIT_FOR_MOVE: 'wait' '-'? 'for' '-'? 'move';

SET: 'set';
GET: 'get';

CALL_SCRIPT: 'call' '-'? 'script';
START_SCRIPT: 'start' '-'? 'script';          


EMIT_SFX: 'emit' '-'? 'sfx';
SLEEP: 'sleep';
HIDE: 'hide';
SHOW: 'show';
EXPLODE: 'explode';
TYPE: 'type';

SIGNAL: 'signal';
SET_SIGNAL_MASK: 'set' '-'? 'signal' '-'? 'mask';

ATTACH_UNIT: 'attach' '-'? 'unit';
DROP_UNIT: 'drop' '-'? 'unit';

RETURN: 'return';
CACHE: 'cache';

DONT_CACHE: 'dont' '-'? 'cache';
DONT_SHADOW: 'dont' '-'? 'shadow';
DONT_SHADE: 'dont' '-'? 'shade';
PLAY_SOUND: 'play' '-'? 'sound';

X_AXIS: 'x' AXIS;
Y_AXIS: 'y' AXIS;
Z_AXIS: 'z' AXIS;
fragment AXIS: '-'? 'axis';
RAND: 'rand';

LINEAR_CONSTANT   : '[' '-'? NUMBER ']';
DEGREES_CONSTANT  : '<' '-'? NUMBER '>';
NUMBER: INT | FLOAT;

FLOAT   : DIGIT+ '.' DIGIT*
        | '.' DIGIT+
        ;

INT     : DIGIT+ 
        | '0x' HEX_DIGIT+
        ;

fragment DIGIT     :    [0-9];
fragment HEX_DIGIT :    [0-9a-f];

LINE_DIRECTIVE: '#line ' INT ' ' ~[\r\n]* -> channel(LINE_MACRO);

MULTI_LINE_MACRO: '#' (~[\r\n]*? '\\' [\r\n])+ ~[\r\n]+ -> channel(PREPROCESSOR);
DIRECTIVE: '#' ~[\r\n]* -> channel(PREPROCESSOR);

LINE_COMMENT    : '//' ~[\r\n]* -> channel(COMMENTS);
BLOCK_COMMENT   : '/*' .*? '*/' -> channel(COMMENTS);

WHITESPACE: [ \t\r\n] + -> channel(HIDDEN);
NEWLINE    : ('\r')? '\n' -> channel(HIDDEN);

ID      : [a-z_][a-z_0-9]*;
STRING  : '"' .*? '"';

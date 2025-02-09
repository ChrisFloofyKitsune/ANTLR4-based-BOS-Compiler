parser grammar BosParser;

options {
    tokenVocab = BosLexer;
}

file: declaration*;

declaration
    : pieceDecl 
    | staticVarDecl 
    | funcDecl
    ;

pieceDecl: PIECE pieceName (COMMA pieceName)* SEMICOLON;
pieceName: ID;

staticVarDecl: STATIC_VAR varName (COMMA varName)* SEMICOLON;
varName: ID;

funcDecl: funcName (L_PAREN R_PAREN | L_PAREN argumentList R_PAREN) statementBlock;
funcName: ID;

argumentList: arguments?;
arguments: argName (COMMA argName)*;
argName: ID;

statementBlock
    : '{' statement* '}'
    | statement
    ;

statement
    : keywordStatement SEMICOLON
    | varStatement SEMICOLON
    | ifStatement
    | whileStatement
    | forStatement
    | assignStatement SEMICOLON
    | SEMICOLON
    ;

assignStatement
    : varName '=' expression 
    | incStatement 
    | decStatement
    ;

incStatement: OP_INCREMENT varName;
decStatement: OP_DECREMENT varName;

ifStatement: IF L_PAREN expression R_PAREN statementBlock elseBlock?;
elseBlock: ELSE statementBlock;
whileStatement: WHILE L_PAREN expression R_PAREN statementBlock;
forStatement: FOR L_PAREN expression SEMICOLON expression SEMICOLON expression SEMICOLON? R_PAREN statementBlock;

keywordStatement
    : callStatement
    | startStatement
    | spinStatement
    | stopSpinStatement
    | turnStatement
    | moveStatement
    | waitForTurnStatement
    | waitForMoveStatement
    | emitSfxStatement
    | sleepStatement
    | hideStatement
    | showStatement
    | explodeStatement
    | signalStatement
    | setSignalMaskStatement
    | setStatement
    | getStatement
    | attachUnitStatement
    | dropUnitStatement
    | returnStatement
//    | breakStatement
//    | continueStatement
//    | soundStatement
    | playSoundStatement
//    | stopSoundStatement
//    | missionCommandStatement
    | cacheStatement
    | dontCacheStatement
    | dontShadowStatement
    | dontShadeStatement
    ;

returnStatement     : RETURN expression?;
sleepStatement      : SLEEP expression;
varStatement        : VAR arguments;

setStatement        : SET expression TO expression;
getStatement        : getTerm;

axis  : X_AXIS | Y_AXIS | Z_AXIS;

turnStatement       : TURN pieceName TO axis expression speedOrNow;
moveStatement       : MOVE pieceName TO axis expression speedOrNow;
speedOrNow          : NOW | SPEED expression;

spinStatement       : SPIN pieceName AROUND axis SPEED expression acceleration?;
acceleration        : ACCELERATE expression;

stopSpinStatement   : STOP_SPIN pieceName AROUND axis deceleration?;
deceleration        : DECELERATE expression;

waitForTurnStatement: WAIT_FOR_TURN pieceName AROUND axis;
waitForMoveStatement: WAIT_FOR_MOVE pieceName ALONG axis;

emitSfxStatement    : EMIT_SFX expression FROM pieceName;
playSoundStatement  : PLAY_SOUND L_PAREN stringConstant COMMA expression R_PAREN;

hideStatement       : HIDE pieceName;
showStatement       : SHOW pieceName;
explodeStatement    : EXPLODE pieceName TYPE expression;

callStatement       : CALL_SCRIPT funcName L_PAREN expressionList R_PAREN;
startStatement      : START_SCRIPT funcName L_PAREN expressionList R_PAREN;

signalStatement         : SIGNAL expression;
setSignalMaskStatement  : SET_SIGNAL_MASK expression;

attachUnitStatement :   ATTACH_UNIT expression TO expression;
dropUnitStatement   :   DROP_UNIT expression;

cacheStatement      :   CACHE pieceName;
dontCacheStatement  :   DONT_CACHE pieceName;
dontShadowStatement :   DONT_SHADOW pieceName;
dontShadeStatement  :   DONT_SHADE pieceName;

expressionList  : expressions?;
expressions     : expression commaExpression*;

getTerm : GET term L_PAREN expression commaExpression? commaExpression? commaExpression? R_PAREN | GET term;

commaExpression : (COMMA expression) ;

expression      : term opterm*;

opterm  : op term;
term    
    : getTerm
    | rand 
    | L_PAREN expression R_PAREN 
    | unaryOp term
    | varName
    | constant
    | unknown_unit_value
    ;

rand    : RAND L_PAREN expression COMMA expression R_PAREN;

unaryOp : LOGICAL_NOT | OP_MINUS;
op
    : (OP_MULT | OP_DIV | OP_MOD)
    | (OP_ADD | OP_MINUS)
    | (COMP_LESS | COMP_GREATER | COMP_LESS_EQUAL | COMP_GREATER_EQUAL)
    | (COMP_EQUAL | COMP_NOT_EQUAL)
    | BITWISE_AND
    | BITWISE_OR
    | BITWISE_XOR
    | LOGICAL_AND
    | LOGICAL_OR
    | LOGICAL_XOR
    ;

constant
    : LINEAR_CONSTANT
    | DEGREES_CONSTANT
    | INT
    | FLOAT
    ;

unknown_unit_value: UNKNOWN_UNIT_VALUE L_PAREN INT R_PAREN;

stringConstant: STRING;

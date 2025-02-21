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

funcDecl: funcName (L_PAREN R_PAREN | L_PAREN argName (COMMA argName)* R_PAREN) statementBlock;
funcName: ID;
argName : ID;

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

varStatement: VAR varName (COMMA varName)*;

ifStatement : IF L_PAREN expression R_PAREN statementBlock elseBlock?;
elseBlock   : ELSE statementBlock;

whileStatement  : WHILE L_PAREN expression R_PAREN statementBlock;
forStatement    : FOR L_PAREN expression SEMICOLON expression SEMICOLON expression SEMICOLON? R_PAREN statementBlock;

assignStatement
    : varName EQUAL_ASSIGN expression
    | incStatement
    | decStatement
    ;

incStatement: OP_INCREMENT varName;
decStatement: OP_DECREMENT varName;


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

returnStatement : RETURN | RETURN expression;
sleepStatement  : SLEEP expression;


setStatement: SET valueId=constTerm TO expression;
getStatement: getTerm;

axis  : X_AXIS | Y_AXIS | Z_AXIS;

turnStatement   : TURN pieceName TO axis expression speedOrNow;
moveStatement   : MOVE pieceName TO axis expression speedOrNow;
speedOrNow      : NOW | SPEED expression;

spinStatement   : SPIN pieceName AROUND axis SPEED expression acceleration?;
acceleration    : ACCELERATE expression;

stopSpinStatement   : STOP_SPIN pieceName AROUND axis deceleration?;
deceleration        : DECELERATE expression;

waitForTurnStatement: WAIT_FOR_TURN pieceName AROUND axis;
waitForMoveStatement: WAIT_FOR_MOVE pieceName ALONG axis;

emitSfxStatement    : EMIT_SFX expression FROM pieceName;
playSoundStatement  : PLAY_SOUND L_PAREN stringConstant COMMA expression R_PAREN;

hideStatement   : HIDE pieceName;
showStatement   : SHOW pieceName;
explodeStatement: EXPLODE pieceName TYPE expression;

callStatement   : CALL_SCRIPT funcName (L_PAREN R_PAREN | L_PAREN expressionList R_PAREN);
startStatement  : START_SCRIPT funcName (L_PAREN R_PAREN | L_PAREN expressionList R_PAREN);

signalStatement         : SIGNAL expression;
setSignalMaskStatement  : SET_SIGNAL_MASK expression;

attachUnitStatement :   ATTACH_UNIT expression TO expression;
dropUnitStatement   :   DROP_UNIT expression;

cacheStatement      :   CACHE pieceName;
dontCacheStatement  :   DONT_CACHE pieceName;
dontShadowStatement :   DONT_SHADOW pieceName;
dontShadeStatement  :   DONT_SHADE pieceName;

expressionList  : expression commaExpression*;

getTerm : GET valueId=constTerm | GET valueId=constTerm L_PAREN expression commaExpression? commaExpression? commaExpression? R_PAREN;

commaExpression : (COMMA expression) ;

expression
    : L_PAREN expression R_PAREN                                                #parenExpr
    | constTerm                                                                 #constTermExpr
    | varyingTerm                                                               #varyingTermExpr
    | op=(OP_MINUS | LOGICAL_NOT) operand=expression                            #unaryExpr
    | operand0=expression op=(OP_MULT | OP_DIV | OP_MOD) operand1=expression    #binaryExpr
    | operand0=expression op=(OP_ADD | OP_MINUS) operand1=expression            #binaryExpr
    | operand0=expression                                                       
        op=(COMP_LESS | COMP_GREATER | COMP_LESS_EQUAL | COMP_GREATER_EQUAL)    
        operand1=expression                                                     #binaryExpr
    | operand0=expression op=(COMP_EQUAL | COMP_NOT_EQUAL) operand1=expression  #binaryExpr
    | operand0=expression op=BITWISE_AND operand1=expression                    #binaryExpr
    | operand0=expression op=BITWISE_OR operand1=expression                     #binaryExpr
    | operand0=expression op=BITWISE_XOR operand1=expression                    #binaryExpr
    | operand0=expression op=LOGICAL_AND operand1=expression                    #binaryExpr
    | operand0=expression op=LOGICAL_OR operand1=expression                     #binaryExpr
    | operand0=expression op=LOGICAL_XOR operand1=expression                    #binaryExpr
    ;

constTerm   : constant | L_PAREN constTerm R_PAREN;
varyingTerm : getTerm | rand | varName;

constant
    : LINEAR_CONSTANT
    | DEGREES_CONSTANT
    | NUMBER
    ;

rand: RAND L_PAREN expression COMMA expression R_PAREN;

stringConstant: STRING;

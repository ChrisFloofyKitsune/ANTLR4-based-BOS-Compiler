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
    : L_BRACE statement* R_BRACE
    | statement
    ;

statement
    : keywordStatement SEMICOLON
    | varStatement SEMICOLON
    | ifStatement
    | whileStatement
//    | forStatement
    | assignStatement SEMICOLON
    | returnStatement SEMICOLON
    | emptyStatement
    ;

varStatement: VAR varName (COMMA varName)*;

ifStatement : IF L_PAREN expression R_PAREN statementBlock elseBlock?;
elseBlock   : ELSE statementBlock;

whileStatement  : WHILE L_PAREN expression R_PAREN statementBlock;
//forStatement    : FOR L_PAREN expression SEMICOLON expression SEMICOLON expression SEMICOLON? R_PAREN statementBlock;

assignStatement
    : varName EQUAL_ASSIGN expression
    | incStatement
    | decStatement
    ;

incStatement: OP_INCREMENT varName;
decStatement: OP_DECREMENT varName;

returnStatement : RETURN  | RETURN expression;
emptyStatement: SEMICOLON;

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

sleepStatement  : kw=SLEEP arg1=expression;


setStatement    : kw=SET arg1=expression TO arg2=expression;
// special "no return" version of get call done for side effects
getStatement    : kw=GET arg1=getCall;

axis  : X_AXIS | Y_AXIS | Z_AXIS;

turnStatement   : kw=TURN arg1=pieceName TO arg2=axis arg3=expression arg4=speedOrNow;
moveStatement   : kw=MOVE arg1=pieceName TO arg2=axis arg3=expression arg4=speedOrNow;
speedOrNow      : NOW | SPEED expression;

spinStatement   : kw=SPIN arg1=pieceName AROUND arg2=axis SPEED arg3=expression arg4=acceleration?;
acceleration    : ACCELERATE expression;

stopSpinStatement   : kw=STOP_SPIN arg1=pieceName AROUND arg2=axis arg3=deceleration?;
deceleration        : DECELERATE expression;

waitForTurnStatement: kw=WAIT_FOR_TURN arg1=pieceName AROUND arg2=axis;
waitForMoveStatement: kw=WAIT_FOR_MOVE arg1=pieceName ALONG arg2=axis;

emitSfxStatement    : kw=EMIT_SFX arg1=expression FROM arg2=pieceName;
playSoundStatement  : kw=PLAY_SOUND L_PAREN arg1=stringConstant COMMA arg2=expression R_PAREN;

hideStatement   : kw=HIDE arg1=pieceName;
showStatement   : kw=SHOW arg1=pieceName;
explodeStatement: kw=EXPLODE arg1=pieceName TYPE arg2=expression;

callStatement   : kw=CALL_SCRIPT arg1=funcName (L_PAREN R_PAREN | L_PAREN expressionList R_PAREN);
startStatement  : kw=START_SCRIPT arg1=funcName (L_PAREN R_PAREN | L_PAREN expressionList R_PAREN);

signalStatement         : kw=SIGNAL arg1=expression;
setSignalMaskStatement  : kw=SET_SIGNAL_MASK arg1=expression;

attachUnitStatement :   kw=ATTACH_UNIT arg1=expression TO arg2=expression;
dropUnitStatement   :   kw=DROP_UNIT arg1=expression;

cacheStatement      :   kw=CACHE arg1=pieceName;
dontCacheStatement  :   kw=DONT_CACHE arg1=pieceName;
dontShadowStatement :   kw=DONT_SHADOW arg1=pieceName;
dontShadeStatement  :   kw=DONT_SHADE arg1=pieceName;

expressionList  : expression commaExpression*;


commaExpression : (COMMA expression) ;

expression
    : L_PAREN expression R_PAREN                                                #parenExpr
    | constTerm                                                                 #constTermExpr
    | varyingTerm                                                               #varyingTermExpr
//    | op=(OP_MINUS | LOGICAL_NOT) operand=expression                            #unaryExpr
    | op=LOGICAL_NOT operand=expression                                         #unaryExpr
    | operand1=expression op=(OP_MULT | OP_DIV | OP_MOD) operand2=expression    #binaryExpr
    | operand1=expression op=(OP_ADD | OP_MINUS) operand2=expression            #binaryExpr
    | operand1=expression                                                       
        op=(COMP_LESS | COMP_GREATER | COMP_LESS_EQUAL | COMP_GREATER_EQUAL)    
        operand2=expression                                                     #binaryExpr
    | operand1=expression op=(COMP_EQUAL | COMP_NOT_EQUAL) operand2=expression  #binaryExpr
    | operand1=expression op=BITWISE_AND operand2=expression                    #binaryExpr
    | operand1=expression op=BITWISE_OR operand2=expression                     #binaryExpr
    | operand1=expression op=BITWISE_XOR operand2=expression                    #binaryExpr
    | operand1=expression op=LOGICAL_AND operand2=expression                    #binaryExpr
    | operand1=expression op=LOGICAL_OR operand2=expression                     #binaryExpr
    | operand1=expression op=LOGICAL_XOR operand2=expression                    #binaryExpr
    ;

constTerm   : constant | L_PAREN constTerm R_PAREN;

varyingTerm : getTerm | randTerm | varNameTerm;
getTerm     : GET getCall;
randTerm    : RAND L_PAREN expression COMMA expression R_PAREN;
varNameTerm : varName;

getCall: value_idx=expression | value_idx=expression L_PAREN arg1=expression arg2=commaExpression? arg3=commaExpression? arg4=commaExpression? R_PAREN;

constant
    : LINEAR_CONSTANT
    | DEGREES_CONSTANT
    | '-'? INT
    | '-'? FLOAT
    ;


stringConstant: STRING;

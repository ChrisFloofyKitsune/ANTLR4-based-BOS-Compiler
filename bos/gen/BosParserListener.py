# Generated from E:/antlr_domain_specifc_lang_stuff/book/part2/bos/BosParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BosParser import BosParser
else:
    from BosParser import BosParser

# This class defines a complete listener for a parse tree produced by BosParser.
class BosParserListener(ParseTreeListener):

    # Enter a parse tree produced by BosParser#file.
    def enterFile(self, ctx:BosParser.FileContext):
        pass

    # Exit a parse tree produced by BosParser#file.
    def exitFile(self, ctx:BosParser.FileContext):
        pass


    # Enter a parse tree produced by BosParser#declaration.
    def enterDeclaration(self, ctx:BosParser.DeclarationContext):
        pass

    # Exit a parse tree produced by BosParser#declaration.
    def exitDeclaration(self, ctx:BosParser.DeclarationContext):
        pass


    # Enter a parse tree produced by BosParser#pieceDecl.
    def enterPieceDecl(self, ctx:BosParser.PieceDeclContext):
        pass

    # Exit a parse tree produced by BosParser#pieceDecl.
    def exitPieceDecl(self, ctx:BosParser.PieceDeclContext):
        pass


    # Enter a parse tree produced by BosParser#pieceName.
    def enterPieceName(self, ctx:BosParser.PieceNameContext):
        pass

    # Exit a parse tree produced by BosParser#pieceName.
    def exitPieceName(self, ctx:BosParser.PieceNameContext):
        pass


    # Enter a parse tree produced by BosParser#staticVarDecl.
    def enterStaticVarDecl(self, ctx:BosParser.StaticVarDeclContext):
        pass

    # Exit a parse tree produced by BosParser#staticVarDecl.
    def exitStaticVarDecl(self, ctx:BosParser.StaticVarDeclContext):
        pass


    # Enter a parse tree produced by BosParser#varName.
    def enterVarName(self, ctx:BosParser.VarNameContext):
        pass

    # Exit a parse tree produced by BosParser#varName.
    def exitVarName(self, ctx:BosParser.VarNameContext):
        pass


    # Enter a parse tree produced by BosParser#funcDecl.
    def enterFuncDecl(self, ctx:BosParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by BosParser#funcDecl.
    def exitFuncDecl(self, ctx:BosParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by BosParser#funcName.
    def enterFuncName(self, ctx:BosParser.FuncNameContext):
        pass

    # Exit a parse tree produced by BosParser#funcName.
    def exitFuncName(self, ctx:BosParser.FuncNameContext):
        pass


    # Enter a parse tree produced by BosParser#argumentList.
    def enterArgumentList(self, ctx:BosParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by BosParser#argumentList.
    def exitArgumentList(self, ctx:BosParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by BosParser#arguments.
    def enterArguments(self, ctx:BosParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by BosParser#arguments.
    def exitArguments(self, ctx:BosParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by BosParser#argName.
    def enterArgName(self, ctx:BosParser.ArgNameContext):
        pass

    # Exit a parse tree produced by BosParser#argName.
    def exitArgName(self, ctx:BosParser.ArgNameContext):
        pass


    # Enter a parse tree produced by BosParser#statementBlock.
    def enterStatementBlock(self, ctx:BosParser.StatementBlockContext):
        pass

    # Exit a parse tree produced by BosParser#statementBlock.
    def exitStatementBlock(self, ctx:BosParser.StatementBlockContext):
        pass


    # Enter a parse tree produced by BosParser#statement.
    def enterStatement(self, ctx:BosParser.StatementContext):
        pass

    # Exit a parse tree produced by BosParser#statement.
    def exitStatement(self, ctx:BosParser.StatementContext):
        pass


    # Enter a parse tree produced by BosParser#assignStatement.
    def enterAssignStatement(self, ctx:BosParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by BosParser#assignStatement.
    def exitAssignStatement(self, ctx:BosParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by BosParser#incStatement.
    def enterIncStatement(self, ctx:BosParser.IncStatementContext):
        pass

    # Exit a parse tree produced by BosParser#incStatement.
    def exitIncStatement(self, ctx:BosParser.IncStatementContext):
        pass


    # Enter a parse tree produced by BosParser#decStatement.
    def enterDecStatement(self, ctx:BosParser.DecStatementContext):
        pass

    # Exit a parse tree produced by BosParser#decStatement.
    def exitDecStatement(self, ctx:BosParser.DecStatementContext):
        pass


    # Enter a parse tree produced by BosParser#ifStatement.
    def enterIfStatement(self, ctx:BosParser.IfStatementContext):
        pass

    # Exit a parse tree produced by BosParser#ifStatement.
    def exitIfStatement(self, ctx:BosParser.IfStatementContext):
        pass


    # Enter a parse tree produced by BosParser#elseBlock.
    def enterElseBlock(self, ctx:BosParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by BosParser#elseBlock.
    def exitElseBlock(self, ctx:BosParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by BosParser#whileStatement.
    def enterWhileStatement(self, ctx:BosParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by BosParser#whileStatement.
    def exitWhileStatement(self, ctx:BosParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by BosParser#forStatement.
    def enterForStatement(self, ctx:BosParser.ForStatementContext):
        pass

    # Exit a parse tree produced by BosParser#forStatement.
    def exitForStatement(self, ctx:BosParser.ForStatementContext):
        pass


    # Enter a parse tree produced by BosParser#keywordStatement.
    def enterKeywordStatement(self, ctx:BosParser.KeywordStatementContext):
        pass

    # Exit a parse tree produced by BosParser#keywordStatement.
    def exitKeywordStatement(self, ctx:BosParser.KeywordStatementContext):
        pass


    # Enter a parse tree produced by BosParser#returnStatement.
    def enterReturnStatement(self, ctx:BosParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by BosParser#returnStatement.
    def exitReturnStatement(self, ctx:BosParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by BosParser#sleepStatement.
    def enterSleepStatement(self, ctx:BosParser.SleepStatementContext):
        pass

    # Exit a parse tree produced by BosParser#sleepStatement.
    def exitSleepStatement(self, ctx:BosParser.SleepStatementContext):
        pass


    # Enter a parse tree produced by BosParser#varStatement.
    def enterVarStatement(self, ctx:BosParser.VarStatementContext):
        pass

    # Exit a parse tree produced by BosParser#varStatement.
    def exitVarStatement(self, ctx:BosParser.VarStatementContext):
        pass


    # Enter a parse tree produced by BosParser#setStatement.
    def enterSetStatement(self, ctx:BosParser.SetStatementContext):
        pass

    # Exit a parse tree produced by BosParser#setStatement.
    def exitSetStatement(self, ctx:BosParser.SetStatementContext):
        pass


    # Enter a parse tree produced by BosParser#getStatement.
    def enterGetStatement(self, ctx:BosParser.GetStatementContext):
        pass

    # Exit a parse tree produced by BosParser#getStatement.
    def exitGetStatement(self, ctx:BosParser.GetStatementContext):
        pass


    # Enter a parse tree produced by BosParser#axis.
    def enterAxis(self, ctx:BosParser.AxisContext):
        pass

    # Exit a parse tree produced by BosParser#axis.
    def exitAxis(self, ctx:BosParser.AxisContext):
        pass


    # Enter a parse tree produced by BosParser#turnStatement.
    def enterTurnStatement(self, ctx:BosParser.TurnStatementContext):
        pass

    # Exit a parse tree produced by BosParser#turnStatement.
    def exitTurnStatement(self, ctx:BosParser.TurnStatementContext):
        pass


    # Enter a parse tree produced by BosParser#moveStatement.
    def enterMoveStatement(self, ctx:BosParser.MoveStatementContext):
        pass

    # Exit a parse tree produced by BosParser#moveStatement.
    def exitMoveStatement(self, ctx:BosParser.MoveStatementContext):
        pass


    # Enter a parse tree produced by BosParser#speedOrNow.
    def enterSpeedOrNow(self, ctx:BosParser.SpeedOrNowContext):
        pass

    # Exit a parse tree produced by BosParser#speedOrNow.
    def exitSpeedOrNow(self, ctx:BosParser.SpeedOrNowContext):
        pass


    # Enter a parse tree produced by BosParser#spinStatement.
    def enterSpinStatement(self, ctx:BosParser.SpinStatementContext):
        pass

    # Exit a parse tree produced by BosParser#spinStatement.
    def exitSpinStatement(self, ctx:BosParser.SpinStatementContext):
        pass


    # Enter a parse tree produced by BosParser#acceleration.
    def enterAcceleration(self, ctx:BosParser.AccelerationContext):
        pass

    # Exit a parse tree produced by BosParser#acceleration.
    def exitAcceleration(self, ctx:BosParser.AccelerationContext):
        pass


    # Enter a parse tree produced by BosParser#stopSpinStatement.
    def enterStopSpinStatement(self, ctx:BosParser.StopSpinStatementContext):
        pass

    # Exit a parse tree produced by BosParser#stopSpinStatement.
    def exitStopSpinStatement(self, ctx:BosParser.StopSpinStatementContext):
        pass


    # Enter a parse tree produced by BosParser#deceleration.
    def enterDeceleration(self, ctx:BosParser.DecelerationContext):
        pass

    # Exit a parse tree produced by BosParser#deceleration.
    def exitDeceleration(self, ctx:BosParser.DecelerationContext):
        pass


    # Enter a parse tree produced by BosParser#waitForTurnStatement.
    def enterWaitForTurnStatement(self, ctx:BosParser.WaitForTurnStatementContext):
        pass

    # Exit a parse tree produced by BosParser#waitForTurnStatement.
    def exitWaitForTurnStatement(self, ctx:BosParser.WaitForTurnStatementContext):
        pass


    # Enter a parse tree produced by BosParser#waitForMoveStatement.
    def enterWaitForMoveStatement(self, ctx:BosParser.WaitForMoveStatementContext):
        pass

    # Exit a parse tree produced by BosParser#waitForMoveStatement.
    def exitWaitForMoveStatement(self, ctx:BosParser.WaitForMoveStatementContext):
        pass


    # Enter a parse tree produced by BosParser#emitSfxStatement.
    def enterEmitSfxStatement(self, ctx:BosParser.EmitSfxStatementContext):
        pass

    # Exit a parse tree produced by BosParser#emitSfxStatement.
    def exitEmitSfxStatement(self, ctx:BosParser.EmitSfxStatementContext):
        pass


    # Enter a parse tree produced by BosParser#playSoundStatement.
    def enterPlaySoundStatement(self, ctx:BosParser.PlaySoundStatementContext):
        pass

    # Exit a parse tree produced by BosParser#playSoundStatement.
    def exitPlaySoundStatement(self, ctx:BosParser.PlaySoundStatementContext):
        pass


    # Enter a parse tree produced by BosParser#hideStatement.
    def enterHideStatement(self, ctx:BosParser.HideStatementContext):
        pass

    # Exit a parse tree produced by BosParser#hideStatement.
    def exitHideStatement(self, ctx:BosParser.HideStatementContext):
        pass


    # Enter a parse tree produced by BosParser#showStatement.
    def enterShowStatement(self, ctx:BosParser.ShowStatementContext):
        pass

    # Exit a parse tree produced by BosParser#showStatement.
    def exitShowStatement(self, ctx:BosParser.ShowStatementContext):
        pass


    # Enter a parse tree produced by BosParser#explodeStatement.
    def enterExplodeStatement(self, ctx:BosParser.ExplodeStatementContext):
        pass

    # Exit a parse tree produced by BosParser#explodeStatement.
    def exitExplodeStatement(self, ctx:BosParser.ExplodeStatementContext):
        pass


    # Enter a parse tree produced by BosParser#callStatement.
    def enterCallStatement(self, ctx:BosParser.CallStatementContext):
        pass

    # Exit a parse tree produced by BosParser#callStatement.
    def exitCallStatement(self, ctx:BosParser.CallStatementContext):
        pass


    # Enter a parse tree produced by BosParser#startStatement.
    def enterStartStatement(self, ctx:BosParser.StartStatementContext):
        pass

    # Exit a parse tree produced by BosParser#startStatement.
    def exitStartStatement(self, ctx:BosParser.StartStatementContext):
        pass


    # Enter a parse tree produced by BosParser#signalStatement.
    def enterSignalStatement(self, ctx:BosParser.SignalStatementContext):
        pass

    # Exit a parse tree produced by BosParser#signalStatement.
    def exitSignalStatement(self, ctx:BosParser.SignalStatementContext):
        pass


    # Enter a parse tree produced by BosParser#setSignalMaskStatement.
    def enterSetSignalMaskStatement(self, ctx:BosParser.SetSignalMaskStatementContext):
        pass

    # Exit a parse tree produced by BosParser#setSignalMaskStatement.
    def exitSetSignalMaskStatement(self, ctx:BosParser.SetSignalMaskStatementContext):
        pass


    # Enter a parse tree produced by BosParser#attachUnitStatement.
    def enterAttachUnitStatement(self, ctx:BosParser.AttachUnitStatementContext):
        pass

    # Exit a parse tree produced by BosParser#attachUnitStatement.
    def exitAttachUnitStatement(self, ctx:BosParser.AttachUnitStatementContext):
        pass


    # Enter a parse tree produced by BosParser#dropUnitStatement.
    def enterDropUnitStatement(self, ctx:BosParser.DropUnitStatementContext):
        pass

    # Exit a parse tree produced by BosParser#dropUnitStatement.
    def exitDropUnitStatement(self, ctx:BosParser.DropUnitStatementContext):
        pass


    # Enter a parse tree produced by BosParser#cacheStatement.
    def enterCacheStatement(self, ctx:BosParser.CacheStatementContext):
        pass

    # Exit a parse tree produced by BosParser#cacheStatement.
    def exitCacheStatement(self, ctx:BosParser.CacheStatementContext):
        pass


    # Enter a parse tree produced by BosParser#dontCacheStatement.
    def enterDontCacheStatement(self, ctx:BosParser.DontCacheStatementContext):
        pass

    # Exit a parse tree produced by BosParser#dontCacheStatement.
    def exitDontCacheStatement(self, ctx:BosParser.DontCacheStatementContext):
        pass


    # Enter a parse tree produced by BosParser#dontShadowStatement.
    def enterDontShadowStatement(self, ctx:BosParser.DontShadowStatementContext):
        pass

    # Exit a parse tree produced by BosParser#dontShadowStatement.
    def exitDontShadowStatement(self, ctx:BosParser.DontShadowStatementContext):
        pass


    # Enter a parse tree produced by BosParser#dontShadeStatement.
    def enterDontShadeStatement(self, ctx:BosParser.DontShadeStatementContext):
        pass

    # Exit a parse tree produced by BosParser#dontShadeStatement.
    def exitDontShadeStatement(self, ctx:BosParser.DontShadeStatementContext):
        pass


    # Enter a parse tree produced by BosParser#expressionList.
    def enterExpressionList(self, ctx:BosParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by BosParser#expressionList.
    def exitExpressionList(self, ctx:BosParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by BosParser#expressions.
    def enterExpressions(self, ctx:BosParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by BosParser#expressions.
    def exitExpressions(self, ctx:BosParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by BosParser#getTerm.
    def enterGetTerm(self, ctx:BosParser.GetTermContext):
        pass

    # Exit a parse tree produced by BosParser#getTerm.
    def exitGetTerm(self, ctx:BosParser.GetTermContext):
        pass


    # Enter a parse tree produced by BosParser#commaExpression.
    def enterCommaExpression(self, ctx:BosParser.CommaExpressionContext):
        pass

    # Exit a parse tree produced by BosParser#commaExpression.
    def exitCommaExpression(self, ctx:BosParser.CommaExpressionContext):
        pass


    # Enter a parse tree produced by BosParser#expression.
    def enterExpression(self, ctx:BosParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BosParser#expression.
    def exitExpression(self, ctx:BosParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BosParser#opterm.
    def enterOpterm(self, ctx:BosParser.OptermContext):
        pass

    # Exit a parse tree produced by BosParser#opterm.
    def exitOpterm(self, ctx:BosParser.OptermContext):
        pass


    # Enter a parse tree produced by BosParser#term.
    def enterTerm(self, ctx:BosParser.TermContext):
        pass

    # Exit a parse tree produced by BosParser#term.
    def exitTerm(self, ctx:BosParser.TermContext):
        pass


    # Enter a parse tree produced by BosParser#rand.
    def enterRand(self, ctx:BosParser.RandContext):
        pass

    # Exit a parse tree produced by BosParser#rand.
    def exitRand(self, ctx:BosParser.RandContext):
        pass


    # Enter a parse tree produced by BosParser#unaryOp.
    def enterUnaryOp(self, ctx:BosParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by BosParser#unaryOp.
    def exitUnaryOp(self, ctx:BosParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by BosParser#op.
    def enterOp(self, ctx:BosParser.OpContext):
        pass

    # Exit a parse tree produced by BosParser#op.
    def exitOp(self, ctx:BosParser.OpContext):
        pass


    # Enter a parse tree produced by BosParser#constant.
    def enterConstant(self, ctx:BosParser.ConstantContext):
        pass

    # Exit a parse tree produced by BosParser#constant.
    def exitConstant(self, ctx:BosParser.ConstantContext):
        pass


    # Enter a parse tree produced by BosParser#unknown_unit_value.
    def enterUnknown_unit_value(self, ctx:BosParser.Unknown_unit_valueContext):
        pass

    # Exit a parse tree produced by BosParser#unknown_unit_value.
    def exitUnknown_unit_value(self, ctx:BosParser.Unknown_unit_valueContext):
        pass


    # Enter a parse tree produced by BosParser#stringConstant.
    def enterStringConstant(self, ctx:BosParser.StringConstantContext):
        pass

    # Exit a parse tree produced by BosParser#stringConstant.
    def exitStringConstant(self, ctx:BosParser.StringConstantContext):
        pass



del BosParser
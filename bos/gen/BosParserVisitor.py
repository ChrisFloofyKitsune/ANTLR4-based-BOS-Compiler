# Generated from E:/antlr_domain_specifc_lang_stuff/book/part2/bos/BosParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BosParser import BosParser
else:
    from BosParser import BosParser

# This class defines a complete generic visitor for a parse tree produced by BosParser.

class BosParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BosParser#file.
    def visitFile(self, ctx:BosParser.FileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#declaration.
    def visitDeclaration(self, ctx:BosParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#pieceDecl.
    def visitPieceDecl(self, ctx:BosParser.PieceDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#pieceName.
    def visitPieceName(self, ctx:BosParser.PieceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#staticVarDecl.
    def visitStaticVarDecl(self, ctx:BosParser.StaticVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#varName.
    def visitVarName(self, ctx:BosParser.VarNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#funcDecl.
    def visitFuncDecl(self, ctx:BosParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#funcName.
    def visitFuncName(self, ctx:BosParser.FuncNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#argumentList.
    def visitArgumentList(self, ctx:BosParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#arguments.
    def visitArguments(self, ctx:BosParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#argName.
    def visitArgName(self, ctx:BosParser.ArgNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#statementBlock.
    def visitStatementBlock(self, ctx:BosParser.StatementBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#statement.
    def visitStatement(self, ctx:BosParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#assignStatement.
    def visitAssignStatement(self, ctx:BosParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#incStatement.
    def visitIncStatement(self, ctx:BosParser.IncStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#decStatement.
    def visitDecStatement(self, ctx:BosParser.DecStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#ifStatement.
    def visitIfStatement(self, ctx:BosParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#elseBlock.
    def visitElseBlock(self, ctx:BosParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#whileStatement.
    def visitWhileStatement(self, ctx:BosParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#forStatement.
    def visitForStatement(self, ctx:BosParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#keywordStatement.
    def visitKeywordStatement(self, ctx:BosParser.KeywordStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#returnStatement.
    def visitReturnStatement(self, ctx:BosParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#sleepStatement.
    def visitSleepStatement(self, ctx:BosParser.SleepStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#varStatement.
    def visitVarStatement(self, ctx:BosParser.VarStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#setStatement.
    def visitSetStatement(self, ctx:BosParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#getStatement.
    def visitGetStatement(self, ctx:BosParser.GetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#axis.
    def visitAxis(self, ctx:BosParser.AxisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#turnStatement.
    def visitTurnStatement(self, ctx:BosParser.TurnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#moveStatement.
    def visitMoveStatement(self, ctx:BosParser.MoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#speedOrNow.
    def visitSpeedOrNow(self, ctx:BosParser.SpeedOrNowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#spinStatement.
    def visitSpinStatement(self, ctx:BosParser.SpinStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#acceleration.
    def visitAcceleration(self, ctx:BosParser.AccelerationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#stopSpinStatement.
    def visitStopSpinStatement(self, ctx:BosParser.StopSpinStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#deceleration.
    def visitDeceleration(self, ctx:BosParser.DecelerationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#waitForTurnStatement.
    def visitWaitForTurnStatement(self, ctx:BosParser.WaitForTurnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#waitForMoveStatement.
    def visitWaitForMoveStatement(self, ctx:BosParser.WaitForMoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#emitSfxStatement.
    def visitEmitSfxStatement(self, ctx:BosParser.EmitSfxStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#playSoundStatement.
    def visitPlaySoundStatement(self, ctx:BosParser.PlaySoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#hideStatement.
    def visitHideStatement(self, ctx:BosParser.HideStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#showStatement.
    def visitShowStatement(self, ctx:BosParser.ShowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#explodeStatement.
    def visitExplodeStatement(self, ctx:BosParser.ExplodeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#callStatement.
    def visitCallStatement(self, ctx:BosParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#startStatement.
    def visitStartStatement(self, ctx:BosParser.StartStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#signalStatement.
    def visitSignalStatement(self, ctx:BosParser.SignalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#setSignalMaskStatement.
    def visitSetSignalMaskStatement(self, ctx:BosParser.SetSignalMaskStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#attachUnitStatement.
    def visitAttachUnitStatement(self, ctx:BosParser.AttachUnitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#dropUnitStatement.
    def visitDropUnitStatement(self, ctx:BosParser.DropUnitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#cacheStatement.
    def visitCacheStatement(self, ctx:BosParser.CacheStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#dontCacheStatement.
    def visitDontCacheStatement(self, ctx:BosParser.DontCacheStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#dontShadowStatement.
    def visitDontShadowStatement(self, ctx:BosParser.DontShadowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#dontShadeStatement.
    def visitDontShadeStatement(self, ctx:BosParser.DontShadeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#expressionList.
    def visitExpressionList(self, ctx:BosParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#expressions.
    def visitExpressions(self, ctx:BosParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#getTerm.
    def visitGetTerm(self, ctx:BosParser.GetTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#commaExpression.
    def visitCommaExpression(self, ctx:BosParser.CommaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#expression.
    def visitExpression(self, ctx:BosParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#opterm.
    def visitOpterm(self, ctx:BosParser.OptermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#term.
    def visitTerm(self, ctx:BosParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#rand.
    def visitRand(self, ctx:BosParser.RandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#unaryOp.
    def visitUnaryOp(self, ctx:BosParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#op.
    def visitOp(self, ctx:BosParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#constant.
    def visitConstant(self, ctx:BosParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#unknown_unit_value.
    def visitUnknown_unit_value(self, ctx:BosParser.Unknown_unit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BosParser#stringConstant.
    def visitStringConstant(self, ctx:BosParser.StringConstantContext):
        return self.visitChildren(ctx)



del BosParser
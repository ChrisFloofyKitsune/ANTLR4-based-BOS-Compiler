import inspect
import json
from enum import Enum
from numbers import Number
from types import GenericAlias
from typing import TypeVar, Generic, Literal

from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.ParserRuleContext import ParserRuleContext
from antlr4.tree.Tree import ParseTree, TerminalNode

from bos.gen.BosLexer import BosLexer
from bos.gen.BosParser import BosParser
from bos.gen.BosParserVisitor import BosParserVisitor

NodeValT = TypeVar('NodeValT')
class ASTNode(Generic[NodeValT]):
    def __init__(self, value: NodeValT):
        self.name = self.__class__.__name__
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.value)})'

class UndefNode(ASTNode[any]):
    def __init__(self, name: str, value: any):
        super().__init__(value)
        self.name = f'Undef__{name}'

class PieceName(ASTNode[str]):
    ...

DeclarationT = TypeVar('DeclarationT')
class Declaration(ASTNode[DeclarationT]):
    ...

class PieceDeclaration(Declaration[list[PieceName]]):
    ...

class VarName(ASTNode[str]):
    ...

class StaticVarDeclaration(Declaration[list[VarName]]):
    ...

class FuncName(ASTNode[str]):
    ...

class Constant(ASTNode[Number]):
    def __init__(self, value: Number | str):
        self.const_type: Literal['normal', 'angular', 'linear'] = 'normal'
        if isinstance(value, str):
            if value[0] == '[' and value[-1] == ']':
                self.const_type = 'linear'
            elif value[0] == '<' and value[-1] == '>':
                self.const_type = 'angular'
            value = value.strip('[]<>')
            value = float(value) if '.' in value else int(value)
        super().__init__(value)
    
    def __repr__(self):
        if self.const_type == 'normal':
            return f'Constant({self.value})'
        if self.const_type == 'angular':
            return f'Constant(\'<{self.value}>\')'
        if self.const_type == 'linear':
            return f'Constant(\'[{self.value}]\')'

class AxisEnum(Enum):
    X = 1
    Y = 2
    Z = 3
    
    @classmethod
    def from_str(cls, string: str):
        if 'x' in string or 'X' in string:
            return AxisEnum.X
        if 'y' in string or 'Y' in string:
            return AxisEnum.Y
        if 'z' in string or 'Z' in string:
            return AxisEnum.Z
        
        return None
        
class Axis(ASTNode[AxisEnum]):
    ...

class ArgName(ASTNode[str]):
    ...

class ASTVisitor(BosParserVisitor):
    
    def aggregateResult(self, aggregate, next_result):
        if next_result is None:
            return aggregate
        
        if aggregate is None:
            return next_result
        
        if not isinstance(aggregate, list):
            return [aggregate, next_result]
        
        return [*aggregate, next_result]
    
    def visitChildren(self, node):
        result = super().visitChildren(node)
        if isinstance(result, ASTNode):
            return result
        return UndefNode(node.__class__.__name__.removesuffix('Context'), result)
    
    def visitTypedChildren(self, node: ParserRuleContext, child_type: type[ParserRuleContext]):
        result = []
        for child in node.getTypedRuleContexts(child_type):
            result.append(self.visit(child))
        return result
    
    def visitPieceName(self, ctx:BosParser.PieceNameContext):
        return PieceName(ctx.getText())
    
    def visitPieceDecl(self, ctx:BosParser.PieceDeclContext):
        return PieceDeclaration(self.visitTypedChildren(ctx, BosParser.PieceNameContext))
    
    def visitVarName(self, ctx:BosParser.VarNameContext):
        return VarName(ctx.getText())
    
    def visitStaticVarDecl(self, ctx:BosParser.StaticVarDeclContext):
        return StaticVarDeclaration(self.visitTypedChildren(ctx, BosParser.VarNameContext))
    
    def visitFuncName(self, ctx:BosParser.FuncNameContext):
        return FuncName(ctx.getText())
    
    def visitConstant(self, ctx:BosParser.ConstantContext):
        return Constant(ctx.getText())
    
    def visitAxis(self, ctx:BosParser.AxisContext):
        return Axis(AxisEnum.from_str(ctx.getText()))
    
    def visitArgName(self, ctx:BosParser.ArgNameContext):
        return ArgName(ctx.getText())

def main():
    with open('./bos/preprocessed/legcom.pcpp', 'rt', encoding='utf8') as file:
        str_data = file.read()

    input_stream = InputStream(str_data)
    lexer = BosLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = BosParser(tokens)

    token_tree: BosParser.FileContext = parser.file_()
    visitor = ASTVisitor()

    ast = visitor.visit(token_tree)
    print(json.dumps(ast, indent=2, default=lambda x: {x.name: x.value} if not isinstance(x.value, (int, float, str, tuple, Enum)) else repr(x)))

if __name__ == '__main__':
    main()

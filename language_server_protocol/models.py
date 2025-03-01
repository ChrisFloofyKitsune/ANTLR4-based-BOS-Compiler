import enum
from functools import total_ordering

from lsprotocol import types as lsp_types
from pydantic import BaseModel, Field

from code_location import CodeLocation


class TokenType(enum.IntEnum):
    Comment = 0, lsp_types.SemanticTokenTypes.Comment
    Macro = enum.auto(), lsp_types.SemanticTokenTypes.Macro
    Keyword = enum.auto(), lsp_types.SemanticTokenTypes.Keyword
    Variable = enum.auto(), lsp_types.SemanticTokenTypes.Variable
    Function = enum.auto(), lsp_types.SemanticTokenTypes.Function
    Parameter = enum.auto(), lsp_types.SemanticTokenTypes.Function
    Number = enum.auto(), lsp_types.SemanticTokenTypes.Number
    Operator = enum.auto(), lsp_types.SemanticTokenTypes.Operator
    Enum = enum.auto(), lsp_types.SemanticTokenTypes.Enum
    EnumMember = enum.auto(), lsp_types.SemanticTokenTypes.EnumMember

    def __new__(cls, value, str_value):
        obj = int.__new__(cls)
        obj._value_ = value
        obj._str_value_ = str_value
        return obj

    @enum.property
    def int_value(self):
        return self._value_

    @enum.property
    def str_value(self):
        return self._str_value_


class TokenModifier(enum.IntFlag):
    Declaration = enum.auto(), lsp_types.SemanticTokenModifiers.Declaration
    Definition = enum.auto(), lsp_types.SemanticTokenModifiers.Definition
    ReadOnly = enum.auto(), lsp_types.SemanticTokenModifiers.Readonly
    DefaultLibrary = enum.auto(), lsp_types.SemanticTokenModifiers.DefaultLibrary
    Static = enum.auto(), lsp_types.SemanticTokenModifiers.Static

    def __new__(cls, value, str_value):
        obj = int.__new__(cls)
        obj._value_ = value
        obj._str_value_ = str_value
        return obj

    @enum.property
    def int_value(self):
        return self._value_

    @enum.property
    def str_value(self):
        return self._str_value_


@total_ordering
class LspToken(BaseModel):
    code_location: CodeLocation
    token_type: TokenType
    token_modifiers: list[TokenModifier] = Field(default_factory=list)
    
    def __eq__(self, other):
        return self.code_location == other.code_location and self.token_type == other.token_type
    
    def __lt__(self, other):
        return self.code_location < other.code_location
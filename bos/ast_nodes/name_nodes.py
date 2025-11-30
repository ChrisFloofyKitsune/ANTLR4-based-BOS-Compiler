from bos.ast_nodes.base_nodes import ValueNode


class NameNode(ValueNode):
    name: str

    def __eq__(self, other):
        return isinstance(other, NameNode) and self.name.lower() == other.name.lower()

    def __hash__(self):
        return hash(self.name.lower())

    def __repr__(self):
        return f'{self.node_name}(\'{self.name}\')'

    def __str__(self):
        return self.name


class PieceName(NameNode):
    ...


class VarName(NameNode):
    ...


class FuncName(NameNode):
    ...


class ArgName(NameNode):
    ...

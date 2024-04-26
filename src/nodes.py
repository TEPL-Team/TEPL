class Stmt:
    pass


class Expr:
    pass


class BinOp(Expr):

    def __init__(self, left, op, right):
        self.type = "binop"
        self.left = left
        self.right = right
        self.op = op

    def __repr__(self):
        return f"BinOp({self.left}, '{self.op}', {self.right})"


class Number(Expr):

    def __init__(self, value):
        self.type = "number"
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class Boolean(Expr):

    def __init__(self, value):
        self.type = "boolean"
        self.value = value

    def __repr__(self):
        return f"Boolean({self.value})"


class Identifier(Expr):

    def __init__(self, name):
        self.type = "identifier"
        self.name = name

    def __repr__(self):
        return f"Identifier({self.name})"


class Output(Stmt):

    def __init__(self, expr):
        self.type = "output"
        self.expr = expr

    def __repr__(self):
        return f"Output({self.expr})"


class Assignment(Stmt):

    def __init__(self, name: Identifier, value):
        self.type = "assignment"
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Assignment({self.name} {self.value})"


class Random(Stmt):

    def __init__(self, _t, _1, _2):
        self.type = "random"
        self._from = _1
        self.to = _2
        self._type = _t

    def __repr__(self):
        return f"Random({self._type} {self._from} {self.to})"


class Input(Expr):

    def __init__(self, question, _T):
        self.type = "input"
        self.q = question
        self.t = _T

    def __repr__(self):
        return f"Input({self.q} {self.t})"


class Comparism(Expr):

    def __init__(self, left, op, right):
        self.type = "comp"
        self.left = left
        self.right = right
        self.op = op

    def __repr__(self):
        return f"Comparison({self.left} {self.op} {self.right})"


class If(Stmt):

    def __init__(self,
                 condition: Comparism,
                 body,
                 Conelse=False,
                 Else_Body=None):
        self.type = "if"
        self.condition = condition
        self.body = body
        self.conelse = Conelse
        self.elsebody = Else_Body

    def __repr__(self):
        if self.elsebody is None:
            return f"If({self.condition} {self.body})"
        else:
            return f"If({self.condition} {self.body} Else {self.elsebody})"


class EndStatement(Stmt):

    def __init__(self, ended):
        self.type = "end"
        self.ended = ended

    def __repr__(self):
        return f"End({self.ended})"


class Text(Expr):

    def __init__(self, text):
        self.type = "text"
        self.text = text

    def __repr__(self):
        return f"Text({self.text})"


class Input_Expr(Expr):

    def __init__(self):
        self.type = "input-expr"

    def __repr__(self):
        return f"Input_Expr"

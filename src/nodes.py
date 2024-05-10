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
                 condition,
                 body,
                 Conelse=False,
                 Else_Body=None,
                 elseifcon=False,
                 elseifbody=None,
                 conelseif=False):
        self.type = "if"
        self.condition = condition
        self.body = body
        self.conelse = Conelse
        self.elsebody = Else_Body
        self.elseifcon = elseifcon
        self.elseifbody = elseifbody
        self.conelseif = conelseif

    def __repr__(self):
        if self.elsebody is None:
            return f"If({self.condition} {self.body})"
        elif self.elseifbody is not None:
            if self.elsebody is None:
                return f"If({self.condition} {self.body} Elseif {self.elseifcon} {self.elseifbody})"
            else:
                return f"If({self.condition} {self.body} Elseif {self.elseifcon} {self.elseifbody} Else {self.elsebody})"
        else:
            return f"If({self.condition} {self.body} Else {self.elsebody})"


class EndStatement(Stmt):

    def __init__(self):
        self.type = "end"

    def __repr__(self):
        return f"End()"


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


class Repeat(Stmt):

    def __init__(self, body, condition):
        self.type = "repeat"
        self.body = body
        self.condition = condition

    def __repr__(self):
        return f"Repeat({self.body} Until {self.condition})"


class Pause(Stmt):

    def __init__(self, time):
        self.type = "pause"
        self.time = time

    def __repr__(self):
        return f"Pause({self.time})"



class Type(Stmt):

    def __init__(self, type):
        self.type = "type"
        self.t_type = type


    def __repr__(self):
        return f"Type({self.t_type})"


class List(Expr):
    def __init__(self, expr):
        self.type = "list"
        self.expr = expr

    def __repr__(self):
        return f"List({self.expr})"


class Function(Stmt):
    def __init__(self, name: Identifier, body):
        self.type = "function"
        self.name = name
        self.body = body

    def __repr__(self):
        return f"Function({self.name} {self.body})"


class While(Stmt):
    def __init__(self, condition, body):
        self.type = "while"
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"While({self.condition} {self.body})"

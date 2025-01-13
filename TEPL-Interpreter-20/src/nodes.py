# Base classes for statements and expressions
class Stmt:
    pass

class Expr:
    pass

# Class for binary operations
class Binary(Expr):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return 'Binary({}, {}, {})'.format(self.left, self.op, self.right)

# Class for numeric values
class Number(Expr):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'Number({})'.format(self.value)

# Class for identifiers
class Id(Expr):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Id({})'.format(self.name)

# Class for set statements
class Set(Stmt):
    def __init__(self, name: Id, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return 'Set({}, {})'.format(self.name, self.value)

# Class for output statements
class Output(Stmt):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'Output({})'.format(self.value)

# Class for random number generation
class Random(Expr):
    def __init__(self, _type, _from, _to):
        self.type = _type
        self.f = _from
        self.to = _to

    def __repr__(self):
        return 'Random({}, {}, {})'.format(self.type, self.f, self.to)

# Class for text values
class Text(Expr):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'Text({})'.format(self.value)

# Class for if statements
class If(Stmt):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return 'If({}, {})'.format(self.condition, self.body)

# Class for conditions
class Condition(Expr):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return 'Condition({}, {}, {})'.format(self.left, self.op, self.right)

# Class for input statements
class Input(Stmt):
    def __init__(self, question):
        self.question = question

    def __repr__(self):
        return 'Input({})'.format(self.question)
    
    
# Class for while statements
class While(Stmt):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body
        
    def __repr__(self):
        return 'While({}, {})'.format(self.cond, self.body)
    

# Class for repeat statements
class Repeat(Stmt):
    def __init__(self, times, body):
        self.times = times
        self.body = body
        
    def __repr__(self):
        return 'Repeat({}, {})'.format(self.times, self.body)

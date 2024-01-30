# importing ply(python, lex, and yacc)
from ply.lex import lex
from ply.yacc import yacc

# list of tokens, this is always required when using ply
tokens = (
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'LPAREN', 'RPAREN', 
    'NUMBER',
)

# regexes for the tokens
t_PLUS         = r'\+'
t_MINUS        = r'-'
t_MULTIPLY     = r'\*'
t_DIVIDE       = r'/'
t_LPAREN       = r'\('
t_RPAREN       = r'\)'
t_NUMBER       = r'\d+'


# a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# handling errors
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# precedence table
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'UMINUS'),            # unary minus operator
)

# transveral ast 
class Expr: 
    pass

class BinOp(Expr):
    def __init__(self,left,op,right):
        self.type = "binop"
        self.left = left
        self.right = right
        self.op = op

    def math(self):
        if self.op == "+":
            return self.left.math() + self.right.math()
        elif self.op == "-":
            return self.left.math() - self.right.math()
        elif self.op == "*":
            return self.left.math() * self.right.math()
        elif self.op == "/":
            return self.left.math() / self.right.math()

class Number(Expr):
    def __init__(self,value):
        self.type = "number"
        self.value = value

    def re(self):
        return int(self.value)

def p_expression_binop(p):
    '''statement  : NUMBER PLUS NUMBER
                  | NUMBER MINUS NUMBER
                  | NUMBER MULTIPLY NUMBER
                  | NUMBER DIVIDE NUMBER'''

    #Math = BinOp(p[1],p[2],p[3])
    #p[0] = Math.math()
    if p[2] == '+':
        p[0] = int(p[1]) + int(p[3])
    elif p[2] == '-':
        p[0] = int(p[1]) - int(p[3])
    elif p[2] == '*':
        p[0] = int(p[1]) * int(p[3])
    elif p[2] == '/':
        p[0] = int(p[1]) / int(p[3])

    print(p[0])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number-expression', p[1])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expr_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_error(p):
    if p:
         print("Syntax error at token", p.type)
         # just discard the token and tell the parser it's okay
         parser.errok()
    else:
         print("Syntax error at EOF")


# building the lexer and parser
lexer = lex()
parser = yacc()

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

class Number(Expr):
    def __init__(self,value):
        self.type = "number"
        self.value = value

def p_expression_binop(p):
    '''expression : expression PLUS expression
              | expression MINUS expression
              | expression TIMES expression
              | expression DIVIDE expression'''

    p[0] = BinOp(p[1], p[2], p[3])

def p_binary_operators(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression'''
    # p[0] = Node("binop", [p[1], p[3]], p[2])
    
    p[0] = ('binary-expression', p[2], p[1], p[3])

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


# running the code
if __name__ == "__main__":
    while True: 
        code = input(">> ")
        try: 
            parser.parse(code, lexer=lexer)
        except Exception as e:
            print(f'Error: {e}')
            break


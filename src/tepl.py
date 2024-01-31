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
t_ignore       = ' '

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
class Node:
    def __init__(self,type,children=None,leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.leaf = leaf

    def binop(self):
        if self.type == "binop": 
            pass
        else: 
            return "Error: Not a binary operation"
        left = self.children[0]
        right = self.children[1]
        op = self.leaf
        
        if op == "+":
            return int(left) + int(right)
        elif op == "-":
            return int(left) - int(right)
        elif op == "*":
            return int(left) * int(right)
        elif op == "/":
            if right == 0: 
                return "Error: Division by zero"
            else:
                return int(left) / int(right)
        else: 
            return f"Unknown operator, {op}"

def p_expression_binop(p):
    '''statement  : NUMBER PLUS NUMBER
                  | NUMBER MINUS NUMBER
                  | NUMBER MULTIPLY NUMBER
                  | NUMBER DIVIDE NUMBER'''
    
    equation = Node("binop", [p[1], p[3]], p[2])
    result = equation.binop()
    p[0] = result
    print(p[0])

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_uminus(p):
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

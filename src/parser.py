import ply.yacc as yacc
from lexer import *

# Define precedence and associativity
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'POWER'),
    ('left', 'LPAREN', 'RPAREN'),
)

vars = {}

# Define grammar rules
def p_statement_output(p):
    '''
    statement : OUTPUT expression
    '''
    print(p[2])

def p_statement_assignment(p):
    '''
    statement : SET IDENTIFIER TO expression
    '''
    vars[p[2]] = p[4]

def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression POWER expression
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            raise ZeroDivisionError("division by zero")
        p[0] = p[1] / p[3]
    elif p[2] == '^':
        p[0] = p[1] ** p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_identifier(p): 
    'expression : IDENTIFIER'
    if p[1] in vars:
        p[0] = vars[p[1]]
    else: 
        raise NameError(f"Name '{p[1]}' is not defined")

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

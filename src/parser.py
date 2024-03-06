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
    p[0] = ('OUTPUT', p[2])

def p_statement_assignment(p):
    '''
    statement : SET IDENTIFIER TO expression
    '''
    p[0] = ('SET', p[2], p[4])

def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression POWER expression
    '''
    p[0] = (p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = (p[2])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('NUMBER', p[1])

def p_expression_identifier(p): 
    'expression : IDENTIFIER'
    p[0] = ('IDENTIFIER', p[1])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

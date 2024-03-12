import ply.yacc as yacc
from lexer import *

# Define precedence and associativity
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'POWER'),
    ('left', 'LPAREN', 'RPAREN'),
)

# Define grammar rules
def p_statement_output(p):
    '''
    statement : OUTPUT expression
    '''
    p[0] = ('OUTPUT', p[2])

def p_statement_type(p):
    '''
    type_statement : TYPE DATATYPE
    '''
    p[0] = ('TYPE', p[2])

def p_statement_var_assignment(p):
    '''
    var_assignment : SET IDENTIFIER
    '''
    p[0] = ('SET', p[2])

def type_set(prs, ts, target, nt, tvt) -> bool:
    if ts == target:
        if tvt == 'typeset':
            prs[0] = (prs[1], 'TYPE', nt)
        else: 
            # p[0] = (p[1], p[3])
            prs[0] = (prs[1], prs[3])
        return True
    else: 
        return False

def type_switch(prs, tt):
    if tt == 'typeset':
        if type_set(prs, prs[2][1], 'NUM', int, 'typeset'):
            pass
        elif type_set(prs, prs[2][1], 'TXT', str, 'typeset'):
            pass
        elif type_set(prs, prs[2][1], 'DEC', float, 'typeset'):
            pass
        elif type_set(prs, prs[2][1], 'BOOL', bool, 'typeset'):
            pass
    else:
        if type_set(prs, prs[2][1], 'NUM', int, 'synmain'):
            pass
        elif type_set(prs, prs[2][1], 'TXT', str, 'synmain'):
            pass
        elif type_set(prs, prs[2][1], 'DEC', float, 'synmain'):
            pass
        elif type_set(prs, prs[2][1], 'BOOL', bool, 'synmain'):
            pass

def p_statement_assignment(p):
    '''
    statement : var_assignment TO expression
              | var_assignment type_statement
              | var_assignment TO expression type_statement
    '''
    if p[2][0] == 'TYPE':
        type_switch(p, 'typeset')
    else:
        if len(p) == 3:
            p[0] = (p[1], p[3])
        elif len(p) == 4:
            type_switch(p, 'synmain')

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

def p_expression_boolean(p):
    '''
    expression : YES
               | NO
    '''
    p[0] = ('BOOL', p[1])

def p_expression_comparison(p):
    '''
    expression : expression EQ expression
               | expression GT expression
               | expression LT expression
               | expression GE expression
               | expression LE expression
               | expression NE expression
    '''
    p[0] = (p[2], p[1], p[3])

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

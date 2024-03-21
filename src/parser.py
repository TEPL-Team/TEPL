import ply.yacc as yacc
from lexer import tokens

__error__ = False

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


def p_random_statement(p):
    '''
    random_statement : RANDOM DATATYPE FROM expression TO expression
    '''
    p[0] = ('RANDOM', p[2], p[4], p[6])


def p_type_statement(p):
    '''
    type_statement : TYPE DATATYPE
    '''
    p[0] = ('TYPE', p[2])


def p_statement_var_assignment(p):
    '''
    var_assignment : SET IDENTIFIER
    '''
    p[0] = ('SET', p[2])


def p_statement_assignment(p):
    '''
    statement : var_assignment TO expression
              | var_assignment 
    '''
    if len(p) == 2:
        p[0] = ('SET', p[1][1], None)
    elif len(p) == 4:
        p[0] = ('SET', p[1][1], p[3])


def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression POWER expression
    '''
    p[0] = ('MATH_EXPR', p[2], p[1], p[3])


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_expression_boolean(p):
    '''
    expression : YES
               | NO
    '''
    p[0] = ('BOOL', p[1])


def p_comp_expr(p):
    '''
    comp_expr  : expression EQ expression
               | expression GT expression
               | expression LT expression
               | expression GE expression
               | expression LE expression
               | expression NE expression
    '''
    p[0] = ('COMP_EXPR', p[2], p[1], p[3])


def p_expression_comp_expr(p):
    '''
    expression : comp_expr
    '''
    p[0] = p[1]


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('NUMBER', p[1])


def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ('IDENTIFIER', p[1])


def p_expression_random(p):
    'expression : random_statement'
    p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    global __error__
    if p:
        print(f"Syntax error at '{p.value}'!")
    else:
        print("Syntax error at EOF")
    __error__ = True


# Build the parser
parser = yacc.yacc()

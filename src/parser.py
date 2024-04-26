import ply.yacc as yacc
from nodes import *
from lexer import tokens

__error__ = False


# Define grammar rules
def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_end_statement(p):
    '''
    end_statement : END IF
    '''
    p[0] = EndStatement(p[2])


def p_statement_output(p):
    '''
    statement : OUTPUT expression
              | OUTPUT ask
    '''
    p[0] = Output(p[2])


def p_ask_statement(p):
    '''
    ask : TEXT EXPECTING INPUT AND DATATYPE
    '''
    p[0] = Input(p[1], p[5])


def p_random_statement(p):
    '''
    random_statement : RANDOM DATATYPE FROM expression TO expression
    '''
    p[0] = Random(p[2], p[4], p[6])


def p_statement_var_assignment(p):
    '''
    var_assignment : SET IDENTIFIER
    '''
    p[0] = Identifier(p[2])


def p_statement_assignment(p):
    '''
    statement : var_assignment TO expression
              | var_assignment 
              | var_assignment TO ask
    '''
    if len(p) == 2:
        p[0] = Assignment(p[1], None)
    elif len(p) == 4:
        p[0] = Assignment(p[1], p[3])


def p_if_then(p):
    '''
    if_then : IF expression THEN statements
    '''
    p[0] = If(p[2], p[4])


def p_statement_if(p):
    '''
    statement : if_then end_statement
              | if_then ELSE THEN statement end_statement
    '''
    if isinstance(p[2], EndStatement):
        if p[2].ended.upper() == 'IF':
            p[0] = If(p[1].condition, p[1].body)
        else:
            return print(
                f'SyntaxError: expected "IF", but got {p[5].ended.upper()} on line {p.lineno}!'
            )
    elif p[2].upper() == 'ELSE':
        if (isinstance(p[5], EndStatement)) and p[5].ended.upper() == 'IF':
            p[0] = If(p[1].condition, p[1].body, True, p[4])
    else:
        return print('SyntaxError: expected "end if", but got "' + p[5] +
                     f'" on line {p.lineno}!')


#def p_expr_if(p):
#   '''
#  expression : expression IF comp_expr
# '''
#p[0] = ('IF', p[1], 'EXPR', p[3])


def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression POWER expression
    '''
    p[0] = BinOp(p[1], p[2], p[3])


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_expression_boolean(p):
    '''
    expression : YES
               | NO
    '''
    p[0] = Boolean(p[1])


def p_comp_expr(p):
    '''
    comp_expr  : expression EQ expression
               | expression GT expression
               | expression LT expression
               | expression GE expression
               | expression LE expression
               | expression NE expression
    '''
    p[0] = Comparism(p[1], p[2], p[3])


def p_expression_comp_expr(p):
    '''
    expression : comp_expr
    '''
    p[0] = p[1]


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = Number(p[1])


def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = Identifier(p[1])


def p_expression_random(p):
    'expression : random_statement'
    p[0] = p[1]


def p_expression_text(p):
    'expression : TEXT'
    p[0] = Text(p[1])


def p_expression_input(p):
    'expression : INPUT'
    p[0] = Input_Expr()


def p_error(p):
    global __error__
    if p:
        print(f"Syntax error at '{p.value}', on line '{p.lineno}'!")
    else:
        print("Syntax error at EOF!")
    __error__ = True


# Build the parser
parser = yacc.yacc()

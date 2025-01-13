from ply import yacc
from src.nodes import Set, Output, Binary, Number, Id, Random, Text, If, Condition, Input, While, Repeat
from src.tokens import tokens

# Define the grammar rules for the language

def p_body(p):
    '''
    body : stmt
         | body stmt
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_stmt(p):
    '''
    stmt : set_stmt
         | output_stmt
         | if_then_stmt
         | input_stmt
         | while_stmt
         | repeat_stmt
         | stmt_rep
    '''
    p[0] = p[1]

def p_var_stmt(p):
    '''
    var_stmt : SET ID
    '''
    p[0] = Id(p[2])

def p_set_stmt(p):
    '''set_stmt : var_stmt TO expr'''
    p[0] = Set(p[1], p[3])

def p_output_stmt(p):
    '''output_stmt : OUTPUT expr'''
    p[0] = Output(p[2])

def p_if_then_stmt(p):
    '''if_then_stmt : IF expr THEN body END'''
    p[0] = If(p[2], p[4])

def p_input_stmt(p):
    '''
    input_stmt : ASK TXT
    '''
    p[0] = Input(p[2])
    
def p_while_stmt(p):
    '''
    while_stmt : WHILE condition DO body END
    '''
    p[0] = While(p[2], p[4])
    
def p_repeat_stmt(p):
    '''
    repeat_stmt : REPEAT expr TIMES AND DO body END
    '''
    p[0] = Repeat(p[2], p[6])
    
def p_stmt_rep(p):
    '''
    stmt_rep : stmt REPEAT expr TIMES
    '''
    p[0] = Repeat(p[3], p[1])

def p_expr(p):
    '''
    expr : binop
         | condition
    '''
    p[0] = p[1]

def p_binop(p):
    '''
    binop : expr PLUS expr
         | expr MINUS expr
         | expr TIMES expr
         | expr DIVIDE expr
    '''
    p[0] = Binary(p[1], p[2], p[3])

def p_condition(p):
    '''
    condition : expr GT expr
              | expr LT expr
              | expr ET expr
              | expr GTE expr
              | expr LTE expr
              | expr NE expr
    '''
    p[0] = Condition(p[1], p[2], p[3])

def p_number(p):
    '''expr : NUM'''
    p[0] = Number(p[1])

def p_id(p):
    '''expr : ID'''
    p[0] = Id(p[1])

def p_group(p):
    '''expr : LPAREN expr RPAREN'''
    p[0] = p[2]

def p_random(p):
    '''
    expr : RANDOM NUMBER FROM expr TO expr
    '''
    p[0] = Random(p[2], p[4], p[6])

def p_text(p):
    '''expr : TXT'''
    p[0] = Text(p[1])

def p_error(p):
    print("Syntax error in input on line %d at token '%s'" %
          ((p.lineno - 27), p.value))

# Build the parser
parser = yacc.yacc()

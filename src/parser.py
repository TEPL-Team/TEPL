from ply import yacc
from src.nodes import Expr, Set, Output, Binary, Number, Id, Random, Text, If, Condition, Input, While, Repeat, Convert, Pause
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
         | pause_stmt
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
    input_stmt : ASK expr
    '''
    p[0] = Input(p[2])
    
def p_while_stmt(p):
    '''
    while_stmt : WHILE condition DO body END
    '''
    p[0] = While(p[2], p[4])

def p_repeat(p):
    '''
    repeat : REPEAT expr TIMES USING expr
    '''
    p[0] = (p[2], p[5])

def p_repeat_stmt(p):
    '''
    repeat_stmt : repeat body END
    '''
    p[0] = Repeat(p[1][0], p[1][1], p[2])


def p_pause_stmt(p):
    '''
    pause_stmt : PAUSE expr
    '''
    p[0] = Pause(p[2])

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
         | expr MULTIPLY expr
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
    '''expr : DIGIT'''
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
    '''expr : TEXT'''
    p[0] = Text(p[1])

def p_convert(p):
    '''
    expr : CONVERT expr TO datatype
    '''
    p[0] = Convert(p[2], p[4])

def p_datatype(p):
    '''
    datatype : NUM
             | TXT
    '''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}' on line {p.lineno}, position {p.lexpos}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Semantic analysis function
def semantic_analysis(tree):
    try:
        for node in tree:
            if isinstance(node, Set):
                if not isinstance(node.name, Id):
                    raise TypeError(f"Expected an identifier for variable name, got {type(node.name).__name__}")
                if not isinstance(node.value, Expr):
                    raise TypeError(f"Expected an expression for variable value, got {type(node.value).__name__}")
            elif isinstance(node, Output):
                if not isinstance(node.value, Expr):
                    raise TypeError(f"Expected an expression for output value, got {type(node.value).__name__}")
            elif isinstance(node, If):
                if not isinstance(node.condition, Expr):
                    raise TypeError(f"Expected an expression for condition, got {type(node.condition).__name__}")
                if not isinstance(node.body, list):
                    raise TypeError(f"Expected a list of statements for body, got {type(node.body).__name__}")
            elif isinstance(node, While):
                if not isinstance(node.cond, Expr):
                    raise TypeError(f"Expected an expression for condition, got {type(node.cond).__name__}")
                if not isinstance(node.body, list):
                    raise TypeError(f"Expected a list of statements for body, got {type(node.body).__name__}")
            elif isinstance(node, Repeat):
                if not isinstance(node.times, Expr):
                    raise TypeError(f"Expected an expression for times, got {type(node.times).__name__}")
                if not isinstance(node.id, Id):
                    raise TypeError(f"Expected an identifier for loop variable, got {type(node.id).__name__}")
                if not isinstance(node.body, list):
                    raise TypeError(f"Expected a list of statements for body, got {type(node.body).__name__}")
            # Add more checks as needed for other node types
    except Exception as e:
        print(f"Semantic error: {e}")
        return False
    return True

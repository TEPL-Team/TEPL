### Stages to completing TEPL:
# 1. Build a basic arithmetic calculator.
# 2. Add variable support.
# 3. Add basic logic operators.
# 4. Implement booleans.
# 5. Add more math operators and math functions, including: sin, cos, and tan.
# 6. Add if statements.
# 7. Add elseif, and else.
# 8. Add AND, OR, and NOT.
# 9. Add TEXT data type.
# 10. Add OUPUT statement.
# 11. Add .tepl file support.
# 12. Add comments.
# 13. Add text manipulation functions.
# 14. Add INPUT statement.
# 15. Add list support.
# 16. Add for loops.
# 17. Add while loops.
# 18. Add special for loop functions.
# 19.
### END OF STAGES


# Grammar rules can be found in the README.md file.

# import ply(python, lex, and yacc) library
import ply.lex as lex
import ply.yacc as yacc

# Define tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'IDENTIFIER',
    'SET'
)

# Define token regex patterns
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_SET = r'SET'

# Ignore whitespace
t_ignore = ' \t'

# Define identifier token
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'
    return t

# Define number token
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define grammar rules
def p_statement_set(p):
    'statement : SET IDENTIFIER expression'
    p[0] = ('SET', p[2], p[3])
    interpret(p[0])

def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
    '''
    p[0] = (p[2], p[1], p[3])
    interpret(p[0])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('NUMBER', p[1])
    interpret(p[0])

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ('IDENTIFIER', p[1])
    interpret(p[0])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]
    interpret(p[0])

def p_error(p):
    print("Syntax error")

# Build the parser
parser = yacc.yacc()

# Interpreter function
def interpret(ast):
    if isinstance(ast, tuple):
        if ast[0] == 'SET':
            variables[ast[1]] = interpret(ast[2])
        elif ast[0] == 'NUMBER':
            return ast[1]
        elif ast[0] == 'IDENTIFIER':
            return variables.get(ast[1], 0)
        else:
            op = ast[0]
            left = interpret(ast[1])
            right = interpret(ast[2])
            if op == 'PLUS':
                return left + right
            elif op == 'MINUS':
                return left - right
            elif op == 'TIMES':
                return left * right
            elif op == 'DIVIDE':
                return left / right
    else:
        return ast

variables = {}
print("TEST=")

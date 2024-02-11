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

import ply.lex as lex
import ply.yacc as yacc

# Define tokens and keywors
keywords = (
    'OUTPUT', 
    'TO',
    'SET'
)

tokens = (
    'NUMBER', 'TEXT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'POWER',
    'IDENTIFIER',
) + keywords

# Define regular expressions for tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_POWER = r'\^'

# Define a rule for numbers
def t_NUMBER(t):
    r'\d+\.?\d*'
    t.value = float(t.value)
    return t

# Define a rule for keywords and identifiers
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Check if it's a keyword
    if t.value in keywords:
        t.type = 'KEYWORD'

    # Check if it's an identifier
    else:
        t.type = 'IDENTIFIER'
    return t

# Ignored characters (whitespace)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define precedence and associativity
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'POWER'),
    ('left', 'LPAREN', 'RPAREN'),
)

# Define grammar rules
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

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

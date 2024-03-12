# import lex tool
import ply.lex as lex

# Define tokens and keywors
keywords: tuple = (
    'OUTPUT', 
    'TO',
    'SET',
    'TYPE'
)

tokens: tuple = (
    'NUMBER', 'TEXT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'POWER',
    'IDENTIFIER',
    'EQ',
    'GT', 
    'LT',
    'GE',
    'LE',
    'NE',
    'YES',
    'NO',
    'DATATYPE'
) + keywords

# Define regular expressions for tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_POWER = r'\^'
t_EQ = r'=='
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_NE = r'!='
t_DATATYPE = r'(NUM|DEC|TXT|BOOL)'


types = (
    'NUM',
    'DEC',
    'TXT',
    'BOOL'
)

# Define a rule for numbers
def t_NUMBER(t):
    r'\d+\.?\d*'
    t.value = float(t.value)
    return t

def t_YES(t):
    r'YES'
    t.value = True
    return t

def t_NO(t):
    r'NO'
    t.value = False
    return t

# Define a rule for keywords and identifiers
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Check if it's a keyword
    if t.value in keywords:
        t.type = t.value
    # Check if it is a datatype
    elif t.value in types:
        t.type = 'DATATYPE'
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

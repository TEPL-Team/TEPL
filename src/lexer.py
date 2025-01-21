import ply.lex as lex
from src.tokens import tokens, keywords

# Define token rules for operators and delimiters
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GT = r'>'
t_LT = r'<'
t_ET = r'=='
t_GTE = r'>='
t_LTE = r'<='
t_NE = r'!='

# Ignore spaces and tabs
t_ignore = ' \t'

# Define a rule for comments (discard them)
def t_COMMENT(t):
    r'Note:.*'
    pass  # Discard comments by not returning them

# Define a rule for numbers
def t_DIGIT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule for text (strings)
def t_TEXT(t):
    r'(\'([^\\\'\n]|(\\.))*?\')|(\"([^\\\"\n]|(\\.))*?\")'
    # t.value = t.value[1:-1]
    return t

# Define a rule for identifiers and keywords
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.upper() in keywords:
        t.type = t.value.upper()
    else:
        t.type = 'ID'
    return t

# Define a rule for newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define a rule for errors
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

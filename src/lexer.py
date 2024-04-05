import ply.lex as lex

# Define tokens and keywords
keywords = ('OUTPUT', 'TO', 'SET', 'RANDOM', 'FROM', 'IF', 'THEN', 'INPUT',
            'EXPECTING', 'AND')

tokens = ('NUMBER', 'TEXT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN',
          'RPAREN', 'POWER', 'IDENTIFIER', 'EQ', 'GT', 'LT', 'GE', 'LE', 'NE',
          'DATATYPE', 'YES', 'NO') + keywords

# Regular expression rules for tokens
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
t_YES = r'YES'
t_NO = r'NO'
t_DATATYPE = r'(NUM|DEC|TXT)'


# Define a rule for numbers (integers)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule for texts (strings)
def t_TEXT(t):
    r'(\'([^\\\n]|(\\.))*?\')|(\"([^\\\n]|(\\.))*?\")'
    t.value = str(t.value)
    return t


# Define a rule for keywords and identifiers
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = t.value.upper() if t.value.upper() in keywords else \
             'DATATYPE' if t.value.upper() in ['DEC', 'NUM', 'TXT'] else \
             t.value.upper() if t.value.upper() in ['YES', 'NO'] else \
             'IDENTIFIER'
    return t


# Ignored characters (whitespace)
t_ignore = ' \t'


# A rule for new lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

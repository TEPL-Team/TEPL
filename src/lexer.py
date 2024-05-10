import ply.lex as lex

# Dictionary of keywords
keywords = {
    'OUTPUT': 'OUTPUT',
    'TO': 'TO',
    'SET': 'SET',
    'RANDOM': 'RANDOM',
    'FROM': 'FROM',
    'IF': 'IF',
    'THEN': 'THEN',
    'INPUT': 'INPUT',
    'EXPECTING': 'EXPECTING',
    'AND': 'AND',
    'END': 'END',
    'YES': 'YES',
    'NO': 'NO',
    'NUM': 'DATATYPE',
    'DEC': 'DATATYPE',
    'TXT': 'DATATYPE',
    'ELSE': 'ELSE',
    'ELSEIF': 'ELSEIF',
    'IN': 'IN',
    'NOT': 'NOT',
    'OR': 'OR',
    'REPEAT': 'REPEAT',
    'UNTIL': 'UNTIL',
    'PAUSE': 'PAUSE',
    'TYPE': 'TYPE',
    'LIST': 'DATATYPE',
    'FUNCTION': 'FUNCTION',
    'MEANS': 'MEANS', 
    'RETURN': 'RETURN',
    'WHILE': 'WHILE',
    'DO': 'DO'
}

# Regular expression rules for tokens
tokens = [
    'NUMBER', 'TEXT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
    'POWER', 'IDENTIFIER', 'EQ', 'GT', 'LT', 'GE', 'LE', 'NE', 'DATATYPE',
    'YES', 'NO'
] + list(keywords.values())  # Include keywords in tokens

# Arithmetic Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_POWER = r'\^'

# Comparison Operators
t_EQ = r'=='
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_NE = r'!='

# Boolean Values
t_YES = r'YES'
t_NO = r'NO'

# Data Types
t_DATATYPE = r'(NUM|DEC|TXT)'


# Rule for numbers (integers)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Rule for texts (strings)
def t_TEXT(t):
    r'(\'([^\\\'\n]|(\\.))*?\')|(\"([^\\\"\n]|(\\.))*?\")'
    t.value = str(t.value)
    return t


# Rule for identifiers
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value.upper(), 'IDENTIFIER')
    return t


# Ignored characters (whitespace)
t_ignore = ' \t'


# Rule for new lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'!")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

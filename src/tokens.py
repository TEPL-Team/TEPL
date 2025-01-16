# Define the keywords used in the language
keywords = (
    'OUTPUT',
    'SET',
    'TO',
    'RANDOM',
    'FROM',
    'NUMBER',
    'IF',
    'THEN',
    'END',
    'ASK',
    'DO',
    'WHILE',
    'REPEAT',
    'TIMES',
    'USING',
    'CONVERT',
    'NUM',
    'TXT',
    'PAUSE'
)

# Define the tokens used in the language, including keywords
tokens = (
    'DIGIT',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    'TEXT',
    'GT',
    'LT',
    'ET',
    'LTE',
    'GTE',
    'NE',
    'COMMENT'
) + keywords

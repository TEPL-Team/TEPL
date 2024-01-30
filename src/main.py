# importing ply(python, lex, and yacc)
from ply import lex, yacc

# list of tokens, this is always required when using ply
tokens = (
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'LPAREN', 'RPAREN', 
    'NUMBER', 'DECIMAL', 'TEXT', 'BOOLEAN', 'ID', 
    'OUTPUT', 'SET', 
    'TO'
)

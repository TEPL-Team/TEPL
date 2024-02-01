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

# importing ply(python, lex, and yacc)
from ply.lex import lex
from ply.yacc import yacc

# a list of reserved keywords
keywords = {
    'var': 'SET',
    'to': 'TO',
}

# list of tokens, this is always required when using ply
tokens = (
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'LPAREN', 'RPAREN', 
    'NUMBER', 'ID'
) + tuple(keywords.values())

# regexes for the tokens
t_PLUS         = r'\+'
t_MINUS        = r'-'
t_MULTIPLY     = r'\*'
t_DIVIDE       = r'/'
t_LPAREN       = r'\('
t_RPAREN       = r'\)'
t_ignore       = ' \t'

# a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# regex rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID') # < check for keywords
    return t

# handling errors
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# precedence table
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    #('right', 'UMINUS'), # unary minus operator
)

vars = {}

# transveral ast 
class Node:
    def __init__(self,type,children=None,leaf=None):
        self.type = type
        
        if children:
            self.children = children
        else:
            self.children = []
        self.leaf = leaf

        if self.type == "binop": 
            self.binop()
        elif self.type == "var-assignment":
            self.assignvar()

    def binop(self):
        left = self.children[0]
        right = self.children[1]
        op = self.leaf
        
        if op == "+":
            return int(left) + int(right)
        elif op == "-":
            return int(left) - int(right)
        elif op == "*":
            return int(left) * int(right)
        elif op == "/":
            if right == 0: 
                return "Error: Division by zero"
            else:
                return int(left) / int(right)
        else: 
            return f"Unknown operator, {op}"

    def assignvar(self):
        global vars
        varname = self.leaf
        value = self.children[0]

        if self.children[1] == 'TO':
            vars[varname] = value
        else: 
            return f"Error: Invalid assignment, was expecting, 'TO', but got {self.children[1]}"
        
def p_statement_assignvar(p):
    '''
    statement : SET ID TO expression
    '''
    newvar = Node("var-assignment", [p[4], p[3]], p[2])

def p_expression_binop(p):
    '''expression : NUMBER PLUS NUMBER
                  | NUMBER MINUS NUMBER
                  | NUMBER MULTIPLY NUMBER
                  | NUMBER DIVIDE NUMBER'''
    
    equation = Node("binop", [p[1], p[3]], p[2])
    result = equation.binop()
    p[0] = result

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_id(p):
    '''
    expression : ID
    '''
    if p[1] in vars:
        p[0] = vars[p[1]] 
    else:
        return f"Error: Variable {p[1]} is not defined"

#def p_expression_uminus(p):
 #   'expression : MINUS NUMBER %prec UMINUS'
#    p[0] = -p[2]

def p_error(p):
    if p:
         print("Syntax error at token", p.type)
         # just discard the token and tell the parser it's okay
         parser.errok()
    else:
         print("Syntax error at EOF")


# building the lexer and parser
lexer = lex()
parser = yacc()

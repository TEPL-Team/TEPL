### Stages to completing TEPL:
# Status: Completed.
# 1. Build a basic arithmetic calculator.
# Status: Completed.
# 2. Add variable support.
# Status: In-Progress
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
# 19. List manipulation functions
# 20.
### END OF STAGES

# Grammar rules can be found at
# https://tepl.vercel.app/docs.html.
# Lexer can be found in the lexer.py file.
# Parser can be found in the parser.py file.

# importing parser
from parser import *

vars = {}


def interpret(ast):
    global vars
    if isinstance(ast, tuple):
        if ast[0] == 'SET':
            vars[ast[1]] = interpret(ast[2])
        elif ast[0] == 'OUTPUT':
            value = interpret(ast[1])
            print(value)
            return value
        elif ast[0] == 'NUMBER':
            return ast[1]
        elif ast[0] == 'IDENTIFIER':
            if ast[1] in vars:
                return vars[ast[1]]
            else:
                raise NameError(f"Name '{ast[1]}' is not defined")
        elif ast[0] == 'BOOL':
            if ast[1] == 'YES':
                return True
            elif ast[1] == 'NO':
                return False
            else: 
                raise ValueError('UnknownError: Invalid boolean value')
        else:
            op = ast[0]
            left = interpret(ast[1])
            right = interpret(ast[2])
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                else:
                    return left / right
            elif op == '^':
                return left**right
            elif op == '==':
                return left == right
            elif op == '>':
                return left > right
            elif op == '<':
                return left < right
            elif op == '>=':
                return left >= right
            elif op == '<=':
                return left <= right
            elif op == '!=':
                return left != right
            else:
                raise ValueError(f"Invalid operator: {op}")
    else:
        return ast



'''
source_code = [
    ('SET', 'x', ('NUMBER', 10)),
    ('SET', 'y', ('NUMBER', 20)),
    ('SET', 'is_greater', ('GT', ('IDENTIFIER', 'x'), ('IDENTIFIER', 'y'))),
    ('SET', 'is_equal', ('EQ', ('IDENTIFIER', 'x'), ('IDENTIFIER', 'y'))),
    ('OUTPUT', ('IDENTIFIER', 'is_greater')),
    ('OUTPUT', ('IDENTIFIER', 'is_equal'))
]

for line in source_code:
    interpret(line)
'''

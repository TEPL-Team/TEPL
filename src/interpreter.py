### Stages to completing TEPL:
# Status: Completed.
# 1. Build a basic arithmetic calculator.
# Status: Completed.
# 2. Add variable support.
# Status: Completed.
# 3. Add basic logic operators.
# Status: Completed.
# 4. Implement booleans.
# Status: To-Begin.
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
# 19. Add list manipulation functions.
# 20. Add TYPE keyword.
### END OF STAGES

# Grammar rules can be found at
# https://tepl.vercel.app/docs.html.
# Lexer can be found in the lexer.py file.
# Parser can be found in the parser.py file.

# importing parser and Any type
from typing import Any
from parser import *

vars = {}

def interpret(ast: tuple | list) -> Any: 
    global vars
    if ast[0] == 'OUTPUT':
        value = interpret(ast[1])
        print(value)
    elif ast[0] == 'SET':
        if ast[2] == 'NONE':
            vars[ast[1]] = None
        else:
            value = interpret(ast[2])
            name = ast[1]
            vars[name] = value
    elif ast[0] == 'IDENTIFIER':
        if ast[1] in vars:
            return vars[ast[1]]
        else: 
            return print('NameError: name \'' + ast[1] + '\' is not defined')
    elif ast[0] == 'MATH_EXPR':
        op = ast[1]
        left = interpret(ast[2])
        right = interpret(ast[3])
        match op:
            case '+':
                return left + right
            case '-':
                return left - right
            case '*':
                return left * right
            case '/':
                return left / right
            case '^':
                return left ** right
            case _:
                return print(f'SyntaxError: invalid operator,  {op}!')
    elif ast[0] == 'BOOL': 
        if ast[1] == 'YES':
            return True
        elif ast[1] == 'NO':
            return False
        else: 
            return print(f'UnknownError: {ast[1]} is not a boolean?')
    elif ast[0] == 'NUMBER':
        return ast[1]
    elif ast[0] == 'COMP_EXPR':
        cp = ast[1]
        left = interpret(ast[2])
        right = interpret(ast[3])
        match cp:
            case '==':
                return left == right
            case '>':
                return left > right
            case '<' :
                return left < right
            case '>=':
                return left >= right
            case '<=':
                return left <= right
            case '!=':
                return left != right
            case _:
                return print(f'SyntaxError: invalid operator, {cp}!')

    else:
        return print(f'SyntaxError: {ast[0]} is not a valid token!')


'''
def interpret(ast):
    global vars
    if isinstance(ast, tuple):
        if ast[0] == 'SET':
            if len(ast) == 4:  # Variable declaration with type
                if ast[1] == 'TYPE':
                    vars[ast[0]]: ast[2] = ast[2]
                else:
                    vars[ast[1]]: ast[4][1] = interpret(ast[2])
                    # Regular variable assignment ^
            else:
                vars[ast[0][1]] = interpret(ast[1])
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
                raise ValueError('UnknownError: Invalid boolean value?')
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


'''
source_code = [
    ('SET', 'x', 5, ('TYPE', 'NUM')),
    ('OUTPUT', ('IDENTIFIER', 'x'))
]

for line in source_code:
    interpret(line)
'''

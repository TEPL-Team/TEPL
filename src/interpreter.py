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
# Status: Completed. 
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

# Docs can be found at
# https://tepl.vercel.app/docs.html.
# Lexer can be found in the lexer.py file.
# Parser can be found in the parser.py file.


# importing parser and Any type
import random
from parser import *
from typing import Any


vars = {}


def interpret(ast: tuple | list) -> Any:
    global vars, __error__
    if ast[0] == 'OUTPUT':
        value = interpret(ast[1])
        print(value)
    elif ast[0] == 'SET':
        if ast[2] is None:
            vars[ast[1]] = None
        else:
            name = ast[1]
            value = interpret(ast[2])
            vars[name] = value

    elif ast[0] == 'IDENTIFIER':
        if ast[1] in vars:
            return vars[ast[1]]
        else:
            print(f'NameError: name \'{ast[1]}\' is not defined!')
            __error__ = True
            return print(f'Current variables and their values: '+ str(vars))
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
                __error__ = True
                return print(f'SyntaxError: invalid operator,  {op}!')
    elif ast[0] == 'BOOL':
        if ast[1] == 'YES':
            return 'YES'
        elif ast[1] == 'NO':
            return 'NO'
        else:
            __error__ = True
            return print(f'UnknownError: {ast[1]} is not a boolean?')
    elif ast[0] == 'NUMBER':
        return ast[1]
    elif ast[0] == 'COMP_EXPR':
        cp = ast[1]
        left = interpret(ast[2])
        right = interpret(ast[3])
        match cp:
            case '==':
                return 'YES' if left == right else 'NO'
            case '>':
                return 'YES' if left > right else 'NO'
            case '<':
                return 'YES' if left < right else 'NO'
            case '>=':
                return 'YES' if left >= right else 'NO'
            case '<=':
                return 'YES' if left <= right else 'NO'
            case '!=':
                return 'YES' if left != right else 'NO'
            case _:
                __error__ = True
                return print(f'SyntaxError: invalid operator, {cp}!')
    elif ast[0] == 'RANDOM':
        _1 = interpret(ast[2])  # Starting value
        _2 = interpret(ast[3])  # Ending value
        if ast[1].upper() == 'NUM':  # Check for NUM or DEC
            return random.randint(_1, _2)
        else:
            __error__ = True
            return print(f'SyntaxError: invalid data type, {ast[1]} only \'NUM\' is allowed!')
    else:
        __error__ = True
        return print(f'SyntaxError: {ast[1]} is not a valid token!')


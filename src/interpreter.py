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
# Status: Completed.
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
# Status: Completed. 
# 21. Add FUNCTIONs. 
### END OF STAGES

# Docs can be found at
# https://tepl.vercel.app/docs.html.
# Lexer can be found in the lexer.py file.
# Parser can be found in the parser.py file.

import random
from parser import *
from parser import __error__
from typing import Any

vars = {}
__input__ = None


def interpret(ast: tuple | list) -> Any:
    global vars, __input__, __error__
    print(ast)
    if __error__:
        return

    if type(ast) is not (tuple or list):
        return ast

    if ast[0] == 'OUTPUT':
        value = interpret(ast[1])
        return value

    elif ast[0] == 'SET':
        name = ast[1]
        if len(ast) == 3:
            value = interpret(ast[2])
            vars[name] = value
        else:
            vars[name] = None

    elif ast[0] == 'IF':
        cond = interpret(ast[1])
        statement = interpret(ast[2])
        if cond == 'YES' and statement is not None:
            print(statement)

    elif ast[0] == 'IDENTIFIER':
        if ast[1] in vars:
            return vars[ast[1]]
        else:
            print(f'NameError: name \'{ast[1]}\' is not defined!')
            __error__ = True
            return __error__

    elif ast[0] == 'MATH_EXPR':
        op = ast[1]
        left = interpret(ast[2])
        right = interpret(ast[3])
        if isinstance(left, bool) or isinstance(right, bool):
            print(
                "TypeError: unsupported operand type(s) for +: 'bool' and 'NoneType'"
            )
            __error__ = True
            return __error__
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right
        elif op == '^':
            return left**right
        else:
            print(f'SyntaxError: invalid operator, {op}!')
            __error__ = True
            return __error__

    elif ast[0] == 'BOOL':
        if ast[1] == 'YES' or ast[1] == 'NO':
            return ast[1]
        else:
            print(f'UnknownError: {ast[1]} is not a boolean, only \'YES\' and \'NO\'?')
            __error__ = True
            return __error__

    elif ast[0] == 'NUMBER':
        return ast[1]

    elif ast[0] == 'TEXT':
        return ast[1][1:-1]

    elif ast[0] == 'INPUT':
        return __input__

    elif ast[0] == 'COMP_EXPR':
        cp = ast[1]
        left = interpret(ast[2])
        right = interpret(ast[3])
        if cp == '==':
            return 'YES' if left == right else 'NO'
        elif cp == '>':
            return 'YES' if left > right else 'NO'
        elif cp == '<':
            return 'YES' if left < right else 'NO'
        elif cp == '>=':
            return 'YES' if left >= right else 'NO'
        elif cp == '<=':
            return 'YES' if left <= right else 'NO'
        elif cp == '!=':
            return 'YES' if left != right else 'NO'
        else:
            print(f'SyntaxError: invalid operator, {cp}!')
            __error__ = True
            return __error__

    elif ast[0] == 'RANDOM':
        _1 = interpret(ast[2])  # Starting value
        _2 = interpret(ast[3])  # Ending value
        if ast[1].upper() == 'NUM':
            return random.randint(_1, _2)
        else:
            print(
                f'SyntaxError: invalid data type, {ast[1]} only \'NUM\' is allowed!'
            )
            __error__ = True
            return __error__

    elif ast[0] == 'ASK':
        question = ast[1]
        datatype = ast[2]
        if datatype.upper() == 'NUM':
            __input__ = int(input(question))
            return __input__
        elif datatype.upper() == 'TXT':
            __input__ = input(question)
            return __input__
        else:
            print(
                f'SyntaxError: invalid data type, {datatype} only \'NUM\' or \'TXT\' is allowed!'
            )
            __error__ = True
            return __error__

    else:
        print(f'SyntaxError: {ast[1]} is not a valid token!')
        __error__ = True
        return __error__


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
# 19. List manipulation functions
# 20. 
### END OF STAGES


# Grammar rules can be found in the README.md file.
# Lexer can be found in the lexer.py file.
# Parser can be found in the parser.py file.

# importing parser
from parser import *

#def run_code(p): 
 #   print(interpret(p[0]))

def interpret(ast):
    if isinstance(ast, tuple):
        if ast[0] == 'SET':
            vars[ast[1]] = interpret(ast[2])
        elif ast[0] == 'OUPUT':
            print(interpret(ast[1]))
        elif ast[0] == 'NUMBER':
            return ast[1]
        elif ast[0] == 'IDENTIFIER':
            if ast[1] in vars:
                return vars.get(ast[1])
            else:
                return NameError(f"Name '{ast[1]}' is not defined")
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
                return left ** right
    else:
        return ast

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

from parser import *


class Node: 
    def __init__(self, ast):
        self.ast = ast
        self.type = ast[0]
        self.checktype()

    def checktype(self):
        if self.type[0] == 'statement': 
            if self.type[1] == 'OUTPUT': 
                self.output()
            elif self.type[1] == 'SET':
                self.set()
        elif self.type[0] == 'expression':
            value = self.eval()
            return value

    def output(self):
        value = Node(['expression', self.ast[1]])
        print(value)

    def set(self):
        varname = self.ast[1]
        value = Node(['expression', self.ast[2]])
        vars[varname] = value

    def eval(self):
        toeval = self.ast[1]


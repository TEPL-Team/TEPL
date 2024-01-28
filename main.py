### IMPORTS
### END OF IMPORTS

col = 0
line = 1

def Parser(tokens):
    LENGTH = len(tokens)
    pos = 0
    vars = []
    output = None
    global col, line
    
    while pos < LENGTH:
        TOKEN = tokens[pos]
        if TOKEN['type'] == 'KEYWORD' and TOKEN['value'] == 'OUTPUT':
            if not(tokens[pos + 1]):
                return f'Unexpected end of line, expected valid value. At line ${line} and column ${col}!'

            if tokens[pos + 1]['type'] == 'STRING':
                output = tokens[pos + 1]['value']

def Lexer(text):
    LENGTH = len(text)
    global col, line
    pos = 0
    tokens = []
    DIGITS = '0123456789'
    while pos < LENGTH:
        char = text[pos]
        if char == ' ':
            col += 1
            pos += 1
            continue
        elif char == '\n':
            line += 1
            col = 0
            pos += 1
            continue
        elif char == '+':
            tokens.append({
                'type': 'PLUS',
                'value': '+',
                'line': line,
                'col': col
            })
            col += 1
            pos += 1
            continue
        elif char == '-':
            tokens.append({
                'type': 'MINUS',
                'value': '-',
                'line': line,
                'col': col
            })
            col += 1
            pos += 1
            continue
        elif char == '*':
            tokens.append({
                'type': 'MULTIPLY',
                'value': '*',
                'line': line,
                'col': col
            })
            col += 1
            pos += 1
            continue
        elif char == '/':
            tokens.append({
                'type': 'DIVIDE',
                'value': '/',
                'line': line,
                'col': col
            })
            col += 1
            pos += 1
            continue
        elif char == '(':
            tokens.append({
                'type': 'LPAREN',
                'value': '(',
                'line': line,
                'col': col
            })
            col += 1
            pos += 1
            continue
        elif char == '(':
            tokens.append({
                'type': 'RPAREN',
                'value': ')',
                'line': line,
                'col': col
            })
            col += 1
            pos += 1
            pass
        elif char == '"' or char == "'":
            res = ""
            pos += 1
            col += 1
            while pos < LENGTH and char != '"' and char != "'":
                res += char 
                pos += 1
                col += 1
            if (text[pos-1] != '"' and text[pos] != '"') or (text[pos-1] != "'" and text[pos] != "'"):
                return f'Unterminated text at line {line} and column {col}!'
            tokens.append({
                'type': 'STRING',
                'value': res,
                'line': line,
                'col': col
            })
            pos += 1
            col += 1
            continue
        elif char in DIGITS: # append: is True
            res = ""
            dots = 0
            while pos < LENGTH and (char in DIGITS or char == '.'):
                if char == '.':
                    if dots == 1:
                        return f'Invalid number at line {line} and column {col}!'
                    dots += 1
                    res += '.'
                    pos += 1
                    col += 1
                else: 
                    res += char
                    pos += 1
                    col += 1

            if dots != 1:
                tokens.append({
                    'type': 'NUMBER',
                    'value': res,
                    'line': line,
                    'col': col
                })
            else: 
                tokens.append({
                    'type': 'DECIMAL',
                    'value': res,
                    'line': line,
                    'col': col
                })

            pos += 1
            col += 1
            continue
        else:
            return f"Invalid character at line {line}, col {col}"

    return tokens
    # return Parser(tokens)


data = '15'
def run(text):
    output = Lexer(text)
    print(output)

run(data)

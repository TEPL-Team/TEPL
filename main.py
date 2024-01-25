### IMPORTS
### END OF IMPORTS

def interpreter(text):
    LENGTH = len(text)
    line = 1
    col = 0
    pos = 0
    tokens = []
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
        else:
            return f"Invalid character at line {line}, col {col}"

    return tokens


data = '"Hello, world!"'
def run(text):
    output = interpreter(text)
    print(output)

run(data)

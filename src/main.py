from interpreter import *


while True:
    try:
        text = input('>> ')
    except EOFError:
        quit(1)
    if not text:
        quit(0)
    result = parser.parse(text)
    interpret(result)


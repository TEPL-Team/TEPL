from tepl import *

while True:
    try:
        text = input('>> ')
    except EOFError:
        break
    if not text:
        continue
    result = parser.parse(text)
    print(result)

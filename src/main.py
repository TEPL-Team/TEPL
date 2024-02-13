from interpreter import *


while True:
    try:
        text = input('>> ')
    except EOFError:
        break
    if not text:
        break
    result = parser.parse(text)
    node = Node(result)

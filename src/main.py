from tepl import *

# running the code
if __name__ == "__main__":
    while True: 
        code = input(">> ")
        try: 
            parser.parse(code, lexer=lexer)
        except Exception as e:
            print(f'Error: {e}')
            break

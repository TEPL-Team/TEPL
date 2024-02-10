from tepl import *

# running the code
if __name__ == "__main__":
    while True: 
        code = input(">> ")
        try: 
            parser.parse(code, lexer=lexer)
            result = interpret(parser.parse(code, lexer=lexer))
            interpret(result)
        except Exception as e:
            print(f'Error: {e}')
            break

# Open and read the content of the index.tepl file
#with open('index.tepl', 'r') as file:
 #   file_content = file.read()

# Print the content of the index.tepl file
#print(parser.parse(file_content, lexer=lexer))


from src.lexer import lexer
from src.parser import parser, semantic_analysis
from src.interpreter import compile_ast
import sys

DEBUG = True

# Function to read the contents of a file
def read_file(file_path):
    """Read the contents of a file and return it as a string."""
    with open(file_path, 'r') as f:
        return f.read()
    
def write_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w') as f:
        f.write(content)

# Main function for interactive mode
def main():
    print('''TEPL compile_aster - v0.1\n\n''')
    while True:
        try:
            text = input('> ')
            if not text:
                exit(0)
            tree = parser.parse(text, lexer=lexer)
            if semantic_analysis(tree):
                compiled_code = compile_ast(tree)
                write_file('output.py', compiled_code)
                exec(open('output.py').read())
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {e}")

# Main function for debug mode
def main_debug():
    print('''TEPL Interpreter - v0.1
DEBUG Mode...\n\n''')
    while True:
        try:
            text = input('> ')
            if not text:
                exit(0)
            # Produce tokens from 'text' variable and print them
            print('TOKENS:')
            lexer.input(text)
            while True:
                tok = lexer.token()
                if not tok:
                    break
                print(
                    f'Token, Type: {tok.type}   Value: {tok.value}  \tLine #: {tok.lineno} Position: {tok.lexpos}'
                )
            # Parse tokens into an abstract syntax tree and print it
            tree = parser.parse(text)
            print('\nAST:')
            for node in tree:
                print(node)
            # Perform semantic analysis and compile_ast the abstract syntax tree if valid
            if semantic_analysis(tree):
                print('\nCompiled Code:')
                compiled_code = compile_ast(tree)
                print(compiled_code)
                write_file('output.py', compiled_code)
                print('\nOutput:')
                exec(open('output.py').read())
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {e}")

# Function to process input from a string or file
def process_input(input_source):
    """Process the input source, which can be a string or a file path."""
    try:
        if input_source.endswith('.tepl'):  # Assuming the file extension is .tepl
            text = read_file(input_source)
        else:
            text = input_source

        # Tokenize, parse, and compile_ast the input
        print('TOKENS:')
        lexer.input(text)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(
                f'Token, Type: {tok.type}   Value: {tok.value}  \tLine #: {tok.lineno} Position: {tok.lexpos}'
            )

        tree = None
        try:
            tree = parser.parse(text)
            print('\nAST:')
            if tree:
                for node in tree:
                    print(node)
        except IndexError as e:
            print(f"Error during parsing: '{e}'")

        if tree and semantic_analysis(tree):
            print('\nCompiled Code:')
            print(compile_ast(tree))
            write_file('output.py', compile_ast(tree))
            print('\nOutput:')
            exec(open('output.py').read())
    except Exception as e:
        print(f"Error: {e}")

# Entry point of the script
if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            input_source = sys.argv[1]
            process_input(input_source)
        else:
            if DEBUG:
                main_debug()
            else:
                main()
    except Exception as e:
        print(f"Error: {e}")

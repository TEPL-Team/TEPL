import argparse
from interpreter import interpret, parser
from lexer import lexer
from parser import __error__
from gui import run

__version__ = '0.73.75'

def run_script(filename):
    try:
        with open(filename, 'r') as file:
            script = file.read()
            result = parser.parse(script, lexer=lexer)
            interpret(result)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error executing script: {e}")

def main():
    _parser = argparse.ArgumentParser(description="TEPL Interpreter")
    _parser.add_argument("--run", help="Execute TEPL script from a file")
    args = _parser.parse_args()

    if args.run:
        run_script(args.run)
    else:
        while True:
            try:
                text = input('>> ')
            except EOFError:
                quit(1)
            
            if not text:
                quit(0)
            elif text == '--help':
                print('''Command List:
                    --help: view available commands
                    --ide: open the IDE
                    --run: run a file
                    --exit: exit the program
                    --clear: clear the console
                    --docs: view the documentation
                    --version: view the version of TEPL
                    --changelog: view the changelog
                    --license: view the license
                ''')
            elif text == '--ide':
                print('Opening the IDE...')
                run()
                print('Exiting...')
                exit(0)
            elif text == '--run':
                file_path = input('Enter the file path: ')
                run_script(file_path)
            else:
                result = parser.parse(text, lexer=lexer)
                if result and not __error__:
                    interpret(result)
                else:
                    break

if __name__ == "__main__":
    main()

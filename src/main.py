import argparse
from parser import __error__
from interpreter import interpret, parser
from lexer import lexer
from gui import run

__version__ = '1.00.00'
__mode__ = 'interpret' # 'interpret'|'parse'|'tokenize'


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
    global __mode__
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
                    --version: view the version
                    --changelog: view the changelog
                    --license: view the license
                    --mode: change the mode (interpret, parse, tokenize)
                ''')
            elif text == '--ide':
                print('Opening the IDE...')
                run()
                print('Exiting the IDE...')
            elif text == '--run':
                file_path = input('Enter the file path: ')
                run_script(file_path)
            elif text == '--exit':
                print('Exiting...')
                exit(0)
            elif text == '--version':
                print(f'TEPL Interpreter {__version__}')
            elif text == '--changelog':
                print('''V0.75.00 update: https://github.com/TENTHER101/TEPL/releases/tag/v0.75.00 
V1.00.00 update: https://github.com/TENTHER101/TEPL/releases/tag/v1.00.00''')
            elif text == '--license':
                print('License: https://github.com/TENTHER101/TEPL/blob/main/LICENSE')
            elif text == '--clear':
                # Clear the console
                print('To be implemented...')
                pass
            elif text == '--docs':
                print('''Documentation: https://tepl.vercel.app/docs
You may need to go to: https://tepl.vercel.app first and then move to the docs tab. 
                ''')
            elif text == '--mode':
                print('''Current mode: {__mode__}
Modes:
    interpret: interprets the script
    parse: parses the script
    tokenize: tokenizes the script''')
                nm = input('Enter the new mode(press enter to exit): ')
                if nm:
                    if nm == 'interpret':
                        __mode__ = 'interpret'
                    elif nm == 'parse':
                        __mode__ = 'parse'
                    elif nm == 'tokenize':
                        __mode__ = 'tokenize'
                    else:
                        print(f'{nm} is not a valid mode!')
                else: 
                    print('Exiting...')
                pass
            else:
                result = parser.parse(text, lexer=lexer)
                if result and not __error__:
                    result = interpret(result)
                    if result is not None:
                        print(result)
                else:
                    break


if __name__ == "__main__":
    main()

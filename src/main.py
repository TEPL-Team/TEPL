import argparse
from parser import __error__, parser
from lexer import lexer
from gui import run
from transpiler import transpile

__version__ = '1.47.38'
__mode__ = 'execute'  # 'execute' | 'transpile'|'parse'|'tokenize'


def run_script(filename):
    try:
        with open(filename, 'r') as file:
            script = file.read()
            result = parser.parse(script, lexer=lexer)
            if result and not __error__:
                transpiled_code = transpile(result)
            else:
                return
            exec(transpiled_code)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error executing script: {e}")


def main():
    global __mode__
    _parser = argparse.ArgumentParser(description="TEPL Transpiler")
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
                    --mode: change the mode (transpile, parse, tokenize)
                ''')
            elif text == '--ide':
                print(
                    'WARNING: IDE IS CURRENTLY NOT WORKING PROPERLY, USE CONSOLE INSTEAD'
                )
                print('Opening the IDE...')
                run()
                print('Exiting the IDE...')
            elif text == '--run':
                file_path = input('Enter the file path: ')
                with open(file_path, "r") as file:
                    data = file.read()

                if __mode__ == 'execute':
                    ast = parser.parse(data, lexer=lexer)
                    compiled_code = transpile(ast)
                    if compiled_code is not None:
                        exec(compiled_code)
                    else:
                        print(
                            "\nCannot execute. Compiled code is None. Please compile the AST first."
                        )
                elif __mode__ == 'transpile':
                    ast = parser.parse(data, lexer=lexer)
                    compiled_code = transpile(ast)
                    if compiled_code is not None:
                        print(compiled_code)
                    else:
                        print(
                            "\nCannot execute. Compiled code is None. Please compile the AST first."
                        )
                elif __mode__ == 'parse':
                    ast = parser.parse(data, lexer=lexer)

                    for node in ast:
                        print(node)
                elif __mode__ == 'tokenize':
                    tokens = lexer.input(data)
                    while True:
                        tok = lexer.token()
                        if not tok:
                            break  # No more input
                        print('Token, Type:' + str(tok.type) + '   Value:' +
                              str(tok.value) + '  \tLine #:' +
                              str(tok.lineno) + ' Position:' + str(tok.lexpos))
            elif text == '--exit':
                print('Exiting...')
                exit(0)
            elif text == '--version':
                print(f'TEPL Transpiler {__version__}')
            elif text == '--changelog':
                print(
                    '''V0.75.00 update: https://github.com/TENTHER101/TEPL/releases/tag/v0.75.00 
V1.00.00 update: https://github.com/TENTHER101/TEPL/releases/tag/v1.00.00''')
            elif text == '--license':
                print(
                    'License: https://github.com/TENTHER101/TEPL/blob/main/LICENSE'
                )
            elif text == '--clear':
                # Clear the console
                print('To be implemented...')
                pass
            elif text == '--docs':
                print('''Documentation: https://tepl.vercel.app/docs
You may need to go to: https://tepl.vercel.app first and then move to the docs tab. 
                ''')
            elif text == '--mode':
                print(f'''Current mode: {__mode__}
Modes:
    execute: executes transpiled code
    transpile: transpiles the script
    parse: parses the script
    tokenize: tokenizes the script''')
                nm = input('Enter the new mode(press enter to exit): ')
                if nm:
                    if nm == 'transpile':
                        __mode__ = 'transpile'
                    elif nm == 'parse':
                        __mode__ = 'parse'
                    elif nm == 'tokenize':
                        __mode__ = 'tokenize'
                    elif nm == 'execute':
                        __mode__ = 'execute'
                    else:
                        print(f'{nm} is not a valid mode!')
                else:
                    print('Exiting...')
                pass
            else:
                try:
                    if __mode__ == 'execute':
                        result = parser.parse(text, lexer=lexer)
                        if result and not __error__:
                            transpiled_code = transpile(result)
                        else:
                            break

                        exec(transpiled_code)
                    elif __mode__ == 'transpile':
                        result = parser.parse(text, lexer=lexer)
                        if result and not __error__:
                            transpiled_code = transpile(result)
                            if transpiled_code is not None:
                                print(transpiled_code)
                        else:
                            break
                    elif __mode__ == 'parse':
                        result = parser.parse(text, lexer=lexer)
                        if result:
                            print(result)
                        else:
                            break
                    elif __mode__ == 'tokenize':
                        lexer.input(text)
                        while True:
                            tok = lexer.token()
                            if not tok:
                                break  # No more input
                            print('Token, Type:' + str(tok.type) +
                                  '   Value:' + str(tok.value) +
                                  '  \tLine #:' + str(tok.lineno) +
                                  ' Position:' + str(tok.lexpos))
                except Exception as e:
                    print(f"Error: {e}")


if __name__ == "__main__":
    main()

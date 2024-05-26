import argparse
from parser import __error__, parser
from lexer import lexer
from gui import run
from transpiler import transpile

__version__ = 'v2.2.0'
__mode__ = 'execute'  # 'execute' | 'transpile'|'parse'|'tokenize'


def run_script(filename):
    try:
        with open(filename, 'r') as file:
            script = file.read()
            result = parser.parse(script, lexer=lexer)
            if result and not __error__:
                transpiled_code = transpile(result)
                exec(transpiled_code)
            else:
                print("Parsing error.")
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
                break

            if not text:
                break
            elif text == '--help':
                print_help()
            elif text == '--ide':
                print_ide_warning()
                run()
            elif text == '--run':
                handle_run_command()
            elif text == '--exit':
                print('Exiting...')
                break
            elif text == '--version':
                print(f'TEPL Transpiler {__version__}')
            elif text == '--changelog':
                print_changelog()
            elif text == '--license':
                print_license()
            elif text == '--clear':
                clear_console()
            elif text == '--docs':
                print_docs()
            elif text == '--mode':
                change_mode()
            else:
                handle_text_input(text)


def print_help():
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


def print_ide_warning():
    print(
        'WARNING: IDE IS CURRENTLY NOT WORKING PROPERLY, USE CONSOLE INSTEAD')
    print('Opening the IDE...')


def handle_run_command():
    global __mode__
    file_path = input('Enter the file path: ')
    try:
        with open(file_path, "r") as file:
            data = file.read()
        ast = parser.parse(data, lexer=lexer)
        if __mode__ == 'execute':
            execute_ast(ast)
        elif __mode__ == 'transpile':
            transpile_ast(ast)
        elif __mode__ == 'parse':
            parse_ast(ast)
        elif __mode__ == 'tokenize':
            tokenize_script(data)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error handling file: {e}")


def execute_ast(ast):
    transpiled_code = transpile(ast)
    if transpiled_code is not None:
        exec(transpiled_code)
    else:
        print(
            "\nCannot execute. Compiled code is None. Please compile the AST first."
        )


def transpile_ast(ast):
    transpiled_code = transpile(ast)
    if transpiled_code is not None:
        print(transpiled_code)
    else:
        print(
            "\nCannot execute. Compiled code is None. Please compile the AST first."
        )


def parse_ast(ast):
    if ast:
        for node in ast:
            print(node)
    else:
        print("Parsing error.")


def tokenize_script(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(
            f'Token, Type: {tok.type}   Value: {tok.value}  \tLine #: {tok.lineno} Position: {tok.lexpos}'
        )


def print_changelog():
    print(
        '''V0.75.00 update: https://github.com/TENTHER101/TEPL/releases/tag/v0.75.00 
V1.00.00 update: https://github.com/TENTHER101/TEPL/releases/tag/v1.00.00''')


def print_license():
    print('License: https://github.com/TENTHER101/TEPL/blob/main/LICENSE')


def clear_console():
    print('To be implemented...')


def print_docs():
    print('''Documentation: https://tepl.vercel.app/docs
You may need to go to: https://tepl.vercel.app first and then move to the docs tab.
    ''')


def change_mode():
    global __mode__
    print(f'''Current mode: {__mode__}
Modes:
    execute: executes transpiled code
    transpile: transpiles the script
    parse: parses the script
    tokenize: tokenizes the script''')
    nm = input('Enter the new mode (press enter to exit): ')
    if nm:
        if nm in ['execute', 'transpile', 'parse', 'tokenize']:
            __mode__ = nm
        else:
            print(f'{nm} is not a valid mode!')
    else:
        print('Exiting...')


def handle_text_input(text):
    global __mode__
    try:
        if __mode__ == 'execute':
            result = parser.parse(text, lexer=lexer)
            if result and not __error__:
                transpiled_code = transpile(result)
                exec(transpiled_code)
            else:
                print("Parsing error.")
        elif __mode__ == 'transpile':
            result = parser.parse(text, lexer=lexer)
            if result and not __error__:
                transpiled_code = transpile(result)
                if transpiled_code is not None:
                    print(transpiled_code)
        elif __mode__ == 'parse':
            result = parser.parse(text, lexer=lexer)
            if result:
                print(result)
        elif __mode__ == 'tokenize':
            lexer.input(text)
            while True:
                tok = lexer.token()
                if not tok:
                    break
                print(
                    f'Token, Type: {tok.type}   Value: {tok.value}  \tLine #: {tok.lineno} Position: {tok.lexpos}'
                )
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

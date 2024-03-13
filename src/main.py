from interpreter import *
#from gui import *

__version__ = '0.72.3'

from gui import run

while True:
    try:
        text = input('>> ')
    except EOFError:
        quit(1)
    if not text:
        quit(0)
    elif text == '--help':
        print(f'''Command List:

            --help: current ran, view commands
            --ide: open the IDE
            --run: run a file, syntax : --run <file_name.tepl>
            --exit: exit the program, alternative: enter nothing
            --clear: clear the console
            --docs: view the documentation, here: https://tepl.vercel.app/docs.html
            --version: view the version of TEPL, currently: {__version__}
            --changelog: view the changelog, here: https://tepl.vercel.app/download.html
            --license: view the license, here: 
        ''')
    elif text == '--ide':
        print('Opening the IDE...')
        run()
        print('Running...')
        exit(0)
    result = parser.parse(text)
    interpret(result)


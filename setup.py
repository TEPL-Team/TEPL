import sys
from cx_Freeze import setup, Executable


# Dependencies
build_exe_options = {
    "include_files": [
        ("src/lexer.py", "lexer.py"),  # Include lexer.py
        ("src/parser.py", "parser.py"),  # Include parser.py
        ("src/interpreter.py", "interpreter.py"), # Include interpreter.py
        ("src/gui.py", "gui.py") # Include gui.py
    ]
}

# Executable
executables = [
    Executable(
        "src/main.py",        # Entry point script
        target_name="tepl07500.exe"  # Name of the executable
    )
]

setup(
    name="TEPL App",
    version="0.1",
    description="Description of your TEPL app",
    options={"build_exe": build_exe_options},
    executables=executables
)

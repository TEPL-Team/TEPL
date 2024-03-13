import tkinter as tk
from interpreter import interpret, parser

def run():
    def run_interpreter():
        code = editor.get("1.0", tk.END)
        result = interpret(parser.parse(code))
        output_area.config(state=tk.NORMAL)
        output_area.delete("1.0", tk.END)
        output_area.insert(tk.END, str(result))
        output_area.config(state=tk.DISABLED)

    root = tk.Tk()
    root.title("TEPL IDE")

    editor = tk.Text(root, wrap=tk.WORD, width=80, height=20)
    editor.pack(padx=10, pady=10)

    run_button = tk.Button(root, text="Run Interpreter", command=run_interpreter)
    run_button.pack(pady=10)

    output_area = tk.Text(root, wrap=tk.WORD, width=80, height=10)
    output_area.pack(padx=10, pady=10)
    output_area.config(state=tk.DISABLED)

    root.mainloop()

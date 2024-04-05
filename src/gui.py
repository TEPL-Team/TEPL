import tkinter as tk
from transpiler import transpile
from parser import parser, __error__

def run():
    def run_transpiler():
        code = editor.get("1.0", tk.END)
        result = transpile(parser.parse(code))
        result = f'{str(exec(result))}'
        output_area.config(state=tk.NORMAL)
        output_area.delete("1.0", tk.END)
        output_area.insert(tk.END, str(result))
        output_area.config(state=tk.DISABLED)

    root = tk.Tk()
    root.title("TEPL IDE")

    editor = tk.Text(root, wrap=tk.WORD, width=80, height=20)
    editor.pack(padx=10, pady=10)

    run_button = tk.Button(root, text="Run Transpiiler", command=run_transpiler)
    run_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=10)

    output_area = tk.Text(root, wrap=tk.WORD, width=80, height=10)
    output_area.pack(padx=10, pady=10)
    output_area.config(state=tk.DISABLED)

    root.mainloop()

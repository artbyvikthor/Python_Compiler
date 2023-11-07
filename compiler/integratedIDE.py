import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import basic  # Import your Basic.py module

compiler = tk.Tk()
compiler.title('MUMU IDE')
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', 'end')
        editor.insert('1.0', code)
        set_file_path(path)

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', 'end')
        file.write(code)
        set_file_path(path)

def run_basic_code():
    if file_path == '':
        save_prompt = tk.Toplevel()
        text = tk.Label(save_prompt, Text='Please save your code')
        text.pack()
        return

    code = editor.get('1.0', 'end-1c')
    ast, error = basic.run('<stdin>', code)

    if error:
        code_output.delete('1.0', 'end-1c')
        code_output.insert('1.0', error.as_string())
    else:
        code_output.delete('1.0', 'end-1c')
        code_output.insert('1.0', ast)

menu_bar = tk.Menu(compiler)  # Specify tk.Menu

file_menu = tk.Menu(menu_bar, tearoff=0)  # Specify tk.Menu
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=compiler.quit)  # Use compiler.quit to exit
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = tk.Menu(menu_bar, tearoff=0)  # Specify tk.Menu

menu_bar.add_cascade(label='Run', menu=run_bar)

run_bar.add_command(label='Run Basic Code', command=run_basic_code)  # Add to run_bar, not menu_bar

compiler.config(menu=menu_bar)

editor = tk.Text(compiler)  # Specify tk.Text
editor.pack()

code_output = tk.Text(compiler, height=10)  # Specify tk.Text
code_output.pack()

compiler.mainloop()
import tkinter as tk
import Generator as gen
import pyperclip
def generate_key(keytext):
    keydone = "Пароль!"
    keytext.delete(0, tk.END)
    keydone = gen.generate(8)
    keytext.insert(0, keydone)
    keytext.config(text=keydone)

def copy(copytext):
    copytext = copytext.cget("text")
    pyperclip.copy(text=copytext)
def run_gui():
    root = tk.Tk()
    root.title('Key generator')

    keytext = tk.Entry(root,)
    keytext.pack()

    generate_button = tk.Button(root, text="Generate Key", command=lambda: generate_key(keytext))
    generate_button.pack()

    copybutton = tk.Button(root, text="Copy to clipboard", command=lambda: copy(keytext))
    copybutton.pack()

    root.geometry("400x600")
    root.resizable(False, False)
    root.iconbitmap(default="C:/Users/Allmost/Documents/GitHub/Key-generator/Main/icon.ico")

    root.mainloop()


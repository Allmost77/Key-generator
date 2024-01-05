import tkinter as tk
import Generator as gen

def generate_key(keytext):
    keydone = gen.generate(8)
    keytext.config(text=keydone)

def run_gui():
    root = tk.Tk()
    root.title('Key generator')

    keytext = tk.Label(root, text="")
    keytext.pack()

    generate_button = tk.Button(root, text="Generate Key", command=lambda: generate_key(keytext))
    generate_button.pack()

    root.geometry("400x600")
    root.resizable(False, False)
    root.iconbitmap(default="C:/Users/Allmost/Documents/GitHub/Key-generator/Main/icon.ico")

    root.mainloop()


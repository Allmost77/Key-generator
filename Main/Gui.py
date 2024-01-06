import tkinter as tk
import Generator as gen
import pyperclip

def generate_key(keytext):
    keytext.delete(0, tk.END)
    keydone = gen.generate()
    keytext.insert(0, keydone)


def copy_to_clipboard(copytext):
    copytext_value = copytext.get()
    pyperclip.copy(text=copytext_value)

def run_gui():
    root = tk.Tk()
    root.title('Key generator url')

    keytext = tk.Entry(root, width=49)
    keytext.pack()

    generate_button = tk.Button(root, text="Generate Key", command=lambda: generate_key(keytext))
    generate_button.pack()

    copy_button = tk.Button(root, text="Copy to clipboard", command=lambda: copy_to_clipboard(keytext))
    copy_button.pack()

    root.resizable(True, True)

    root.mainloop()

if __name__ == "__main__":
    run_gui()

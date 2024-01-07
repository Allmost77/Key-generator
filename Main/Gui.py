import tkinter as tk
import Generator as gen
import pyperclip

def generate_key(keylabel, key_length_var, num_turn_var, special_chars_turn_var):
    key_length = int(key_length_var.get())
    use_digits = num_turn_var.get() == '1'
    use_special_chars = special_chars_turn_var.get() == '1'
    keydone = gen.generate(key_length, use_digits, use_special_chars)
    keylabel.config(text=keydone)

def copy(copytext):
    copytext = copytext.cget("text")
    pyperclip.copy(text=copytext)

def run_gui():
    root = tk.Tk()
    root.title('Key generator')

    frame = tk.Frame(root)
    frame.pack()

    key_length_var = tk.StringVar(value='8')
    text_len = tk.Entry(frame, textvariable=key_length_var)
    text_len.pack(side=tk.LEFT)

    keylabel = tk.Label(root, text="")
    keylabel.pack()

    special_chars_turn_var = tk.StringVar(value='0')
    num_turn_var = tk.StringVar(value='0')  

    special_chars_turn = tk.Checkbutton(root, text="Turn Special Characters", variable=special_chars_turn_var, onvalue='1', offvalue='0')
    special_chars_turn.pack()

    num_turn = tk.Checkbutton(root, text="Turn Numbers", variable=num_turn_var, onvalue='1', offvalue='0')
    num_turn.pack()

    generate_button = tk.Button(frame, text="Generate Key", command=lambda: generate_key(keylabel, key_length_var, num_turn_var, special_chars_turn_var))
    generate_button.pack(side=tk.LEFT)

    button_len = tk.Button(root, text="Set Length", command=lambda: key_length_var.set(text_len.get()))
    button_len.pack()

    copybutton = tk.Button(root, text="Copy to clipboard", command=lambda: copy(keylabel))
    copybutton.pack()

    root.geometry("400x600")
    root.resizable(False, False)

    root.mainloop()


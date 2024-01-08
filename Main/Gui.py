import tkinter as tk
import Generator as gen
import pyperclip

def generate_key(keylabel, key_length_var, num_turn_var, special_chars_turn_var):
    try:
        key_length = int(key_length_var.get())
        use_digits = num_turn_var.get() == '1'
        use_special_chars = special_chars_turn_var.get() == '1'
        keydone = gen.generate(key_length, use_digits, use_special_chars)
        keylabel.config(text=keydone)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def copy(copytext):
    copytext = copytext.cget("text")
    pyperclip.copy(text=copytext)

def set_length(key_length_var, text_len_var):
    try:
        key_length_var.set(int(text_len_var.get()))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def run_gui():
    root = tk.Tk()
    root.title('Key generator')
    root.configure(bg='#d9d9d9')

    frame = tk.Frame(root, bg='#d9d9d9')  # Match background color
    frame.pack(padx=20, pady=20)

    key_length_var = tk.StringVar(value='8')
    keylabel = tk.Label(frame, text="", font=("Courier New", 10), bg='#d9d9d9', width=30, height=2, relief=tk.GROOVE)
    keylabel.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

    special_chars_turn_var = tk.StringVar(value='0')
    num_turn_var = tk.StringVar(value='0')

    special_chars_turn = tk.Checkbutton(frame, text="Turn Special Characters", variable=special_chars_turn_var, onvalue='1', offvalue='0', bg='#d9d9d9', font=("Segoe UI", 9))
    special_chars_turn.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    num_turn = tk.Checkbutton(frame, text="Turn Numbers", variable=num_turn_var, onvalue='1', offvalue='0', bg='#d9d9d9', font=("Segoe UI", 9))
    num_turn.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    text_len = tk.Entry(frame, font=("Courier New", 10), bg='white', width=20, bd=2, relief=tk.GROOVE)
    text_len.grid(row=3, column=0, padx=10, pady=10)

    generate_button = tk.Button(frame, text="Generate Key", command=lambda: generate_key(keylabel, key_length_var, num_turn_var, special_chars_turn_var), font=("Segoe UI", 9), bg='#d9d9d9')
    generate_button.grid(row=4, column=0, padx=10, pady=10)

    button_len = tk.Button(frame, text="Set Length", command=lambda: set_length(key_length_var, text_len), font=("Segoe UI", 9), bg='#d9d9d9')
    button_len.grid(row=3, column=1, padx=10, pady=10)

    copybutton = tk.Button(frame, text="Copy to clipboard", command=lambda: copy(keylabel), font=("Segoe UI", 9), bg='#d9d9d9')
    copybutton.grid(row=4, column=1, padx=10, pady=10)

    root.geometry("400x400")
    root.resizable(False, False)

    root.mainloop()

run_gui()

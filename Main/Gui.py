import tkinter as tk
import Main

def generate_key():
    keydone = Main.generate(8)
    keytext.config(text=keydone)

root = tk.Tk()
root.title('Key generator')

keytext = tk.Label(root, text="")
keytext.pack()

generate_button = tk.Button(root, text="Generate Key", command=generate_key)
generate_button.pack()

root.geometry("400x600")
root.resizable(False, False)
root.iconbitmap(default="icon.ico")

root.mainloop()


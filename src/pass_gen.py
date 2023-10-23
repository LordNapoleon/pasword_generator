from tkinter import *
from tkinter import ttk, messagebox
import string
import secrets

def generate_password(pass_len, use_upper=True, use_nums=True, use_special_chars=True):
    char = string.ascii_lowercase
    if use_upper:
        char += string.ascii_uppercase
    if use_nums:
        char += string.digits
    if use_special_chars:
        char += string.punctuation

    password = "".join(secrets.choice(char) for i in range(pass_len))
    return password

def generate():
    try:
        password_len = int(password_var.get())
        password_generated = generate_password(password_len, upper_var.get(), nums_var.get(), special_chars_var.get())
        password_display_var.set(password_generated)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

def copy_password():
    top.clipboard_clear()
    top.clipboard_append(password_display_var.get())
    copy_button.config(text="Password Copied!", state=DISABLED)
    top.after(2000, lambda: copy_button.config(text="Copy Password", state=NORMAL))

top = Tk()
top.geometry("280x275")

frame = Frame(top)
frame.pack()

password_label = Label(top, text="Password Length")
password_label.pack(padx=5, pady=5)
password_var = StringVar()
password = Entry(top, width=20, show="", textvariable=password_var)
password.pack(padx=5, pady=0)

output_label = Label(top, text="Password:")
output_label.pack(padx=5, pady=10)
password_display_var = StringVar()
password_display = Entry(top, width=20, state=DISABLED, textvariable=password_display_var)
password_display.pack(padx=5, pady=0)

upper_var = BooleanVar(value=True)
upper_checkbox = Checkbutton(top, text="Include Uppercase", variable=upper_var)
upper_checkbox.pack(padx=5, pady=1)

nums_var = BooleanVar(value=True)
nums_checkbox = Checkbutton(top, text="Include Numbers", variable=nums_var)
nums_checkbox.pack(padx=5, pady=1)

special_chars_var = BooleanVar(value=True)
special_chars_checkbox = Checkbutton(top, text="Include Special Characters", variable=special_chars_var)
special_chars_checkbox.pack(padx=5, pady=1)

button = ttk.Button(top, text="Generate Password", command=generate)
button.pack(padx=5, pady=5)

copy_button = ttk.Button(top, text="Copy Password", command=copy_password)
copy_button.pack(padx=5, pady=3)

top.title("Password Generator")
top.mainloop()

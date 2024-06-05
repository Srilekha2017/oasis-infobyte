import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("300x250")

        self.password_length_label = tk.Label(master, text="Password Length:")
        self.password_length_label.pack()
        self.password_length_entry = tk.Entry(master)
        self.password_length_entry.pack()

        self.complexity_label = tk.Label(master, text="Password Complexity:")
        self.complexity_label.pack()
        self.complexity_var = tk.StringVar(master, "Medium")
        self.complexity_dropdown = tk.OptionMenu(master, self.complexity_var, "Low", "Medium", "High")
        self.complexity_dropdown.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_display = tk.Text(master, height=1, width=30)
        self.password_display.pack()

        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()

    def generate_password(self):
        length = self.validate_input(self.password_length_entry.get())
        complexity = self.complexity_var.get()

        if length is not None:
            if complexity == "Low":
                charset = string.ascii_letters + string.digits
            elif complexity == "Medium":
                charset = string.ascii_letters + string.digits + string.punctuation
            else:  # High complexity
                charset = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

            password = ''.join(random.choice(charset) for _ in range(length))
            self.password_display.delete(1.0, tk.END)
            self.password_display.insert(tk.END, password)
        else:
            messagebox.showerror("Error", "Invalid password length. Please enter a positive integer.")

    def validate_input(self, input_text):
        try:
            length = int(input_text)
            if length <= 0:
                return None
            else:
                return length
        except ValueError:
            return None

    def copy_to_clipboard(self):
        password = self.password_display.get(1.0, tk.END).strip()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard.")
        else:
            messagebox.showerror("Error", "No password generated yet.")

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

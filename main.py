import string
import random
import tkinter as tk

def password_generation(symbols, using_upper_case, using_numbers, using_special_characters):
    try:
        password_length = int(password_length_get.get())
        if using_upper_case.get():
            symbols += uppercase_alphabet

        if using_numbers.get():
            symbols += digits

        if using_special_characters.get():
            symbols += special_characters

        password = ''

        for symbol in range(password_length):
            password += random.choice(symbols)

        password_window.delete('1.0', tk.END)
        password_window.insert(tk.END, password)


    except ValueError:
        pass

symbols = string.ascii_lowercase
uppercase_alphabet = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

root = tk.Tk()
root.title("Генератор паролей")
root.geometry("300x400")

using_upper_case = tk.IntVar()
using_upper_case_сheckbutton = tk.Checkbutton(root, text="Использовать верхний регистр", variable=using_upper_case)
using_upper_case_сheckbutton.pack()

using_numbers = tk.IntVar()
using_numbers_сheckbutton = tk.Checkbutton(root, text="Использовать цифры", variable=using_numbers)
using_numbers_сheckbutton.pack()

using_special_characters = tk.IntVar()
using_special_characters_сheckbutton = tk.Checkbutton(root, text="Использовать специальные символы", variable=using_special_characters)
using_special_characters_сheckbutton.pack()

password_length_get = tk.Entry(root)
password_length_get.pack()

generation_password_button = tk.Button(root, text = 'Сгенерировать пароль', command = lambda: password_generation(symbols, using_upper_case, using_numbers, using_special_characters))
generation_password_button.pack()

password_window = tk.Text(root, height=1, width=30)
password_window.insert(tk.END, "")
password_window.pack(pady=10)

root.mainloop()
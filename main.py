import string
import random
import tkinter as tk

password_length = 10

def password_generation(symbols, password_length, using_upper_case, using_numbers, using_special_characters):
    if using_upper_case:
        symbols += uppercase_alphabet

    if using_numbers:
        symbols += digits

    if using_special_characters:
        symbols += special_characters

    password = ''

    for symbol in range(password_length):
        password += random.choice(symbols)

    print(password)

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

generation = password_generation(symbols, password_length, using_upper_case, using_numbers, using_special_characters)
generation_password_button = tk.Button(root, text = 'Сгенерировать пароль', command = generation)
generation_password_button.pack()

root.mainloop()
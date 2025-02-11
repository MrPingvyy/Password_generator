import string # Импорты
import random
import tkinter as tk

def password_generation(): # Функция генерации пароля
    symbols = string.ascii_lowercase # В переменную symbols записываются все буквы англ. алфавита нижнего регистра
    try:
        password_length = int(password_length_get.get())
        if using_upper_case.get():
            symbols += string.ascii_uppercase # В переменную symbols добавляются все буквы англ. алфавита верхнего регистра

        if using_numbers.get():
            symbols += string.digits # В переменную symbols добавляются все цифры

        if using_special_characters.get():
            symbols += string.punctuation # В переменную symbols добавляются все специальные символы

        password = ''

        for symbol in range(password_length):
            password += random.choice(symbols) # В Генерируется рандомный пароль

        password_window.delete('1.0', tk.END) # Удаляется имеющийся текст
        password_window.insert(tk.END, password) # Выводится новый текст

    except ValueError:
        pass

root = tk.Tk()
root.title("Генератор паролей") # Установка названия окна
root.geometry("300x400") # Установка размера окна

generation_password_button = tk.Button(root, text = 'Сгенерировать пароль', command = password_generation) # Кнопка, которая по нажатию вызывает функцию
generation_password_button.pack(pady = 10)

frame = tk.Frame(root)
frame.pack(anchor = "w")

message = tk.Message(frame, text = "Введите длинну пароля", width = 300) # Текст
message.pack(side = tk.LEFT, padx = 5, pady = 10)

password_length_get = tk.Entry(frame) # Поле для ввода текста
password_length_get.pack(side = tk.LEFT)

using_upper_case = tk.IntVar()
using_upper_case_сheckbutton = tk.Checkbutton(root, text = "Испльзовать верхний регистр", variable = using_upper_case) # Флажок
using_upper_case_сheckbutton.pack(anchor = "w", padx = 5, pady = 10)

using_numbers = tk.IntVar()
using_numbers_сheckbutton = tk.Checkbutton(root, text="Использовать цифры", variable = using_numbers) # Флажок
using_numbers_сheckbutton.pack(anchor = "w", padx = 5, pady = 10)

using_special_characters = tk.IntVar()
using_special_characters_сheckbutton = tk.Checkbutton(root, text = "Использовать специальные символы", variable = using_special_characters) # Флажок
using_special_characters_сheckbutton.pack(anchor = "w", padx = 5, pady = 10)

password_window = tk.Text(root, height = 1, width = 30)  # Текстовое поле в котором выводится пароль
password_window.insert(tk.END, "")
password_window.pack(pady = 50)

root.mainloop()  # Обновление
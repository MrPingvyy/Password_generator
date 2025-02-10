import string
import random

symbols = string.ascii_lowercase
uppercase_alphabet = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

password_length = int(input('Введите длинну пароля - '))
using_upper_case = input('Использовать верхний регистр? ')
using_numbers = input('Использовать цифры? ')
using_special_characters = input('Использовать специальные символы? ')

if using_upper_case == 'Да':
    symbols += uppercase_alphabet

if using_numbers == 'Да':
    symbols += digits

if using_special_characters == 'Да':
    symbols += special_characters

password = ''

for symbol in range(password_length):
    password += random.choice(symbols)

print(password)
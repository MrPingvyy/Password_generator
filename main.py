import string
import random

lowercase_alphabet = string.ascii_lowercase
uppercase_alphabet = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

password_length = int(input('Введите длинну пароля - '))
using_upper_case = input('Использовать верхний регистр? ')
using_numbers = input('Использовать цифры? ')
using_special_characters = input('Использовать специальные символы? ')

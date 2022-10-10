import string
import random as rnd
import os
import json


# Условие: Функция generate_txt_data. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100, но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы.


def generate_txt_data() -> str:
    txt_data_length = rnd.randint(100, 1000)
    available_symbols = [*string.ascii_letters, *string.digits, " "]
    txt_data = "".join([rnd.choice(available_symbols) for _ in range(txt_data_length)])
    return txt_data


# Условие: Функция generate_json_data. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5, но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.


def generate_key() -> str:
    key = "".join([rnd.choice(string.ascii_lowercase) for _ in range(5)])
    return key


def generate_value() -> str:
    value = rnd.choice([rnd.randint(-100, 100), rnd.random(), rnd.choice([True, False])])
    return value


def generate_json_data() -> dict:
    json_data_length = rnd.randint(5, 20)
    json_data = {generate_key(): generate_value() for _ in range(json_data_length)}
    return json_data


# Условие: Функция generate_and_write_file. Написать функцию, которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"
#
# Разрешается создавать дополнительные (вспомогательные) функции.


def generate_and_write_file(path: str):
    if os.path.splitext(path)[1] == ".txt":
        with open(path, "w") as file:
            file.write(generate_txt_data())
    elif os.path.splitext(path)[1] == ".json":
        with open(path, "w") as file:
            file.write(json.dumps(generate_json_data()))
    else:
        print("Unsupported file format")

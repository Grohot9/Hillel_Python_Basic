# 1. Условие:  Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
def reverse_words_at_odd_positions(lst: list) -> list:
    return [word if index % 2 == 1 else word[::-1] for index, word in enumerate(lst)]


my_list = ["apple", "orange", "cherry", "strawberry"]
words_with_reverse_at_odd_positions: list = reverse_words_at_odd_positions(my_list)

# 2. Условие:  Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".
def filter_by_the_char_a_in_the_first_position(lst: list) -> list:
    return [word for word in lst if word[0].lower() == "a"]


my_list = ["Artyom", "Marina", "Evgeniy", "Dmitry", "Ludmila", "Andrew", "Alyona", "Yuri"]
words_with_char_a_in_the_first_position: list = filter_by_the_char_a_in_the_first_position(my_list)

# 3. Условие: Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.
def filter_by_the_char_a_in_the_word(lst: list) -> list:
    return [word for word in lst if "a" in word.lower()]


my_list = ["Artyom", "Marina", "Evgeniy", "Dmitry", "Ludmila", "Andrew", "Alyona", "Yuri"]
words_with_char_a: list = filter_by_the_char_a_in_the_word(my_list)

# 4. Условие: Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
def filter_by_str_type(lst: list) -> list:
    return [item for item in lst if type(item) == str]


my_list = ["Igor", 9, "Python", "community", 102]
strings_from_my_list: list = filter_by_str_type(my_list)

# 5. Условие: Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
def take_chars_that_are_occur_only_once(string: str) -> list:
    return [char for char in set(string) if string.count(char) == 1]


my_str = "Сегодня был продуктивный день."
chars_that_are_occur_only_once_in_my_str: list = take_chars_that_are_occur_only_once(my_str)

# 6. Условие: Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
def take_chars_that_are_occur_in_both_strings(first_string: str, second_string: str) -> list:
    return [char for char in set(first_string) if char in second_string]


str1 = "Сегодня был солнечный день."
str2 = "Вчера был дождливый день."
chars_that_are_occur_in_str1_and_str2: list = take_chars_that_are_occur_in_both_strings(str1, str2)

# 7. Условие: Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
def take_chars_that_are_occur_once_in_both_strings(first_string: str, second_string: str) -> list:
    return [char for char in set(first_string) if first_string.count(char) == second_string.count(char) == 1]


str1 = "Сегодня был солнечный день."
str2 = "Вчера был дождливый день."
chars_that_are_occur_once_in_both_strings: list = take_chars_that_are_occur_once_in_both_strings(str1, str2)

# 8. Условие: Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
import random
import string

surnames = ["smith", "martinez", "hernandez", "rodriguez", "lopes", "johnson", "williams", "brown", "jones", "miller"]
domains = ["com", "net", "us", "ua", "me", "org", "gov"]


def generate_email(surnames: list = surnames, domains: list = domains) -> str:
    random_surname = random.choice(surnames)
    random_number = random.randint(100, 999)
    length_of_the_random_string = random.randint(5, 7)
    random_string = "".join([random.choice(string.ascii_lowercase) for _ in range(length_of_the_random_string)])
    random_domain = random.choice(domains)
    return f"{random_surname}.{random_number}@{random_string}.{random_domain}"


user_email = generate_email()
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com

# модули в пайтон
# словари


############ ВАРИАНТ №1
import random

value = random.randint(1, 10)
print(value)

value_2 = random.randint(2, 100)
print(value_2)

values = ["qwe", "asd", "zxc"]
# values = "asjkdfgaksdhvkahvkz"
value_3 = random.choice(values)
print(value_3)

############ ВАРИАНТ №2
from random import randint, choice

value = randint(1, 10)
print(value)

value_2 = randint(2, 100)
print(value_2)

values = ["qwe", "asd", "zxc"]
# values = "asjkdfgaksdhvkahvkz"
value_3 = choice(values)
print(value_3)


############ ВАРИАНТ №3

import random as rnd
# import numpy as np
# import pandas as pd
# import tensorflow as tf
# import cv2 as cv

value = rnd.randint(1, 10)
print(value)

value_2 = rnd.randint(2, 100)
print(value_2)

values = ["qwe", "asd", "zxc"]
# values = "asjkdfgaksdhvkahvkz"
value_3 = rnd.choice(values)
print(value_3)

################# словари
value = {"key": "value"}
print(value, type(value))

# словарь - изменяемый тип, порядок не гарантируется

# ключ - уникальное значение, остается последнее значение
# ключем может быть: int, float, str, bool-лучше не использовать???, любой неизменяемый объект (tuple)
# ключем НЕ может быть: изменяемый объект (list, set)
# значением может быть ЛЮБОЙ объект

my_dict = {False: 11,
           2: 22,
           3: 33,
           "4": 44,
           "5": 55,
           6.5: 123,
           0: True,
           True: False,
           3: 3333,
           (1, 2): "tuple",
           []: "qwe",
           }
print(my_dict)

address_1 = {'city': 'Dnipro',
             'street': 'Polya',
             'building': 123}
person_1 = {'name': 'John',
            'age': 23,
            'jobs': ['programmer', 'teacher'],
            'address': address_1}

address_2 = {'city': 'New York',
             'street': 'Polya',
             'building': 321}
person_2 = {'name': 'Jackob',
            'age': 32,
            'jobs': ['programmer',],
            'address': address_2}

persons = [person_1, person_2]

print(person_1["name"], person_1["job"])
print(person_2["name"], person_2["job"])

for person in persons:
    print(person["address"]["city"])
    print(person['jobs'][-1])


address = {'city': 'Dnipro',
           'street': 'Polya',
           'building': 123}

address['city'] = "London"
address["zip"] = 49000
address["zip"] = "49000"

address_2 = address.copy()
address_2['city'] = "QQQ"
print(address, address_2)

city = address["City"]
city = address.get("City")
print(city, address)

key = "Zip"
zip_value = address.pop(key)
print(zip_value, address)

if key in address:  # проверка только в ключах!!!
    address.pop(key)

for key in address:  # цикл только по ключам!!!
    print(key, address[key])


address = {'city': 'Dnipro',
           'street': 'Polya',
           'building': 123}

for key, value in address.items():
    print(key, value)

keys = list(address.keys())
print(keys)

values = list(address.values())
print(values)
address_additional_info = {'zip': '49000',
                           'apartment': 12,
                           'City': None}

address_info = {"info": "TEST"}

address.update(address_additional_info)
address.update(address_info)

new_address = {**address, **address_additional_info, **address_info}
print(new_address)

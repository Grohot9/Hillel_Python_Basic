# from lesson_11_tanos import create_directory
#
# print("lesson_11", __name__)
# dirname = "TEST4"
# create_directory(dirname)

import json


# values_str = "[1, 2, 3]"
# values_str = '''{"key": "value"}'''
#
# values = json.loads(values_str)
# print(values['key'], values)
#################################################
# address_1 = {'city': 'Dnipro',
#              'street': 'Polya',
#              'building': 123}
#
# data = json.dumps(address_1)
# print(data, type(data))

# def read_json(filename):
#     with open(filename, 'r') as json_file:
#         data = json.load(json_file)
#     return data
#
#
# def write_json(filename, data):
#     with open(filename, 'w') as json_file:
#         json.dump(data, json_file, indent=4)


# filename = "data.json"
# data = read_json(filename)
# print(data)
# data = {"name": "John", "address": {"city": "Dnipro", "street": "Polya", "building": 123}}
# filename_output = "out.json"
# write_json(filename_output, data)



#12#
# Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#13#
# Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу.

# my_str1 = 'qwwwwwertyi'
# my_str2 = 'qqqqqwertyo'
#
# common_elements = list(set(my_str1) & set(my_str2))
# unique_common_elements = []
#
# for element in common_elements:
#     if my_str1.count(element) == 1 and my_str2.count(element) == 1:
#         unique_common_elements.append(element)
# print(unique_common_elements)


def turning_string_list(my_list):
    new_list = []
    for index, item in enumerate(my_list):
        if index % 2 != 0:
            new_list.append(item[::-1])
        else:
            new_list.append(item)
    return new_list


my_list = ["321", "123", "qwe", "asd", "qwe", "asd", "qwe", "asd"]
new_list = [turning_string_list(my_list)]
print(new_list[0][0], "\t" "№1")

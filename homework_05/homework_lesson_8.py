# 1. Условие: Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
my_list = ["apple", "orange", "cherry", "strawberry"]

# Сделаем выборку по местам, а не индексам:
new_list = [word if index % 2 == 1 else word[::-1] for index, word in enumerate(my_list)]

# 2. Условие: Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
my_list = ["Артём", "Марина", "Евгений", "Дмитрий", "Людмила", "Андрей", "Алёна", "Юрий"]

name_with_first_char_a = [name for name in my_list if name[0].lower() == "а"]

# 3. Условие: Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
my_list = ["Артём", "Марина", "Евгений", "Дмитрий", "Людмила", "Андрей", "Алёна", "Юрий"]

name_with_char_a = [name for name in my_list if "а" in name.lower()]

# 4) Условие: Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
people = [{"name": "John", "age": 15},
          {"name": "Igor", "age": 17},
          {"name": "Sam", "age": 22},
          {"name": "Denis", "age": 15},
          {"name": "Anna", "age": 17},
          {"name": "Jack", "age": 45},
          {"name": "Sally", "age": 32}]

# а) Создать список и поместить туда имя самого молодого человека.
# Если возраст совпадает - поместить все имена самых молодых.
min_age_of_people = min({person["age"] for person in people})
list_of_youngest = [person["name"] for person in people if person["age"] == min_age_of_people]

# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
len_of_the_longest_name_of_people = max({len(person["name"]) for person in people})
list_of_longest_names = [person["name"] for person in people
                         if len(person["name"]) == len_of_the_longest_name_of_people]

# в) Посчитать среднее количество лет всех людей из начального списка.
average_age_of_people = round(sum([person["age"] for person in people]) / len(people))

# 5) Условие: Даны два словаря my_dict_1 и my_dict_2.
my_dict_1 = {
    "name": "Igor",
    "surname": "Samarsky",
    "age": 17,
    "nationality": "Ukrainian",
    "profession": "Backend Python Developer",
    "hobby": "sport"
}
my_dict_2 = {
    "name": "Denis",
    "surname": "Shapelich",
    "age": 17,
    "nationality": "Ukrainian",
    "hobby": "swimming"
}
# а) Создать список из ключей, которые есть в обоих словарях.
same_keys_of_dicts = list(my_dict_1.keys() & my_dict_2.keys())

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
unique_keys_of_the_my_dict_1 = list(my_dict_1.keys() - my_dict_2.keys())

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
new_dict = {key: value for key, value in my_dict_1.items() if key in unique_keys_of_the_my_dict_1}

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
custom_dict = {key: my_dict_1[key] for key in unique_keys_of_the_my_dict_1}
for key in same_keys_of_dicts:
    custom_dict[key] = [my_dict_1[key], my_dict_2[key]]

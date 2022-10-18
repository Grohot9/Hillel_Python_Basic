# 1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
# Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
# Пример:  my_str="blablacar", my_symbol="bla".
# Вывод на экран:
# 2

my_str = "blablacar"
my_symbol = "bla"
number = my_str.count(my_symbol)
print(number)

# 2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
# Напечатать столько раз my_symbol, сколько он встречается в my_str.
# Пример:  my_str="blablacar", my_symbol="bla".
# Вывод на экран:
# bla
# bla

for _ in range(number):
    print(my_symbol)

# 3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько
# РАЗНЫХ символов встречается в my_str.
# Большая и маленькая буква считается как один символ.
# Пробелы, запятые и т.д. считаем тоже как символы.
# Пример:  my_str="bla BLA car".
# Вывод на экран:
# 6

my_str = "bla BLA car"

result = len(set(my_str.lower()))
print(result)

unique_symbols = []
for symbol in my_str.lower():
    if symbol not in unique_symbols:
        unique_symbols.append(symbol)
print(len(unique_symbols), unique_symbols)

unique_symbols = ""
for symbol in my_str.lower():
    if symbol not in unique_symbols:
        unique_symbols += symbol
print(len(unique_symbols), unique_symbols)


# 4) Дана строка my_str и пустой список my_list.
# Заполнить my_list символами из my_str,
# которые стоят на четных местах в строке (считаем с 0)

my_str = "zhjdsgfz,jhvzxnvkzxnj"
my_list = []

for symbol in my_str[::2]:
    my_list.append(symbol)
print(my_list)

my_list += list(my_str[::2])
print(my_list)


# 5) Дана строка my_str, список str_indexes целых чисел в диапазоне от
# 0 до длинны строки минус 1, пустой список my_list.
# Заполнить my_list символами из my_str, которые стоят на местах с
# индексами из str_index

my_str = "qwertyuiop"
str_indexes = [0, 9, 9, 1, 5]
my_list = []
#
for index in str_indexes:
    value = my_str[index]
    my_list.append(value)
print(my_list)



# 6) Дано целое число (int). Определить сколько цифр в этом числе.
my_number = 12345670007654321000

print(len(str(my_number)))

# 7) Дано целое число. Определить наибольшую цифру в этом числе.

number_str = str(my_number)

number_str = "qwertyQWERTY1234@#$%^&Б"  # ASCII
max_digit = max(number_str)
print(max_digit)

print(ord("a"), chr(98))

for index in range(150, 200):
    print(index, chr(index))

# 8) Дано целое число. Составить число (int) с цифрами в обратном порядке.

str_number = str(my_number)
reversed_number = str_number[::-1]
new_number = int(reversed_number)

new_number = int(str(my_number)[::-1])

print(new_number)

# 9) Дано целое число. Составить число с цифрами в порядке возрастания(убывания).

values = [12, 2, 34, -6, 100]
new_values = values.copy()
new_values.sort()
print(values, new_values)

new_values = sorted(values)
print(values, new_values)


str_number = str(my_number)
sorted_number = sorted(str_number)
sorted_number = "".join(sorted_number)
number = int(sorted_number)

number = int("".join(sorted(str(my_number))))

print(number)



# 10) Даны списки my_list_1 и my_list_2.
# Создать список my_result в который поместить элементы из my_list_1 и
# my_list_2 через один, начиная с my_list_1.
# a) кол-во эл-тов одинаковое
# б) кол-во эл-тов разное, Остаток списка дописать в конец

my_list_1 = [1, 2, 3, 4, 5, 6, 7]
my_list_2 = [10, 20, 30, 40]
my_result = []

index_count = min(len(my_list_1), len(my_list_2))

for index in range(index_count):
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])

my_result = my_result + my_list_1[index_count:] + my_list_2[index_count:]

print(my_result)


# генераторы списков

numbers = [number for number in range(10)]

for number in range(10):
    numbers.append(number)
print(numbers)

squares = [number ** 2 for number in range(11, 21)]
print(squares)

values = [123, 23, -4, 78, -94, -1, 0]
positive_numbers = [value for value in values if value > 0 or value < -10]
print(positive_numbers)


# множества

values = [1, "3", "2", 2, "3", 3, 1]

my_set = set(values)
new_values = list(set(values))
print(my_set)

my_set = {1, 3, "asd"}
my_set = set()

################################

set_1 = {1, 2, 3, 3}
set_2 = {1, 20, 3, 40}
set_3 = {1, 20, 3, 50}

my_set = set_1 | set_2 | set_3
print(my_set)

print(set_1)
my_set = set_1.union(set_2, set_3)
print(my_set)

my_set = set_1.intersection(set_2)
print(my_set)

my_set = set_2.difference(set_1)
print(my_set)



################################
my_str = "qweeeeeeeeeeeeeeeeeee"

for symbol in set(my_str):
    print(symbol)

# 1) Условие: У вас есть список my_list со значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

my_list = [101, 85, 502, 421, 159, 21, 9, 100]

for integer in my_list:
    if integer > 100:
        print(integer)

# Ещё один вариант оформления:
# for integer in my_list:
#     print(integer) if integer > 100 else None

# И ещё один вариант оформления:
# [print(integer) for integer in my_list if integer > 100]

# 2) Условие: У вас есть список my_list со значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = [101, 85, 502, 421, 159, 21, 9, 100]
my_results = []

for integer in my_list:
    my_results.append(integer) if integer > 100 else None

print(my_results)

# 3) Условие: У вас есть список my_list со значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

my_list = [101, 85, 502, 421, 159, 21, 9, 100]

my_list.append(0) if len(my_list) < 2 else my_list.append(my_list[-2] + my_list[-1])

# if len(my_list) < 2:
#     my_list.append(0)
# else:
#     my_list.append(my_list[-2] + my_list[-1])

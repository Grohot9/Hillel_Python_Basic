# 1) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и распечатать их.

my_string = "0123456789"
for num_1 in my_string:
    for num_2 in my_string:
        print(int(num_1 + num_2))

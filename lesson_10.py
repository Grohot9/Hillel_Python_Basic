# ПЛОХИЕ ИМЕНА ПЕРЕМЕННЫХ
# number = "123"
# e_mail = ["qwe@qwe.com", "asd@asd.com"]
# value_list = 123
# file_names = "test.txt"
# value = [1, 2, 3]
# values = value[0]

# модуль os
# работа с файлами

import os

path = "Homeworks"
files = os.listdir(path)
print(files)


filename = "Homeworks/lesson_9.txt"


# 1 - можно, но осторожно ))

file = open(filename, 'r')
data = file.read()
print(data)
file.close()  # !!!!

#  2 - гараздо лучше!!!

with open(filename, 'r') as file:
    data = file.read()
# print(data)

filename_out = "test.txt"
text = data + "\n\nTEST"
with open(filename_out, 'w') as file_txt:
    file_txt.write(text)

#######################################
with open(filename, 'r') as file:
    data = [line.strip() for line in file.readlines()]
    # data = file.readlines()
# print(data)

filename_out = "test.txt"
data.append("TEST")
with open(filename_out, 'w') as file_txt:
    file_txt.writelines([f"{line}\n" for line in data])

######################################

with open(filename, 'r') as file:
    data = file.read().splitlines()
print(data)

filename_out = "test.txt"
data.append("TEST")
with open(filename_out, 'w') as file_txt:
    file_txt.write("\n".join(data))


def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read().splitlines()
    return data


data = read_file(filename)
print(data)

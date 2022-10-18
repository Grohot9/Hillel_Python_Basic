import os
import string
import random


# 1. Создать папку ./alphabet/ Если папка существует, то ОК.
location = "./"
file = "alphabet"
cwd = location + file


def create_file(path: str = cwd):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


create_file()
# 2. В папке ./alphabet/ создать файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
os.chdir(cwd)

for character in string.ascii_lowercase:
    with open(f"{character}.txt", "w") as file:
        file.write(string.ascii_lowercase.replace(character, character.upper()))
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
# files_for_delete = random.choices(string.ascii_lowercase.split(), k=len(string.ascii_lowercase) // 2)
# for del_file in files_for_delete:
#     os.remove(f"{location}{file}/{del_file}.txt")


def thanos_snap():
    for root, dirs, files in os.walk("../.."):
        files_for_delete = random.sample(files, k=len(files) // 2)
        for file_for_delete in files_for_delete:
            os.remove(file_for_delete)


thanos_snap()

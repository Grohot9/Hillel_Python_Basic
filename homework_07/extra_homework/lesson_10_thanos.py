# 1. Создать папку ./alphabet/ Если папка существует, то ОК.
# 2. В папке ./alphabet/ создать файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчок Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
import string
import random


class ThanosSnap:  # with encapsulation examples
    def __init__(self, dirname: str):
        self._dirname = dirname
        self._create_directory()

    @property
    def dirname(self):
        return self._dirname

    def _create_directory(self):
        os.makedirs(self._dirname, exist_ok=True)

    def crate_files(self):
        for symbol in string.ascii_lowercase:
            filename = os.path.join(self._dirname, f"{symbol}.txt")
            self._create_data_in_file(filename, symbol)

    @staticmethod
    def _create_data_in_file(filename: str, symbol: str):
        data = string.ascii_lowercase.replace(symbol, symbol.upper())
        with open(filename, "w") as file:
            file.write(data)

    def do_thanos_snap(self):
        listdir = os.listdir(self._dirname)
        random.shuffle(listdir)
        for filename in listdir[:len(listdir) // 2]:
            os.remove(os.path.join(self._dirname, filename))


if __name__ == "__main__":
    directory_name = "alphabet"
    example = ThanosSnap(directory_name)
    example.crate_files()
    example.do_thanos_snap()

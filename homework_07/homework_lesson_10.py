# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).
def get_domains(file_name: str) -> list:
    with open(file_name, "r") as domains:
        domains = [domain.strip(".\n") for domain in domains.readlines()]
    return domains


get_domains("domains.txt")

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"
def get_surnames(file_name: str) -> list:
    with open(file_name, "r") as names:
        surnames = [line_info.split()[1] for line_info in names.readlines()]
    return surnames


get_surnames("names.txt")

# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]
def get_dates(file_name: str) -> list:
    dates = []
    with open(file_name, "r") as file:
        for line in file.readlines():
            if "-" in line:
                dates += [{"date": line.split("-")[0].strip()}]
    return dates


get_dates("authors.txt")

# По просьбам некоторых студентов начну включать дополнительные задания.
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - это та же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
def get_original_and_modified_dates(file_name: str) -> list:
    months = {"January": "01",
              "February": "02",
              "March": "03",
              "April": "04",
              "May": "05",
              "June": "06",
              "July": "07",
              "August": "08",
              "September": "09",
              "October": "10",
              "November": "11",
              "December": "12"
              }
    dates = [{"date_original": date["date"]} for date in get_dates(file_name)]
    for date in dates:
        date_modified_year = date["date_original"].split()[-1]
        date_modified_month = months[date["date_original"].split()[-2]]
        if len(date["date_original"].split()) > 2:
            if len(date["date_original"].split()[-3]) == 3:
                date_modified_day = "0" + date["date_original"].split()[-3][0]
            else:
                date_modified_day = date["date_original"].split()[-3][0:2]
        else:
            date_modified_day = "__"
        date_modified = {"date_modified": f"{date_modified_day}/{date_modified_month}/{date_modified_year}"}
        date.update(date_modified)
    return dates
# Пришлось продумывать такую логику так как в одной из строк в файле authors.txt есть случай где указывается только
# месяц и год и я не знаю было ли так задумано или просто пропустили день в дате, так что сделал для этого случая
# вот такой вывод: {'date_original': 'December 1817', 'date_modified': '__/12/1817'}


get_original_and_modified_dates("authors.txt")

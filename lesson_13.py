# функции сортировки
# лямбда функции
# регулярные выражения
# csv
import json
import re

filename = "data.json"
with open(filename, 'r') as json_file:
    values = json.load(json_file)


values = [2, -3, 6, 100, 45]
sorted_values = values.copy()
sorted_values.sort(reverse=True)

values.sort(reverse=True)  # змінює обʼект

sorted_values = sorted(values, reverse=True)
print(values, sorted_values)
######################################
values = ['qwe123', "1as", "Z", "!zx"]
sorted_values = sorted(values, key=len, reverse=True)
print(sorted_values)

######################################
values = [2, -30, 30, 6, 100, 45]
sorted_values = sorted(values, key=abs)
print(sorted_values)

######################################
def sort_by_age(item):
    age = item["age"]
    return age


sorted_values = sorted(values, key=sort_by_age)
print(sorted_values)
######################################
def sort_by_name(item):
    name = item["name"]
    return len(name), name


sorted_values = sorted(values, key=sort_by_name)
print(sorted_values)

# ######################################
values = [(200, "-30"), (30, "a6"), (100, "45"), (30, "A6"), (10,)]
sorted_values = sorted(values)
print(sorted_values)

######################################

sorted_values = sorted(values, key=lambda item: item["age"])
print(sorted_values)

sorted_values = sorted(values, key=lambda item: (len(item["name"]), item["name"]))
print(sorted_values)
######################################
def sort_by_zip_number(item):
    zip_code = item["zip"]
    template = r"[0-9]+"
    zip_values = re.findall(template, zip_code)
    result = ''
    if zip_values:
        result = zip_values[0]
    return result


sorted_values = sorted(values, key=sort_by_zip_number)
print(sorted_values)


zip_code = 'YTRE290060POI'
# template = r"[А-ЯІїʼҐ]+"

template = r"\d+"

result = re.findall(template, zip_code)
print(result)

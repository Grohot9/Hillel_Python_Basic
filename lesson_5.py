# Fifth lesson: knowledge of for loops and enumerate method, string methods: count, strip, upper, lower, capitalize,
# replace, id() function

#####################################################
# for loop showcase:
my_str = "I'm a man. My mane is Volodymyr"

count = 0
for symbol in my_str:
    # if symbol.isalpha() and symbol.lower() not in "eyuioa":
    if symbol == " ":
        count += 1
        # print(symbol)
print(count)

#####################################################
# some string methods and id() function:

count = my_str.count(' ') + my_str.count('a')
count_space = my_str.count(' ')
count_a = my_str.count('a')
print(count)

my_str = "\n\t "
print(my_str.isspace())

my_str = "aesdeeeeeee"
my_str = my_str.strip('ed')
print(my_str)

my_str = " \t  qwerty@\n@\n"
# my_str = "aesdeeeeeee"

my_str = my_str.strip()
print(my_str)
print("-------")


print(id(my_str))
# new_str = my_str.upper()
my_str = my_str.lower()
print(my_str)
print(id(my_str))

my_str = my_str.capitalize()
print(my_str)

first_name_1 = "Vova"
first_name_2 = "VOvA"
print(first_name_1.upper() == first_name_2.upper())

new_str = my_str.replace("man", "woman", 1)
print(new_str)

#####################################################
# for loops and enumerate method:

my_str = "qwerty123"

for symbol in my_str:
    new_symbol = symbol * 2
    print(new_symbol)

for symbol in my_str[::2]:
    new_symbol = symbol * 2
    print(new_symbol)

for index in range(len(my_str)):
    if not index % 2 or not index % 3:   # math ))
        print(index, my_str[index])

index = 13
print(index % 2 == 0, not index % 2)

for index, symbol in enumerate(my_str):  # enumerate return index and value by this index
    print(index, symbol)


#####################################################
# a little practice:

input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n: ")

if input_case in "1234":
    try:
        value_1 = float(input("Ведите первое число:"))
        value_2 = float(input("Ведите второе число:"))
        if input_case == "1":
            result = value_1 + value_2
            sign = '+'
        elif input_case == "2":
            result = value_1 - value_2
            sign = '-'
        elif input_case == "3":
            result = value_1 * value_2
            sign = '*'
        else:
            result = value_1 / value_2
            sign = '/'
        print(f'{value_1} {sign} {value_2} = {result}')
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except ValueError:
        print("Это не число")
else:
    print("Вы не выбрали операцию")

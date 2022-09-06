# Fourth lesson: knowledge of the function input(), errors handling, short hand if...else, while loops, string methods,
# slicing strings, is... methods

#####################################################
# input() function:

value = input("Print an integer: ")
try:
    value = int(value)
    result = 1 / value
    print(value, result)
except (ValueError, TypeError):
    print("It's not integer!!!")
except ZeroDivisionError:
    print("You can't divide by zero!!!")

#####################################################
# short hand if...else:

value = -12
if value >= 0:
    result = value
else:
    result = value * 2
print(result)

# new_variable = value_if_true if condition else value_if_false
result = value if value >= 0 else value * 2
print(result)

#####################################################
# while loops:

# normal solution
value = 10
while value >= 0:
    print(value)
    value -= 1

# bad solution
while True:
    print(value)
    value -= 1
    if value < 0:
        break

# solution for a specific problem
do_while = True
while do_while:
    print(value)
    value -= 1
    if value < 0:
        do_while = False

#####################################################
# string methods:

my_str = "qwerty"
# index = 0  # first index
index = -1  # last index
symbol = my_str[index]  # getting value by index
print(symbol)

if index < len(my_str):
    symbol = my_str[index]  # getting value by index
    print(symbol)

symbol_count = len(my_str)
print(symbol_count)

my_str[0] = "Q"  # TypeError: 'str' object does not support item assignment

#####################################################
# slicing strings:

my_str = "qwerty"
new_str = my_str[1:5]  # "wert"
new_str = my_str[3:]  # "rty"
new_str = my_str[:-3]  # "qwe"
new_str = my_str[:]  # "qwerty", string copy
new_str = my_str[-40:20]  # None
print(new_str)

new_str = "Q" + my_str[1:]  # "Qwerty"
new_str = my_str[:3] + "R" + my_str[4:]  # "qweRty"
print(new_str)

new_str = my_str[::2]  # 2 - slicing step. Values at even indices
new_str = my_str[1::2]  # 2 - slicing step. Values at odd indices
new_str = my_str[::-1]  # string reverse
print(new_str)

#####################################################
# is... methods:

my_str = "asD"
if my_str[-1].isupper():
    print(f"The last characters is uppercase in {my_str}")

my_str = "teremok"
if my_str.islower():
    print(f"All of string characters is lowercase in {my_str}")

my_str = "42"
if my_str.isdigit():
    print(f"All of string characters is digit in {my_str}")

my_str = "ASdsafasgds"
if my_str.isalpha():
    print(f"All of string characters is letters in {my_str}")

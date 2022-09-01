# Second lesson: knowledge of comments, data types, arithmetic operators, assignment operators, basic PEP-8 knowledge,
# naming styles, concatenation escape characters, string literals, f-string and r-string

# Ctrl + ? (Mac: Command + ?) for comment

# Data types:
# type_1 = "Hello World"  # str
# type_2 = 20 # int
# type_3 = 20.5   # float
# type_4 = 1j	# complex
# type_5 = ["apple", "banana", "cherry"]	# list
# type_6 = ("apple", "banana", "cherry")	# tuple
# type_7 = range(6)	range
# type_8 = {"name" : "John", "age" : 36}	# dict
# type_9 = {"apple", "banana", "cherry"}	# set
# type_10 = frozenset({"apple", "banana", "cherry"})	# frozenset
# type_11 = True	# bool
# type_12 = b"Hello"	# bytes
# type_13 = bytearray(5)	# bytearray
# type_14 = memoryview(bytes(5))	# memoryview
# type_15 = None	# NoneType


# Arithmetic operators:
# result = value_1 + value_2  # sum
# result = value_1 - value_2  # difference
# result = value_1 * value_2  # multiplication
# result = value_1 / value_2  # division
# result = value_1 % value_2  # remainder of the division
# result = value_1 ** value_2 # exponentiation
# result = value_1 // value_2  # integer division


# Assignment operators:
# Operator:	 Example:	Same As:
#     =	      x = 5	     x = 5
#     +=	  x += 3	 x = x + 3
#     -       x -= 3	 x = x - 3
#     *=      x *= 3	 x = x * 3
#     /=      x /= 3	 x = x / 3
#     %=      x %= 3	 x = x % 3
#     //      x //= 3	 x = x // 3
#     **=     x **= 3	 x = x ** 3

# PEP-8 formatting Alt+Ctrl+L (Mac Option+Command+L)

# snake_case_object_notification - In Python for variables, functions, etc.
# PascalCaseObjectNotification - In Python for classes
# camelCaseObjectNotification
# cebab-object-notification

# Some examples with types and operator:
active_users_count = 1000
price = 10
total_money = active_users_count * price
RATIO = 100
print(total_money, RATIO)

value_type = type(total_money)
print(total_money, value_type)

value = 123123123
new_value = 123123123
print(id(value), id(new_value))

value = "qQwWe"
my_str = "zxc"
print(value, type(value))

result = value + "__" + value  # concatenation

result = ("123" + "5") * 2
print(result)

# Escape characters:
# \'	    "Double Quotes"
# \'	    "Single Quote"
# \\	    "Backslash"
# \n	    "New Line"
# \r	    "Carriage Return"
# \t	    "Tab"
# \b	    "Backspace"
# \f	    "Form Feed"
# \ooo	    "Octal value"
# \xhh      "Hex value"

# String literals:
# ""                "Double Quotes"
# ''                "Single Quote"
# """""" or ''''''  "Multi-line String"

# Some examples with string literals:
my_str = "New string"
my_str = 'New string'
my_str = """New 
string"""
my_str = '''New_string'''

my_str = 'FC "Arsenal"'
my_str = "I'm a boy"

my_str = 'My\tname\'is\nVova'
new_str = r'My\tname\tis\nVova'  # r (raw) string
format_str = f"{value = }"  # f (format) string
print(my_str)
print(new_str)
print(format_str)

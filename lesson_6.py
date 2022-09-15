# Sixth lesson: knowledge of lists, tuples, list methods, list and tuple indexing, tuple() and list() functions,
# split and strip string methods, list and tuple slicing


#####################################################
# tuple and list:

# Tuple:
my_tuple = (1, 2, 3, "qwe", True, ("a", "b"), None, [])  #items are ordered, unchangeable, and allow duplicate values.
# print(type(my_tuple), my_tuple)

# List:
my_list = [1, 2, 3, "qwe", True, ("a", "b"), None, []]  #items are ordered, changeable, and allow duplicate values.
# print(type(my_list), my_list)

#####################################################
# change list which contained in tuple by list methods:

my_tuple[-1].append(1)
my_tuple[-1].extend([2, 3.14])
my_tuple[-1].pop()
print(my_tuple)

#####################################################
# interesting case:

my_list = []
new_list = [my_list.copy()] * 3
print(new_list)

my_list.append(1)  # changing item in my_list
print(new_list, my_list)

new_list[0].append(2)  # changing all items in new_list
print(new_list)

#####################################################
# How to do this case:

my_list = []
new_list = [my_list.copy()] * 3
print(new_list)

my_list.append(1)  # changing item in my_list
print(new_list, my_list)

first_item = new_list[0].copy()  # add new var for new_list[0] copy: []
first_item.append(2)  # [] -> [2]
new_list.pop(0)  # new_list:  [[], []]
new_list.insert(0, first_item)  # [[], []] -> [[2], [], []]
print(new_list)

#####################################################
# list and tuple indexing:

my_list[0] = 100
print(my_list)

# my_tuple[0] = 100  # TypeError
print(my_tuple)

#####################################################
# tuple() and list() functions:

new_values = tuple(my_list)
new_values = list(my_tuple)
print(new_values, type(new_values))

new_values = list(my_tuple)
new_values[0] = 100
my_tuple = tuple(new_values)
print(my_tuple)

#####################################################
# some list practice:

new_list = []
# new_list = list()
# print(new_list)

for number in range(1, 11):
    new_list.append(number)

new_list.append("qwe")  # O(1)
new_list.insert(0, "asd")  # O(n)
print(new_list)

value = new_list.pop()  # O(1)
new_list.pop(0)  # O(n)
print(value, new_list)

# Value returning - pop return deleted value
#####################################################
# cases in which the id changes and in which it doesn't:

result = my_list[:2] + my_list[5:]
print(result)

items_1 = [1, 2, 3, "a"]
items_2 = ["q", "w", "e"]

result = []
print(result, id(result))

result = items_1 + items_2  # changes id

result.extend(items_1)  # doesn't change id
result.extend(items_2)  # doesn't change id
print(result, id(result))

result += items_1  # doesn't change id
result += items_2  # doesn't change id
print(result, id(result))

#####################################################
# split and strip string methods:

message = "My name is   \t   Volodymyr"
words = message.split()
print(words)

ip_address = "127.255.12.0"
groups = ip_address.split(".")
print(groups)

filename = "/home/volodymyr/PycharmProjects/IntroPython_25_08_22/"
path = filename.strip("/").split("/")
print(path)

new_message = " ".join(words)
print(new_message)

new_filename = "C:\\\\" + "\\".join(path)

print(new_filename)

#####################################################
# list and tuple slicing:

print(len(my_list), len(my_tuple))

index = 5
value = my_tuple[-1]
value = my_list[index]
print(value)

start = 1
finish = 3
values = my_list[start:finish]
values = my_tuple[::-1]
print(values)

for value in my_list[::-1]:
    print(value)

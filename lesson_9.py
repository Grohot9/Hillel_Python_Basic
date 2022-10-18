# функции
import random
from typing import List

DEBUG_MODE = True


# A(1; 2; -3)

# point_a = (1, 2, -3)
# print(point_a)
# print(point_a[0])

################ базовый синтаксис функции
def print_hello_world():  # описание (декларация) функции
    print("Hello, World!")


print_hello_world()  # вызов функции
#######################

def create_point_with_random_values(min_value, max_value):
    point = {"x": random.randint(min_value, max_value),
             "y": random.randint(min_value, max_value),
             "z": random.randint(min_value, max_value)}
    return point


def create_triangle(name, min_value=-10, max_value=10, debug_mode=DEBUG_MODE):
    triangle = {}
    for letter in name:
        triangle[letter] = create_point_with_random_values(min_value, max_value)
    if debug_mode:
        for key in triangle:
            print(f"{key}: {triangle[key]}")
    return triangle


min_limit = -50
max_limit = 50

min_value = -100
max_value = 100

# DRY
point_a = create_point_with_random_values(min_limit, max_limit)
point_b = create_point_with_random_values(min_limit, max_limit)
point_c = create_point_with_random_values(-10, 10)

print(point_a)
print(point_b)
print(point_c)

# triangle_one = create_triangle()
# print(triangle_one)
# triangle_two = create_triangle(max_value=10, min_value=0)
# triangle_two = create_triangle(max_value=max_limit, min_value=min_limit)
# triangle_two = create_triangle(min_value=min_value, max_value=max_value)
# print(triangle_two)

triangle = create_triangle("QWE", -100, 100, True)
print(triangle)

##########################################

def combine_two_lists(list_1: List[int], list_2: List[int]) -> List[int]:
    my_result = []
    index_count = min(len(list_1), len(list_2))
    for index in range(index_count):
        my_result.append(list_1[index])
        my_result.append(list_2[index])
    return my_result + list_1[index_count:] + list_2[index_count:]


my_list_1 = [1, 2, 3, 4, 5, 6, 7]
my_list_2 = [10, 20, 30, 40]

my_result = combine_two_lists(my_list_1, my_list_2)
print(my_result)
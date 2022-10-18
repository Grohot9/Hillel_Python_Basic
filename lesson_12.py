# CLI (command-line interface)
from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("name", type=str)
args.add_argument("--age", type=int, nargs='?', default=0)
args.add_argument("--job", type=str, nargs='?', default='')

args = vars(args.parse_args())
print(args)

name = args['name']
age = args['age'] * 2

print(f"Hello {name}! Age: {age}")

# Results:
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John
# {'name': 'John'}
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John
# {'NAME': 'John'}
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py
# usage: lesson_12.py [-h] name
# lesson_12.py: error: the following arguments are required: name
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John
# {'name': 'John', 'age': 0}
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John 45
# {'name': 'John', 'age': 45}
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John 45
# {'name': 'John', 'age': 45}
# Hello John! Age: 90
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John --job programmer --age 45
# {'name': 'John', 'age': 45, 'job': 'programmer'}
# Hello John! Age: 90
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John --job programmer --age 45
# usage: lesson_12.py [-h] name [age] [job]
# lesson_12.py: error: unrecognized arguments: --job programmer --age 45
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John --job programmer
# {'name': 'John', 'age': 0, 'job': 'programmer'}
# Hello John! Age: 0
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John 45 programmer
# usage: lesson_12.py [-h] [--age [AGE]] [--job [JOB]] name
# lesson_12.py: error: unrecognized arguments: 45 programmer
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John --age 45 programmer
# usage: lesson_12.py [-h] [--age [AGE]] [--job [JOB]] name
# lesson_12.py: error: unrecognized arguments: programmer
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John --age 45 --job=programmer
# {'name': 'John', 'age': 45, 'job': 'programmer'}
# Hello John! Age: 90
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John --age=45 --job=programmer
# {'name': 'John', 'age': 45, 'job': 'programmer'}
# Hello John! Age: 90
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 %
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John --age=45a --job='programmer asd'
# usage: lesson_12.py [-h] [--age [AGE]] [--job [JOB]] name
# lesson_12.py: error: argument --age: invalid int value: '45a'
# (IntroPython_25_08_22) volodymyrzontov@VolodymyrZ IntroPython_25_08_22 % python lesson_12.py John --age=45 --job='programmer asd'

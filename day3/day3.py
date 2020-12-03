input_file = open('day3.txt', 'r')
next(input_file)
lines = input_file.readlines()

index = 0
num_trees = 0
result = 0
for line in lines:
    index += 1
    if index > 30:
        index -= 31
    if line[index] == '#':
        print("tree")
        num_trees += 1
print(f"num_trees: {num_trees}")
result = num_trees

input_file = open('day3.txt', 'r')
next(input_file)
lines = input_file.readlines()

index = 0
num_trees = 0
for line in lines:
    index += 3
    if index > 30:
        index -= 31
    if line[index] == '#':
        print("tree")
        num_trees += 1
print(f"num_trees: {num_trees}")
result *= num_trees

input_file = open('day3.txt', 'r')
next(input_file)
lines = input_file.readlines()

index = 0
num_trees = 0
for line in lines:
    index += 5
    if index > 30:
        index -= 31
    if line[index] == '#':
        print("tree")
        num_trees += 1
print(f"num_trees: {num_trees}")
result *= num_trees

input_file = open('day3.txt', 'r')
next(input_file)
lines = input_file.readlines()

index = 0
num_trees = 0
for line in lines:
    index += 7
    if index > 30:
        index -= 31\
    if line[index] == '#':
        print("tree")
        num_trees += 1
print(f"num_trees: {num_trees}")
result *= num_trees

input_file = open('day3.txt', 'r')
next(input_file)
next(input_file)
lines = input_file.readlines()

index = 0
num_trees = 0
for i, line in enumerate(lines):
    if i % 2 == 1:
        continue
    index += 1
    if index > 30:
        index -= 31
    if line[index] == '#':
        print("tree")
        num_trees += 1
print(f"num_trees: {num_trees}")
result *= num_trees
print(f"result: {result}")

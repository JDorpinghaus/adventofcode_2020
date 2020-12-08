import sys

input_file = open('day8.txt', 'r')
lines = input_file.readlines()

def run_commands(input_lines, stop_at_first_double):
    length = len(input_lines)
    num_instructions = 0
    index = 0
    accumulator = 0
    commands = {}
    first_double = True
    while True:
        if index >= length:
            print(f"Terminated successfully! Accumulator = {accumulator}")
            sys.exit(0)
        elif num_instructions > 10000:
            break
        else:
            num_instructions += 1
        if str(index) in commands:
            if stop_at_first_double:
                print(f"First double instruction, accumulator = {accumulator}")
                break
            commands[str(index)] += 1
        else:
            commands[str(index)] = 1
        current_line = input_lines[index]
        tokens = current_line.strip().split(' ')
        command = tokens[0]
        value = int(tokens[1])
        if command == 'acc':
            accumulator += value
            index += 1
        elif command == 'jmp':
            index += value
        else:
            index += 1

accumulator = 0
index = 0
run_commands(lines, True)

accumulator = 0
index = 0
for index, line in enumerate(lines):
    new_lines = lines.copy()
    tokens = line.strip().split(' ')
    command = tokens[0]
    value = tokens[1]
    if command == 'jmp':
        new_line = f"nop {value}\n"
        new_lines[index] = new_line
        run_commands(new_lines, False)

accumulator = 0
index = 0
for index, line in enumerate(lines):
    new_lines = lines.copy()
    tokens = line.strip().split(' ')
    command = tokens[0]
    value = tokens[1]
    if command == 'nop':
        new_line = f"jmp {value}\n"
        new_lines[index] = new_line
        run_commands(new_lines, False)






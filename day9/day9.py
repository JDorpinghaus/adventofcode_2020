import sys

input_file = open('day9.txt', 'r')
lines = input_file.readlines()
invalid_number = 0

### Part 1 ###
for index, line in enumerate(lines):
    if index < 25:
        continue
    next_num = int(line.strip())
    window = lines[(index-25):index].copy()
    window_2 = window.copy()
    match = False
    for num in window:
        for other_num in window_2:
            if int(num.strip()) + int(other_num.strip()) == next_num:
                match = True
    if not match:
        invalid_number = next_num
        print(f"Invalid number: {invalid_number}")

### Part 2 ###
window_size = 2
while True:
    for index, line in enumerate(lines):
        if index < window_size-1:
            continue
        if index > len(lines):
            break
        num = int(line.strip())
        window = lines[(index-window_size):index].copy()
        acc = 0
        window2 = []
        for w in window:
            acc += int(w.strip())
            window2.append(int(w.strip()))
        if acc == invalid_number:
            print(f"Sum: {min(window2) + max(window2)}")
            sys.exit(0)
    window_size += 1





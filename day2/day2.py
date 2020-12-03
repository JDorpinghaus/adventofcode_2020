input_file = open('day2.txt', 'r')
lines = input_file.readlines()
valid_passwords_1 = 0
valid_passwords_2 = 0

for line in lines:
    split1 = line.split(':')
    password = split1[1].strip()
    split2 = split1[0].split(' ')
    character = split2[1]
    split3 = split2[0].split('-')
    min_num = int(split3[0])
    max_num = int(split3[1])
    #print(f"password = {password}, min_num={min_num}, max_num={max_num}, character = {character}")

    character_count = password.count(character)
    if character_count >= min_num and character_count <= max_num:
        valid_passwords_1 += 1

    valid_1 = password[min_num - 1] == character
    valid_2 = password[max_num - 1] == character
    if (valid_1 and not valid_2) or (valid_2 and not valid_1):
        valid_passwords_2 += 1

print(f"Valid passwords 1: {valid_passwords_1}")
print(f"Valid passwords 2: {valid_passwords_2}")

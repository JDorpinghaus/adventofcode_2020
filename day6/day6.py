input_file = open('day6.txt', 'r')
lines = input_file.readlines()

total_1 = 0
total_2 = 0
people = 0
num_answers = {}
answers = ""

for line in lines:
    if line.strip() == '':
        total_1 += len(set(answers))
        for answer, answer_count in num_answers.items():
            if answer_count == people:
                total_2 += 1
        answers = ""
        people = 0
        num_answers = {}
    else:
        answers += line.strip()
        people += 1
        for answer in line.strip():
            if answer in num_answers:
                num_answers[answer] += 1
            else:
                num_answers[answer] = 1

print(f"total_1: {total_1}")
print(f"total_2: {total_2}")


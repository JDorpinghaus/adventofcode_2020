input_file = open('day5.txt', 'r')
lines = input_file.readlines()

max_id = 0
ids = []
for line in lines:
    row = int(line[0:7].replace('F', '0').replace('B', '1'), 2)
    column = int(line[7:10].replace('L', '0').replace('R', '1'), 2)
    id = (row * 8) + column
    ids.append(id)
    if id > max_id:
        max_id = id
ids.sort()
for index, id in enumerate(ids):
    if id + 1 != ids[index + 1]:
        print(f"your seat: {id + 1}")
        break
print(f"max id: {max_id}")
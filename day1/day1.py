input_file = open('day_1.txt', 'r')
lines = input_file.readlines()

for index, line in enumerate(lines):
    addend_1 = int(line)
    line_range_1 = range(index, len(lines))
    for index_2 in line_range_1:
        addend_2 = int(lines[index_2])
        sum_1 = addend_1 + addend_2
        if sum_1 == 2020:
            product_1 = addend_1 * addend_2
            print(f"a1: {addend_1}, a2: {addend_2}, Result: {product_1}")
        line_range_2 = range(index_2, len(lines))
        for index_3 in line_range_2:
            addend_3 = int(lines[index_3])
            sum_2 = sum_1 + addend_3
            if sum_2 == 2020:
                product_2 = addend_1 * addend_2 * addend_3
                print(f"a1: {addend_1}, a2: {addend_2}, a3: {addend_3}, Result: {product_2}")

input_file = open('day7.txt', 'r')
lines = input_file.readlines()

def can_hold_gold(bag_name):
    if bag_name == 'shiny gold':
        return True
    else:
        if bag_name in holds:
            held_bags = holds[bag_name]
            for held_bag in held_bags:
                if can_hold_gold(held_bag['name']) == True:
                    return True
            return False
        else:
            return False

def num_bags_contained(bag_name):
    total_held = 0
    if bag_name in holds:
        held_bags = holds[bag_name]
        for held_bag in held_bags:
            if held_bag['name'] == 'none':
                return 0
            else:
                total_held += int(held_bag['quantity']) * (num_bags_contained(held_bag['name']) + 1)
        return total_held
    else:
        return 0

holds = {}
bags = []

for line in lines:
    tokens = line.strip().split('contain')
    current_bag = ' '.join(tokens[0].split(' ')[0:2])
    for item in tokens[1].strip().split(','):
        tok = item.strip().split(' ')
        quantity = tok[0]
        bag = ' '.join(tok[1:3]).strip()
        if bag != 'other bags.':
            if bag != 'shiny gold':
                bags.append(bag)
            bag_item = {"name": bag, "quantity": quantity}
            if current_bag in holds:
                holds[current_bag].append(bag_item)
            else:
                holds[current_bag] = [bag_item]
    if current_bag != 'shiny gold':
        bags.append(current_bag)

total_gold_holding_bags = 0
for bag in set(bags):
    if can_hold_gold(bag):
        total_gold_holding_bags += 1
print(f"Total bags that can hold gold: {total_gold_holding_bags}")

num_bags = num_bags_contained('shiny gold')
print(f"Number of bags contained within a shiny gold bag: {num_bags}")
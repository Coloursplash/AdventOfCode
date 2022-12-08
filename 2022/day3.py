with open("day3.txt", "r") as file:
    raw_data = file.read()

# part a

rucksacks = []

for line in raw_data.split("\n"):
    median = len(line) // 2
    rucksacks.append([line[:median], line[median:]])

priority_sum = 0

for rucksack in rucksacks:
    repeats = []
    for item in rucksack[0]:
        if item in rucksack[1] and item not in repeats:
            repeats.append(item)
            priority = ord(item.lower()) - 96
            if item.isupper():
                priority += 26
            priority_sum += priority

print("Priority sum is", priority_sum)

# part b

groups = [[]]

for rucksack in rucksacks:
    if len(groups[-1]) == 3:
        groups.append([])
    groups[-1].append(rucksack[0] + rucksack[1])

priority_sum = 0

for group in groups:
    for item in min(group, key=len):
        if item in group[0] and item in group[1] and item in group[2]:
            priority = ord(item.lower()) - 96
            if item.isupper():
                priority += 26
            priority_sum += priority
            break

print("Priority sum of badges is", priority_sum)

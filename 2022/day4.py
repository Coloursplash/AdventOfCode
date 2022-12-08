def contains(range_a, range_b):
    if range_a[0] <= range_b[0]:
        if range_a[1] >= range_b[1]:
            return True
    elif range_a[0] >= range_b[0]:
        if range_a[1] <= range_b[1]:
            return True
    return False


with open("day4.txt", "r") as file:
    raw_data = file.read()

pairs = []

for line in raw_data.split("\n"):
    pair = line.split(",")
    l1 = pair[0].split("-")
    l2 = pair[1].split("-")
    pairs.append([[int(x) for x in l1], [int(y) for y in l2]])

# part a
repeated_pairs = 0

for pair in pairs:
    if contains(pair[0], pair[1]):
        repeated_pairs += 1

print(repeated_pairs)

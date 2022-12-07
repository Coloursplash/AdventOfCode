with open("day1.txt", "r") as file:
    raw_data = file.read()

elves = [0]

for num in raw_data.split('\n'):
    if num == "":
        elves.append(0)
    else:
        elves[-1] += int(num)

elves.sort()

#part 1
print("Maximum calorie elf is elf", len(elves))
print("Elf is carrying", elves[-1], "calories")

# part 2
print("Top three are carrying", elves[-1] + elves[-2] + elves[-3], "calories")

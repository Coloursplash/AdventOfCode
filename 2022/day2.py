def char_to_move(letter):
    if letter in ["A", "X"]:
        return "ROCK"
    if letter in ["B", "Y"]:
        return "PAPER"
    return "SCISSORS"


with open("day2.txt", "r") as file:
    raw_data = file.read()

# part a

rounds = []

for line in raw_data.split("\n"):
    rounds.append([char_to_move(line[0]), char_to_move(line[2])])

score = 0

for enemy, move in rounds:
    if move == "ROCK":
        if enemy == "ROCK":
            score += 3
        elif enemy == "SCISSORS":
            score += 6
        score += 1
    elif move == "PAPER":
        if enemy == "PAPER":
            score += 3
        elif enemy == "ROCK":
            score += 6
        score += 2
    elif move == "SCISSORS":
        if enemy == "SCISSORS":
            score += 3
        elif enemy == "PAPER":
            score += 6
        score += 3

print("Score is", score)

# part b
rounds = []

for line in raw_data.split("\n"):
    rounds.append([char_to_move(line[0]), line[2]])

score = 0

for enemy, outcome in rounds:
    if outcome == "Y":
        if enemy == "ROCK":
            score += 1
        elif enemy == "PAPER":
            score += 2
        else:
            score += 3
        score += 3
    elif outcome == "Z":
        if enemy == "ROCK":
            score += 2
        elif enemy == "PAPER":
            score += 3
        else:
            score += 1
        score += 6
    else:
        if enemy == "ROCK":
            score += 3
        elif enemy == "PAPER":
            score += 1
        else:
            score += 2

print("Score is", score)
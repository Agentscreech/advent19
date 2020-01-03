with open("inputs/day1.txt", "r") as f:
    total = 0
    for line in f:
        total += (int(line)//3) - 2
    print(total)
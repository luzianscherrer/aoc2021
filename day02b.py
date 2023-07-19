f = open("day02input.txt", "r")

horizontal = 0
depth = 0
aim = 0

for line in f.read().split("\n"):
    instruction, value = line.split(" ")
    value = int(value)
    match instruction:
        case "forward":
            horizontal += value
            depth += aim * value
        case "down":
            aim += value
        case "up":
            aim -= value

print(horizontal*depth)

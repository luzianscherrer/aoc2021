f = open("day02input.txt", "r")

horizontal = 0
depth = 0

for line in f.read().split("\n"):
    instruction, value = line.split(" ")
    value = int(value)
    match instruction:
        case "forward":
            horizontal += value
        case "down":
            depth += value
        case "up":
            depth -= value

print(horizontal*depth)

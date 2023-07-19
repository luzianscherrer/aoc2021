import sys

f = open("day01input.txt", "r")

total = 0
prev = sys.maxsize
for line in f.read().split("\n"):
    if int(line) > prev:
        total += 1
    prev = int(line)
print(total)

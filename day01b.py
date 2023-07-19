import sys
from functools import reduce

f = open("day01input.txt", "r")
window_size = 3

total = 0
prev = sys.maxsize
input = f.read().split("\n")
for i in range(0, len(input)-window_size+1):
    cur = reduce(lambda a, b: int(a)+int(b), input[i:i+window_size])
    if cur > prev:
        total += 1
    prev = cur 
print(total)

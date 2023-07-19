f = open("day03input.txt", "r")

steps = 0
sum = [0 for _ in range(100)]
for line in f.read().split("\n"):
    arr = [int(_) for _ in line]
    sum = list(map(lambda x, y: x+y, arr, sum))
    steps += 1

gamma = 0
epsilon = 0
res = list(map(lambda x: x>steps/2, sum))
for i, bit in enumerate(reversed(res)):
    if bit == True:
        gamma += 2**i
    else:
        epsilon += 2**i

print(gamma*epsilon)
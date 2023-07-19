from functools import reduce

SLOTS = 9
EXTRA_DAYS = 2
ROUNDS = 256

def main():
    f = open("day06input.txt", "r")
    fishes = [0]*SLOTS
    for index in list(map(int, f.readline().split(","))):
        fishes[index] += 1

    for _ in range(ROUNDS):
        first = fishes[0]
        del fishes[0]
        fishes[SLOTS-EXTRA_DAYS-1] += first
        fishes.append(first)
    print(reduce(lambda a, b : a+b, fishes))
    
if __name__ == "__main__":
    main()
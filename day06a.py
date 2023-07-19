START_REGULAR = 6
START_NEW = 8
ROUNDS = 80

def main():
    f = open("day06input.txt", "r")
    fishes = list(map(int, f.readline().split(",")))

    for _ in range(ROUNDS):
        fishes = list(map(lambda a : a-1, fishes))
        count = len(list(filter(lambda a: a < 0, fishes)));
        for _ in range(count):
            fishes.append(START_NEW)
        fishes = list(map(lambda a : START_REGULAR if a < 0 else a, fishes))
    print(len(fishes))
    
if __name__ == "__main__":
    main()
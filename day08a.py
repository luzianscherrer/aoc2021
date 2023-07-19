def main():
    input = open("day08input.txt", "r").read().split("\n")
    total = 0
    for line in input:
        total += len(list(filter(lambda a : len(a) in [2,4,3,7], line.split(" | ")[1].split(" "))))
    print(total)

if __name__ == "__main__":
    main()
def process(polymer, insertions):
    newpolymer = ""
    for i in range(len(polymer) - 1):
        newpolymer += polymer[i] + insertions[polymer[i] + polymer[i + 1]]
    newpolymer += polymer[-1]
    return newpolymer


def main():
    insertions = {}

    input = open("day14input.txt", "r").read().split("\n")
    for line in input:
        if "->" in line:
            pair, insert = line.split(" -> ")
            insertions[pair] = insert
        elif len(line) != 0:
            polymer = line

    for i in range(10):
        polymer = process(polymer, insertions)

    max = 0
    min = 2**31
    count = 1
    prev = ""
    for char in sorted(polymer):
        if char == prev:
            count += 1
        elif count != 1:
            if count > max:
                max = count
            if count < min:
                min = count
            count = 1
        prev = char

    print(max - min)


if __name__ == "__main__":
    main()

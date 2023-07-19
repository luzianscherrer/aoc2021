def main():
    insertions = {}
    totals = {}
    occurences = {}

    input = open("day14input.txt", "r").read().split("\n")
    for line in input:
        if "->" in line:
            pair, insert = line.split(" -> ")
            insertions[pair] = insert
        elif len(line) != 0:
            occurences[line[0]] = 1
            for i in range(len(line) - 1):
                totals[line[i] + line[i + 1]] = 1

    for i in range(40):
        newtotals = {}
        for key in totals.keys():
            middle = insertions[key[0] + key[1]]
            if key[0] + middle in newtotals:
                newtotals[key[0] + middle] += totals[key]
            else:
                newtotals[key[0] + middle] = totals[key]
            if middle + key[1] in newtotals:
                newtotals[middle + key[1]] += totals[key]
            else:
                newtotals[middle + key[1]] = totals[key]
        totals = newtotals

    for key in totals.keys():
        if key[1] in occurences:
            occurences[key[1]] += totals[key]
        else:
            occurences[key[1]] = totals[key]

    max = 0
    min = 2**63
    for key in occurences.keys():
        if occurences[key] > max:
            max = occurences[key]
        if occurences[key] < min:
            min = occurences[key]
    print(max - min)


if __name__ == "__main__":
    main()

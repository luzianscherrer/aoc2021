def expand_field(field, count, char):
    for _ in range(count):
        field.insert(0, list(char * len(field[0])))
        field.append(list(char * len(field[0])))
    for line in field:
        for _ in range(count):
            line.insert(0, char)
        line += char * count


def shrink_field(field):
    del field[0]
    del field[-1]
    for row in field:
        del row[0]
        del row[-1]


def create_field(width, height):
    return [["." for _ in range(width)] for _ in range(height)]


def print_field(field):
    for y in range(len(field)):
        for x in range(len(field[y])):
            print(field[y][x], end="")
        print()
    print()


def value(field, y, x):
    res = ""
    res += field[y - 1][x - 1]
    res += field[y - 1][x]
    res += field[y - 1][x + 1]
    res += field[y][x - 1]
    res += field[y][x]
    res += field[y][x + 1]
    res += field[y + 1][x - 1]
    res += field[y + 1][x]
    res += field[y + 1][x + 1]
    res = res.replace(".", "0")
    res = res.replace("#", "1")
    return int(res, 2)


def main():
    input = open("day20input.txt", "r").read().split("\n")
    lookup = input[0]
    field = []
    for i in range(2, len(input)):
        field.append(list(input[i]))

    expansion = 3
    for i in range(2):
        expand_field(field, expansion, "." if i % 2 == 0 else "#")
        new_field = create_field(len(field[0]), len(field))
        for y in range(1, len(field) - 1):
            for x in range(1, len(field[0]) - 1):
                val = value(field, y, x)
                new_field[y][x] = lookup[val]

        shrink_field(new_field)
        field = new_field

    print_field(field)
    print(len(list(filter(lambda a: a == "#", [i for s in field for i in s]))))


# This solution only works for the real input where
# lookup[0] is "." and lookup[-1] is "#".
if __name__ == "__main__":
    main()

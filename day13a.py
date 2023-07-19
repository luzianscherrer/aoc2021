def print_field(field):
    for y in range(len(field)):
        for x in range(len(field[0])):
            print(field[y][x], end="")
        print()
    print()


def fold(field, axis, value):
    if axis == "y":
        upper = value - 1
        lower = value + 1
        while True:
            if upper < 0 or lower >= len(field):
                break
            for x in range(len(field[0])):
                if field[lower][x] == "#":
                    field[upper][x] = field[lower][x]
            upper -= 1
            lower += 1
        return field[:value]
    elif axis == "x":
        left = value - 1
        right = value + 1
        while True:
            if left < 0 or right >= len(field[0]):
                break
            for y in range(len(field)):
                if field[y][right] == "#":
                    field[y][left] = field[y][right]
            left -= 1
            right += 1
        return [row[:value] for row in field]


def main():
    width = 0
    height = 0
    coords = []
    folds = []
    input = open("day13input.txt", "r").read().split("\n")
    for line in input:
        if "," in line:
            x, y = line.split(",")
            x = int(x)
            y = int(y)
            coords.append([x, y])
            if x + 1 > width:
                width = x + 1
            if y + 1 > height:
                height = y + 1
        elif "=" in line:
            axis, value = line.split(" ")[2].split("=")
            folds.append([axis, int(value)])

    field = [["." for _ in range(width)] for _ in range(height)]
    for coord in coords:
        field[coord[1]][coord[0]] = "#"

    for f in folds:
        field = fold(field, f[0], f[1])
        break

    print(
        len(
            list(
                filter(lambda a: a == "#", [point for list in field for point in list])
            )
        )
    )


if __name__ == "__main__":
    main()

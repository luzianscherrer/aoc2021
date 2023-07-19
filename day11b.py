def print_field(field):
    for y in range(len(field)):
        for x in range(len(field[0])):
            print(f"{field[y][x]:>3}", end="")
        print()
    print()


def incr_neighbours(field, x, y):
    if y > 0 and field[y - 1][x] not in (10, 11):
        field[y - 1][x] += 1
    if y > 0 and x < len(field[0]) - 1 and field[y - 1][x + 1] not in (10, 11):
        field[y - 1][x + 1] += 1
    if x < len(field[0]) - 1 and field[y][x + 1] not in (10, 11):
        field[y][x + 1] += 1
    if (
        y < len(field) - 1
        and x < len(field[0]) - 1
        and field[y + 1][x + 1] not in (10, 11)
    ):
        field[y + 1][x + 1] += 1
    if y < len(field) - 1 and field[y + 1][x] not in (10, 11):
        field[y + 1][x] += 1
    if y < len(field) - 1 and x > 0 and field[y + 1][x - 1] not in (10, 11):
        field[y + 1][x - 1] += 1
    if x > 0 and field[y][x - 1] not in (10, 11):
        field[y][x - 1] += 1
    if y > 0 and x > 0 and field[y - 1][x - 1] not in (10, 11):
        field[y - 1][x - 1] += 1


def flash_field(field):
    more_work = False
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == 10:
                more_work = True
                incr_neighbours(field, x, y)
                field[y][x] = 11
    if more_work:
        flash_field(field)


def main():
    input = open("day11input.txt", "r").read().split("\n")
    field = []
    for line in input:
        field.append(list(map(int, line)))

    step = 0
    while True:
        step += 1
        field = [list(map(lambda a: a + 1, line)) for line in field]
        flash_field(field)
        flashes = 0
        for line in field:
            flashes += len(list(filter(lambda a: a == 11, line)))
        if flashes == len(field) * len(field[0]):
            break
        field = [list(map(lambda a: 0 if a == 11 else a, line)) for line in field]
        # print(f"after step {i+1} ({flashes} flashes):")
        # print_field(field)
    print(step)


if __name__ == "__main__":
    main()

import heapq


def main():
    input = open("day15input.txt", "r").read().split("\n")
    field = []
    visited = []
    costs = {(0, 0): 0}
    for i in range(5):
        for line in input:
            row = []
            for j in range(0, 5):
                summand = i + j
                part = [int(number) + summand for number in line]
                row += list(map(lambda a: a if a < 10 else a - 9, part))
            field.append(row)

    # for y in range(len(field)):
    #     for x in range(len(field[0])):
    #         print(f"{field[y][x]} ", end="")
    #     print()

    heap = []
    heapq.heappush(heap, (0, (0, 0)))

    while len(heap):
        cost, (x, y) = heapq.heappop(heap)
        visited.append((x, y))

        neighbours = []
        if y > 0 and (x, y - 1) not in visited:
            neighbours.append((x, y - 1))
        if y < len(field) - 1 and (x, y + 1) not in visited:
            neighbours.append((x, y + 1))
        if x > 0 and (x - 1, y) not in visited:
            neighbours.append((x - 1, y))
        if x < len(field[0]) - 1 and (x + 1, y) not in visited:
            neighbours.append((x + 1, y))

        if costs[(x, y)] < cost:
            continue

        for neighbour in neighbours:
            nextcost = costs[(x, y)] + field[neighbour[1]][neighbour[0]]
            if neighbour not in costs or nextcost < costs[neighbour]:
                costs[neighbour] = nextcost
                heapq.heappush(heap, (nextcost, neighbour))

    print(costs[(len(field) - 1, len(field[0]) - 1)])


# Beware, runtime is around 2 hours.
if __name__ == "__main__":
    main()

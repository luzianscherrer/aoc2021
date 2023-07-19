class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}/{self.y}"

    def __repr__(self):
        return self.__str__()


class Amphipod:
    def __init__(self, type, position):
        self.type = type
        if type == "A":
            self.cost = 1
        elif type == "B":
            self.cost = 10
        elif type == "C":
            self.cost = 100
        elif type == "D":
            self.cost = 1000
        self.position = position

    def __str__(self):
        return f"{self.type}@{self.position}"

    def __repr__(self):
        return self.__str__()


def getmoves(amphipod, field):
    moves = []
    candidates = []
    if amphipod.position.y == 3:
        if amphipod.type == "A" and amphipod.position.x != 3:
            candidates.append((Position(amphipod.position.x, amphipod.position.y - 1)))
            candidates.append((Position(1, amphipod.position.y - 2)))
            candidates.append((Position(2, amphipod.position.y - 2)))
            candidates.append((Position(4, amphipod.position.y - 2)))
            candidates.append((Position(6, amphipod.position.y - 2)))
            candidates.append((Position(8, amphipod.position.y - 2)))
            candidates.append((Position(9, amphipod.position.y - 2)))
            candidates.append((Position(10, amphipod.position.y - 2)))
        elif amphipod.type == "B" and amphipod.position.x != 5:
            return []
        elif amphipod.type == "C" and amphipod.position.x != 7:
            return []
        elif amphipod.type == "D" and amphipod.position.x != 9:
            return []
    return moves


def printfield(field):
    for y in range(len(field)):
        print("".join(field[y]))


def main():
    amphipods = []
    field = []

    input = open("day23example.txt", "r").read().split("\n")
    for y in range(len(input)):
        field.append([])
        for x in range(len(input[y])):
            field[y].append(input[y][x])
            if input[y][x] in ["A", "B", "C", "D"]:
                amphipods.append(Amphipod(input[y][x], Position(x, y)))

    print(getmoves(amphipods[0], field))
    # printfield(field)


if __name__ == "__main__":
    main()

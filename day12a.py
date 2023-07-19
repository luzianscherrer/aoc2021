import copy


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def multi_visit(self):
        return self.name != "start" and self.name != "end" and self.name.isupper()

    def __str__(self):
        return f"name:{self.name} neighbours:{list(map(lambda a: a.name, self.neighbours))}"

    def __repr__(self):
        return self.__str__()


nodes = {}


def search_path(node, path, total):
    path.append(node)
    if node.name == "end":
        total[0] += 1
        # print(f"found path {list(map(lambda a: a.name, path))}")
        return total

    for neighbour in node.neighbours:
        if neighbour not in path or neighbour.multi_visit():
            search_path(neighbour, copy.copy(path), total)

    return total


def main():
    input = open("day12input.txt", "r").read().split("\n")
    for line in input:
        leftin, rightin = line.split("-")
        if leftin in nodes:
            left = nodes[leftin]
        else:
            left = Node(leftin)
            nodes[leftin] = left
        if rightin in nodes:
            right = nodes[rightin]
        else:
            right = Node(rightin)
            nodes[rightin] = right
        left.neighbours.append(right)
        right.neighbours.append(left)

    paths = search_path(nodes["start"], [], [0])
    print(paths[0])


if __name__ == "__main__":
    main()

class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __str__(self):
        return f"{self.value}|{self.x},{self.y}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def bfsearch(input, queue, visited, node):
    if node in visited:
        return visited
    visited.append(node)
    queue.append(node)
    # print(f"bfsearch for node {node} with visited {visited} and queue {queue}")

    while queue:
        curnode = queue.pop(0)
        if curnode.y > 0 and int(input[curnode.y-1][curnode.x]) != 9 and int(input[curnode.y-1][curnode.x]) > curnode.value:
            bfsearch(input, queue, visited, Node(
                curnode.x, curnode.y-1, int(input[curnode.y-1][curnode.x])))
        if curnode.y < len(input)-1 and int(input[curnode.y+1][curnode.x]) != 9 and int(input[curnode.y+1][curnode.x]) > curnode.value:
            bfsearch(input, queue, visited, Node(
                curnode.x, curnode.y+1, int(input[curnode.y+1][curnode.x])))
        if curnode.x > 0 and int(input[curnode.y][curnode.x-1]) != 9 and int(input[curnode.y][curnode.x-1]) > curnode.value:
            bfsearch(input, queue, visited, Node(
                curnode.x-1, curnode.y, int(input[curnode.y][curnode.x-1])))
        if curnode.x < len(input[curnode.y])-1 and int(input[curnode.y][curnode.x+1]) != 9 and int(input[curnode.y][curnode.x+1]) > curnode.value:
            bfsearch(input, queue, visited, Node(
                curnode.x+1, curnode.y, int(input[curnode.y][curnode.x+1])))

    return visited


def main():
    input = open("day09input.txt", "r").read().split("\n")
    basins = []
    for y in range(len(input)):
        for x in range(len(input[y])):
            cur = int(input[y][x])

            if y == 0:
                above = 10
            else:
                above = int(input[y-1][x])

            if y == len(input)-1:
                below = 10
            else:
                below = int(input[y+1][x])

            if x == 0:
                left = 10
            else:
                left = int(input[y][x-1])

            if x == len(input[y])-1:
                right = 10
            else:
                right = int(input[y][x+1])

            if above > cur and below > cur and left > cur and right > cur:
                # print(f"lowpoint {cur} ({x},{y})")
                visited = bfsearch(input, [], [], Node(x, y, cur))
                basins.append(visited)

    basins.sort(key=lambda a: len(a), reverse=True)
    print(len(basins[0]) * len(basins[1]) * len(basins[2]))


if __name__ == "__main__":
    main()

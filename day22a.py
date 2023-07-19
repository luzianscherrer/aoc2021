import re


def main():
    cubes = set()
    input = open("day22input.txt", "r").read().split("\n")
    for line in input:
        state, x1, x2, y1, y2, z1, z2 = re.match(
            r"(on|off) x=([-0-9]+)\.\.([-0-9]+),y=([-0-9]+)\.\.([-0-9]+),z=([-0-9]+)\.\.([-0-9]+)",
            line,
        ).groups()
        x1, x2, y1, y2, z1, z2 = int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)
        if abs(x1) > 100:
            continue
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    if state == "on":
                        cubes.add((x, y, z))
                    elif (x, y, z) in cubes:
                        cubes.remove((x, y, z))
    print(len(cubes))


if __name__ == "__main__":
    main()

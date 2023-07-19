import re

X1 = 0
X2 = 1
Y1 = 2
Y2 = 3
Z1 = 4
Z2 = 5
STATE = 6


def main():
    input = open("day22input.txt", "r").read().split("\n")

    cuboids = []
    steps = []
    min = 0
    max = 0

    for line in input:
        state, x1, x2, y1, y2, z1, z2 = re.match(
            r"(on|off) x=([-0-9]+)\.\.([-0-9]+),y=([-0-9]+)\.\.([-0-9]+),z=([-0-9]+)\.\.([-0-9]+)",
            line,
        ).groups()
        step = (int(x1), int(x2), int(y1), int(y2), int(z1), int(z2), state)
        if step[X1] < min:
            min = step[X1]
        if step[X2] > max:
            max = step[X2]
        if step[Y1] < min:
            min = step[Y1]
        if step[Y2] > max:
            max = step[Y2]
        if step[Z1] < min:
            min = step[Z1]
        if step[Z2] > max:
            max = step[Z2]
        steps.append(step)
    cuboids.append((min, max, min, max, min, max, "off"))
    print(cuboids)

    count = 0
    for step in steps:
        i = 0
        while i < len(cuboids):
            cuboid = cuboids[i]
            if step[STATE] != cuboid[STATE]:
                if (
                    step[X1] <= cuboid[X1]
                    and step[X2] >= cuboid[X2]
                    and step[Y1] <= cuboid[Y1]
                    and step[Y2] >= cuboid[Y2]
                    and step[Z1] <= cuboid[Z1]
                    and step[Z2] >= cuboid[Z2]
                ):
                    print("covered", end=" ")
                    cuboids[i] = (
                        cuboid[X1],
                        cuboid[X2],
                        cuboid[Y1],
                        cuboid[Y2],
                        cuboid[Z1],
                        cuboid[Z2],
                        step[STATE],
                    )
                else:
                    changes = []
                    did_cut = False
                    current = cuboid

                    if (
                        step[X1] > current[X1]
                        and step[X1] <= current[X2]
                        and current[Y1] <= step[Y2]
                        and current[Y2] >= step[Y1]
                        and current[Z1] <= step[Z2]
                        and current[Z2] >= step[Z1]
                    ):
                        print("x1", end=" ")
                        changes.append(current)
                        changes[-1] = (
                            step[X1],
                            current[X2],
                            current[Y1],
                            current[Y2],
                            current[Z1],
                            current[Z2],
                            current[STATE],
                        )
                        cuboids[i] = (
                            cuboid[X1],
                            step[X1] - 1,
                            cuboid[Y1],
                            cuboid[Y2],
                            cuboid[Z1],
                            cuboid[Z2],
                            cuboid[STATE],
                        )
                        did_cut = True
                        current = changes[-1]

                    # print(changes)

                    if (
                        step[X2] < current[X2]
                        and step[X2] >= current[X1]
                        and current[Y1] <= step[Y2]
                        and current[Y2] >= step[Y1]
                        and current[Z1] <= step[Z2]
                        and current[Z2] >= step[Z1]
                    ):
                        print("x2", end=" ")
                        changes.append(current)
                        changes[-1] = (
                            current[X1],
                            step[X2],
                            current[Y1],
                            current[Y2],
                            current[Z1],
                            current[Z2],
                            current[STATE],
                        )
                        if did_cut == False:
                            cuboids[i] = (
                                step[X2] + 1,
                                cuboid[X2],
                                cuboid[Y1],
                                cuboid[Y2],
                                cuboid[Z1],
                                cuboid[Z2],
                                cuboid[STATE],
                            )
                            did_cut = True
                        else:
                            changes[-2] = (
                                step[X2] + 1,
                                changes[-2][X2],
                                changes[-2][Y1],
                                changes[-2][Y2],
                                changes[-2][Z1],
                                changes[-2][Z2],
                                changes[-2][STATE],
                            )
                        current = changes[-1]

                    # print(changes)

                    if (
                        step[Y1] > current[Y1]
                        and step[Y1] <= current[Y2]
                        and current[X1] <= step[X2]
                        and current[X2] >= step[X1]
                        and current[Z1] <= step[Z2]
                        and current[Z2] >= step[Z1]
                    ):
                        print("y1", end=" ")
                        changes.append(current)
                        changes[-1] = (
                            current[X1],
                            current[X2],
                            step[Y1],
                            current[Y2],
                            current[Z1],
                            current[Z2],
                            current[STATE],
                        )
                        if did_cut == False:
                            cuboids[i] = (
                                cuboid[X1],
                                cuboid[X2],
                                cuboid[Y1],
                                step[Y1] - 1,
                                cuboid[Z1],
                                cuboid[Z2],
                                cuboid[STATE],
                            )
                            did_cut = True
                        else:
                            changes[-2] = (
                                changes[-2][X1],
                                changes[-2][X2],
                                changes[-2][Y1],
                                step[Y1] - 1,
                                changes[-2][Z1],
                                changes[-2][Z2],
                                changes[-2][STATE],
                            )
                        current = changes[-1]

                    # print(changes)

                    if (
                        step[Y2] < current[Y2]
                        and step[Y2] >= current[Y1]
                        and current[X1] <= step[X2]
                        and current[X2] >= step[X1]
                        and current[Z1] <= step[Z2]
                        and current[Z2] >= step[Z1]
                    ):
                        print("y2", end=" ")
                        changes.append(current)
                        changes[-1] = (
                            current[X1],
                            current[X2],
                            current[Y1],
                            step[Y2],
                            current[Z1],
                            current[Z2],
                            current[STATE],
                        )
                        if did_cut == False:
                            cuboids[i] = (
                                cuboid[X1],
                                cuboid[X2],
                                step[Y2] + 1,
                                cuboid[Y2],
                                cuboid[Z1],
                                cuboid[Z2],
                                cuboid[STATE],
                            )
                            did_cut = True
                        else:
                            changes[-2] = (
                                changes[-2][X1],
                                changes[-2][X2],
                                step[Y2] + 1,
                                changes[-2][Y2],
                                changes[-2][Z1],
                                changes[-2][Z2],
                                changes[-2][STATE],
                            )
                        current = changes[-1]

                    # print(changes)

                    if (
                        step[Z1] > current[Z1]
                        and step[Z1] <= current[Z2]
                        and current[X1] <= step[X2]
                        and current[X2] >= step[X1]
                        and current[Y1] <= step[Y2]
                        and current[Y2] >= step[Y1]
                    ):
                        print("z1", end=" ")
                        changes.append(current)
                        changes[-1] = (
                            current[X1],
                            current[X2],
                            current[Y1],
                            current[Y2],
                            step[Z1],
                            current[Z2],
                            current[STATE],
                        )
                        if did_cut == False:
                            cuboids[i] = (
                                cuboid[X1],
                                cuboid[X2],
                                cuboid[Y1],
                                cuboid[Y2],
                                cuboid[Z1],
                                step[Z1] - 1,
                                cuboid[STATE],
                            )
                            did_cut = True
                        else:
                            changes[-2] = (
                                changes[-2][X1],
                                changes[-2][X2],
                                changes[-2][Y1],
                                changes[-2][Y2],
                                changes[-2][Z1],
                                step[Z1] - 1,
                                changes[-2][STATE],
                            )
                        current = changes[-1]

                    # print(changes)

                    if (
                        step[Z2] < current[Z2]
                        and step[Z2] >= current[Z1]
                        and current[X1] <= step[X2]
                        and current[X2] >= step[X1]
                        and current[Y1] <= step[Y2]
                        and current[Y2] >= step[Y1]
                    ):
                        print("z2", end=" ")
                        changes.append(current)
                        changes[-1] = (
                            current[X1],
                            current[X2],
                            current[Y1],
                            current[Y2],
                            current[Z1],
                            step[Z2],
                            current[STATE],
                        )
                        if did_cut == False:
                            cuboids[i] = (
                                cuboid[X1],
                                cuboid[X2],
                                cuboid[Y1],
                                cuboid[Y2],
                                step[Z2] + 1,
                                cuboid[Z2],
                                cuboid[STATE],
                            )
                            did_cut = True
                        else:
                            changes[-2] = (
                                changes[-2][X1],
                                changes[-2][X2],
                                changes[-2][Y1],
                                changes[-2][Y2],
                                step[Z2] + 1,
                                changes[-2][Z2],
                                changes[-2][STATE],
                            )
                        current = changes[-1]

                    if len(changes):
                        changes[-1] = (
                            changes[-1][X1],
                            changes[-1][X2],
                            changes[-1][Y1],
                            changes[-1][Y2],
                            changes[-1][Z1],
                            changes[-1][Z2],
                            step[STATE],
                        )
                        cuboids.extend(changes)
            i += 1
        print()
        print(f"round {count} cubes {len(cuboids)}")
        count += 1

    cubes = 0
    for cuboid in cuboids:
        if cuboid[STATE] == "on":
            cubes += (
                (cuboid[X2] - cuboid[X1] + 1)
                * (cuboid[Y2] - cuboid[Y1] + 1)
                * (cuboid[Z2] - cuboid[Z1] + 1)
            )
    print(cubes)


if __name__ == "__main__":
    main()

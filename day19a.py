import numpy as np
import copy


def rotations(vs):
    rot_x_90 = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    rot_y_90 = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    rot_z_90 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])

    for _ in range(4):
        for i in range(len(vs)):
            vs[i] = np.matmul(vs[i], rot_x_90)
        yield vs

    for i in range(len(vs)):
        vs[i] = np.matmul(vs[i], rot_z_90)

    for _ in range(4):
        for i in range(len(vs)):
            vs[i] = np.matmul(vs[i], rot_y_90)
        yield vs

    for i in range(len(vs)):
        vs[i] = np.matmul(vs[i], rot_z_90)

    for _ in range(4):
        for i in range(len(vs)):
            vs[i] = np.matmul(vs[i], rot_x_90)
        yield vs

    for i in range(len(vs)):
        vs[i] = np.matmul(vs[i], rot_z_90)

    for _ in range(4):
        for i in range(len(vs)):
            vs[i] = np.matmul(vs[i], rot_y_90)
        yield vs

    for i in range(len(vs)):
        vs[i] = np.matmul(vs[i], rot_z_90)

    for i in range(len(vs)):
        vs[i] = np.matmul(vs[i], rot_y_90)

    for _ in range(4):
        for i in range(len(vs)):
            vs[i] = np.matmul(vs[i], rot_z_90)
        yield vs

    for i in range(len(vs)):
        vs[i] = np.matmul(vs[i], rot_y_90)

    for i in range(len(vs)):
        vs[i] = np.matmul(vs[i], rot_y_90)

    for _ in range(4):
        for i in range(len(vs)):
            vs[i] = np.matmul(vs[i], rot_z_90)
        yield vs


def main():
    input = open("day19input.txt", "r").read().split("\n")
    scanners = []
    scanner = []
    for line in input:
        if "scanner" in line:
            if len(scanner):
                scanners.append(scanner)
            scanner = []
        if "," in line:
            x, y, z = line.split(",")
            v = np.array(
                [
                    int(x),
                    int(y),
                    int(z),
                ]
            )
            scanner.append(v)
    scanners.append(scanner)

    normalized_beacons = copy.copy(scanners[0])
    normalized_scanners = [np.array([0, 0, 0])]

    scans_to_check = []
    for i in range(1, len(scanners)):
        for rotation in rotations(scanners[i]):
            scans_to_check.append(copy.copy(rotation))

    while scans_to_check:
        scan_to_check = scans_to_check.pop(0)

        diffs = {}
        for i in range(len(normalized_beacons)):
            for k in range(len(scan_to_check)):
                res = np.subtract(normalized_beacons[i], scan_to_check[k])
                diff = f"{res[0],res[1],res[2]}"
                if diff not in diffs:
                    diffs[diff] = 0
                diffs[diff] += 1

        found = False
        for key in diffs:
            if diffs[key] >= 12:
                print(
                    f"found scanner at {key} / normalized beacons: {len(normalized_beacons)}"
                )
                distance = eval(key)
                normalized_scanners.append(np.array(distance))
                for beacon in scan_to_check:
                    normalized_beacons.append(np.add(beacon, np.array(distance)))
                    uniq = np.unique(normalized_beacons, axis=0)
                    normalized_beacons = []
                    for element in uniq:
                        normalized_beacons.append(element)
                found = True
                break

        if len(normalized_scanners) == len(scanners):
            break

        if found == False:
            scans_to_check.append(scan_to_check)

    print(f"beacons: {len(normalized_beacons)}")


if __name__ == "__main__":
    main()

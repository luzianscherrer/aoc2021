import re


def main():
    input = open("day17input.txt", "r").read()

    x1, x2, y2, y1 = re.match(
        r".*x=([0-9]+)\.+([0-9]+), y=([-0-9]+)\.+([-0-9]+).*", input
    ).groups()
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    bestheight = 0
    for start_velocity_x in range(1, x2 + 1):
        for start_velocity_y in range(1, x2):
            velocity_x = start_velocity_x
            velocity_y = start_velocity_y
            coord_x = 0
            coord_y = 0
            maxheight = 0
            while coord_x <= x2 and coord_y >= y2:
                coord_x += velocity_x
                coord_y += velocity_y

                if coord_y > maxheight:
                    maxheight = coord_y

                if velocity_x > 0:
                    velocity_x -= 1
                elif velocity_x < 0:
                    velocity_x += 1
                velocity_y -= 1

                if coord_x >= x1 and coord_x <= x2 and coord_y <= y1 and coord_y >= y2:
                    if maxheight > bestheight:
                        bestheight = maxheight
                    break

    print(bestheight)


if __name__ == "__main__":
    main()

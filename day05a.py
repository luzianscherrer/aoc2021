import re

def print_field(field, width, height):
    for y in range(height):
        for x in range(width):
            print(field[y*width+x], end="")
        print()

def main():
    file = open("day05input.txt", "r")
    width = height = 0
    instructions = []
    input = file.read().split("\n")
    for line in input:
        str = re.match(r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)", line).groups()
        x1, y1, x2, y2 = list(map(int, str))
        if x1 > width:
            width = x1
        if x2 > width:
            width = x2
        if y1 > height:
            height = y1
        if y2 > height:
            height = y2
        instructions.append([x1, y1, x2, y2])
    width += 1
    height += 1

    field = [0 for _ in range(width*height)]
    
    for instruction in instructions:
        x1, y1, x2, y2 = instruction
        step = 0
        if x1 == x2:
            step = (-width, width)[y2>y1]
        elif y1 == y2:
            step = (-1, 1)[x2>x1]
        if step != 0:
            for point in range(x1+y1*height, x2+y2*height+step, step):
                field[point] += 1

    # print_field(field, width, height)
    print(len(list(filter(lambda a : a>1, field))))

if __name__ == "__main__":
    main()

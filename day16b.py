from functools import reduce


def operation(operator, operands):
    if operator == 0:
        return sum(operands)
    elif operator == 1:
        return reduce(lambda a, b: a * b, operands)
    elif operator == 2:
        return min(operands)
    elif operator == 3:
        return max(operands)
    elif operator == 5:
        return int(operands[0] > operands[1])
    elif operator == 6:
        return int(operands[0] < operands[1])
    elif operator == 7:
        return int(operands[0] == operands[1])


def readbits(binstr, len, num):
    return int(binstr[:num], 2), binstr[num:], len + num


def process(binstr, len, indent):
    # print(f"{'':>{indent}}process {binstr}")

    version, binstr, len = readbits(binstr, len, 3)
    type, binstr, len = readbits(binstr, len, 3)

    if type == 4:
        literal = 0
        while True:
            literal = literal << 4
            mode, binstr, len = readbits(binstr, len, 1)
            part, binstr, len = readbits(binstr, len, 4)
            literal += part
            if mode == 0:
                break
    else:
        length_type, binstr, len = readbits(binstr, len, 1)
        if length_type == 0:
            total_bits, binstr, len = readbits(binstr, len, 15)
            operands = []
            sublen = 0
            while sublen != total_bits:
                binstr, sublen, literal = process(binstr, sublen, indent + 2)
                operands.append(literal)
            len += sublen
        else:
            total_count, binstr, len = readbits(binstr, len, 11)
            sublen = 0
            count = 0
            operands = []
            while count != total_count:
                binstr, sublen, literal = process(binstr, sublen, indent + 2)
                operands.append(literal)
                count += 1
            len += sublen

        literal = operation(type, operands)

    return binstr, len, literal


def main():
    input = open("day16input.txt", "r").read()
    binstr = ""
    for char in input:
        binstr += f"{int(char, base=16):04b}"

    binstr, _, literal = process(binstr, 0, 0)
    print(literal)


if __name__ == "__main__":
    main()

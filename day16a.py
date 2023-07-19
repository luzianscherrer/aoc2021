from enum import Enum

State = Enum(
    "State",
    ["Version", "Type", "Literal", "Operator"],
)

offset = 0
binstr = ""
subpacket = []
state = [State.Version]
version_total = 0


def readbits(num):
    global binstr, offset, subpacket
    val = int(binstr[offset : offset + num], 2)
    offset += num

    if len(subpacket):
        (counttype, length) = subpacket[-1]
        if counttype == "length":
            subpacket[-1] = (counttype, length - num)

    return val


def main():
    global binstr, offset, subpacket, state, version_total
    input = open("day16input.txt", "r").read()
    for char in input:
        binstr += f"{int(char, base=16):04b}"

    while len(state) and offset < len(binstr) - 1:
        if state[-1] == State.Version:
            version = readbits(3)
            version_total += version
            # print(f"{' ':>{len(state)*2}}{version=}")
            state[-1] = State.Type
        elif state[-1] == State.Type:
            type = readbits(3)
            # print(f"{' ':>{len(state)*2}}{type=}")
            if type == 4:
                state[-1] = State.Literal
                literal = 0
            else:
                state[-1] = State.Operator
        elif state[-1] == State.Literal:
            bits = readbits(5)
            literal = literal << 4
            if bits & 0x10 == 0x10:
                bits = bits & 0xF
                literal += bits
            else:
                literal += bits
                # print(f"{' ':>{len(state)*2}}{literal=}")
                if len(subpacket):
                    (counttype, count) = subpacket[-1]
                    if counttype == "count":
                        subpacket[-1] = (counttype, count - 1)
                    (counttype, num) = subpacket[-1]
                    if num == 0:
                        state.pop()
                    else:
                        state[-1] = State.Version
                else:
                    state.pop()
        elif state[-1] == State.Operator:
            lengthtype = readbits(1)
            if lengthtype == 0:
                subpacket_length = readbits(15)
                # print(f"{' ':>{len(state)*2}}{subpacket_length=}")
                subpacket.append(("length", subpacket_length))
                state[-1] = State.Version
                state.append(State.Version)
            else:
                subpacket_count = readbits(11)
                # print(f"{' ':>{len(state)*2}}{subpacket_count=}")
                subpacket.append(("count", subpacket_count))
                state[-1] = State.Version
                state.append(State.Version)

    print(f"{version_total=}")


if __name__ == "__main__":
    main()

def explode(sum, pos):
    # print(f"explode {sum} at {pos}")
    pair = ""
    i = pos + 1
    while sum[i] != "]":
        pair += sum[i]
        i += 1
    left, right = pair.split(",")
    sum = "0".join([sum[:pos], sum[i + 1 :]])

    repl = ""
    for i in range(pos + 1, len(sum)):
        if sum[i].isdigit():
            repl += sum[i]
        elif sum[i].isdigit() == False and len(repl):
            sum = f"{int(repl)+int(right)}".join([sum[: i - len(repl)], sum[i:]])
            break

    repl = ""
    for i in range(pos - 1, 0, -1):
        if sum[i].isdigit():
            repl = f"{sum[i]}{repl}"
        elif sum[i].isdigit() == False and len(repl):
            sum = f"{int(repl)+int(left)}".join(
                [sum[: i + 1], sum[i + len(repl) + 1 :]]
            )
            break

    # print(f"exploded {sum}")
    return sum


def reduce(sum):
    # print(f"reduce {sum}")
    keep_going = True
    while keep_going:
        keep_going = False

        keep_exploding = True
        while keep_exploding:
            keep_exploding = False
            level = 0
            for i in range(len(sum)):
                if sum[i] == "[":
                    level += 1
                elif sum[i] == "]":
                    level -= 1
                if level == 5:
                    sum = explode(sum, i)
                    keep_exploding = True
                    break

        repl = ""
        for i in range(len(sum)):
            if sum[i].isdigit() and len(repl) == 0:
                repl = sum[i]
            elif sum[i].isdigit() and len(repl):
                repl += sum[i]
            elif sum[i].isdigit() == False and len(repl) > 1:
                left = int(repl) // 2
                right = int(repl) - left
                sum = f"[{left},{right}]".join([sum[: i - len(repl)], sum[i:]])
                keep_going = True
                break
            else:
                repl = ""

    # print(f"reduced {sum}")
    return sum


def magnitude(sum):
    if type(sum) != list:
        return sum
    return 3 * magnitude(sum[0]) + 2 * magnitude(sum[1])


def main():
    input = open("day18input.txt", "r").read().split("\n")
    sum = ""
    for line in input:
        if sum == "":
            sum = line
        else:
            sum = f"[{sum},{line}]"
        sum = reduce(sum)
    print(magnitude(eval(sum)))


if __name__ == "__main__":
    main()

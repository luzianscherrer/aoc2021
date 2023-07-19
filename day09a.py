def main():
    input = open("day09input.txt", "r").read().split("\n")
    total = 0
    for row in range(len(input)):
        for col in range(len(input[row])):
            cur = int(input[row][col])

            if row == 0:
                above = 10
            else:
                above = int(input[row-1][col])

            if row == len(input)-1:
                below = 10
            else:
                below = int(input[row+1][col])

            if col == 0:
                left = 10
            else:
                left = int(input[row][col-1])

            if col == len(input[row])-1:
                right = 10
            else:
                right = int(input[row][col+1])

            if above > cur and below > cur and left > cur and right > cur:
                total += (cur+1)

    print(total)

if __name__ == "__main__":
    main()
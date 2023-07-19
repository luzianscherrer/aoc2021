def main():
    input = open("day10input.txt", "r").read().split("\n")
    pairs = {"(":")", ")":"(", "[":"]", "]":"[", "{":"}", "}":"{", "<":">", ">":"<"}
    points = {")":3, "]":57, "}":1197, ">":25137}
    # score = {")":0, "]":0, "}":0, ">":0}
    score = 0
    stack = []
    for line in input:
        for char in line:
            if char in "([{<":
                stack.append(char)
            elif char in ")]}>" and stack[-1] == pairs[char]:
                stack.pop()
            else:
                # print(f"expected {pairs[stack[-1]]}, but found {char} ({points[char]} points)")
                score += points[char]
                break
    print(score)

if __name__ == "__main__":
    main()

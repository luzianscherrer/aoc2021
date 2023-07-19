def main():
    input = open("day10input.txt", "r").read().split("\n")
    pairs = {"(":")", ")":"(", "[":"]", "]":"[", "{":"}", "}":"{", "<":">", ">":"<"}
    points = {")":1, "]":2, "}":3, ">":4}
    scores = []
    for line in input:
        score = 0
        stack = []
        is_corrupt = False
        for char in line:
            if char in "([{<":
                stack.append(char)
            elif char in ")]}>" and stack[-1] == pairs[char]:
                stack.pop()
            else:
                is_corrupt = True
                break
        if is_corrupt == False:
            while len(stack):
                popped = pairs[stack.pop()]
                score *= 5
                score += points[popped]
            scores.append(score)
    scores.sort()
    print(scores[int(len(scores)/2)])
        
if __name__ == "__main__":
    main()

def roll(n):
    p = (n + 1) * 3
    q = p - 3
    upper = (p * (p + 1)) // 2
    lower = (q * (q + 1)) // 2
    return upper - lower


def run(positions, scores):
    round = 0
    while True:
        for player in range(len(positions)):
            positions[player] = (positions[player] + roll(round) - 1) % 10 + 1
            scores[player] += positions[player]
            round += 1
            if scores[player] >= 1000:
                return round * 3 * min(scores)


def main():
    positions = []
    scores = [0, 0]
    input = open("day21input.txt", "r").read().split("\n")
    for line in input:
        positions.append(int(line.split(": ")[1]))

    print(run(positions, scores))


if __name__ == "__main__":
    main()

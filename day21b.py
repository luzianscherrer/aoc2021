def run(statecount):
    wins = [0, 0]
    while len(statecount):
        statecount_new = {}

        for state, count in statecount.items():
            (p1pos, p1scr), (p2pos, p2scr) = state
            for i1 in range(1, 4):
                for j1 in range(1, 4):
                    for k1 in range(1, 4):
                        p1pos_new = (p1pos + i1 + j1 + k1 - 1) % 10 + 1
                        p1scr_new = p1scr + p1pos_new
                        if p1scr_new >= 21:
                            wins[0] += count
                        else:
                            for i2 in range(1, 4):
                                for j2 in range(1, 4):
                                    for k2 in range(1, 4):
                                        p2pos_new = (p2pos + i2 + j2 + k2 - 1) % 10 + 1
                                        p2scr_new = p2scr + p2pos_new
                                        if p2scr_new >= 21:
                                            wins[1] += count
                                        else:
                                            state_new = (
                                                (p1pos_new, p1scr_new),
                                                (p2pos_new, p2scr_new),
                                            )
                                            if state_new in statecount_new:
                                                statecount_new[state_new] += count
                                            else:
                                                statecount_new[state_new] = count

        statecount = statecount_new
    return wins


def main():
    input = open("day21input.txt", "r").read().split("\n")
    pos1 = int(input[0].split(": ")[1])
    pos2 = int(input[1].split(": ")[1])
    state = ((pos1, 0), (pos2, 0))
    statecount = {state: 1}
    print(max(run(statecount)))


if __name__ == "__main__":
    main()

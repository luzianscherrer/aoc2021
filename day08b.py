def main():
    input = open("day08input.txt", "r").read().split("\n")
    total = 0
    for line in input:
        patterns = list(line.split(" | ")[0].split(" "))
        lookup = {}
        fivesegs = []
        sixsegs = []
        for pattern in patterns:
            if len(pattern) == 2:
                lookup.update({'1': set(pattern)})
            elif len(pattern) == 3:
                lookup.update({'7': set(pattern)})
            elif len(pattern) == 4:
                lookup.update({'4': set(pattern)})
            elif len(pattern) == 5:
                fivesegs.append(set(pattern))
            elif len(pattern) == 6:
                sixsegs.append(set(pattern))
            elif len(pattern) == 7:
                lookup.update({'8': set(pattern)})
        # the 5 segment element with all segments from number 7 is number 3
        for fiveseg in fivesegs:
            if lookup["7"].issubset(fiveseg):
                lookup.update({'3': fiveseg})
                fivesegs.remove(fiveseg)
                break
        # the 6 segment element with all segments from number 3 is number 9
        for sixseg in sixsegs:
            if lookup["3"].issubset(sixseg):
                lookup.update({'9': sixseg})
                sixsegs.remove(sixseg)
                break
        # the 6 segment element with exactly 1 common element with number 1 is number 6
        # keep said common element as sigma
        for sixseg in sixsegs:
            sigma = lookup["1"].intersection(sixseg)
            if len(sigma) == 1:
                lookup.update({'6': sixseg})
                sixsegs.remove(sixseg)
                break
        # the remaining 6 segment element is number 0
        lookup.update({'0': sixsegs[0]})     
        # the 5 segment element that contains element sigma is number 5
        for fiveseg in fivesegs:
            if sigma.issubset(fiveseg):
                lookup.update({'5': fiveseg})
                fivesegs.remove(fiveseg)
                break 
        # the remaining 5 segment element is number 2
        lookup.update({'2': fivesegs[0]})   

        outputs = list(line.split(" | ")[1].split(" "))
        current = ""
        for output in outputs:
            for key in lookup.keys():
                if lookup[key] == set(output):
                    current += key
                    break
        total += int(current)

    print(total)

if __name__ == "__main__":
    main()
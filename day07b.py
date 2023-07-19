import sys

def main():
    positions = list(map(int, open("day07input.txt", "r").readline().split(",")))
    lower = min(positions)
    upper = max(positions)

    lowest_cost = sys.maxsize
    for height in range(lower, upper+1):
        cost = 0
        for position in positions:
            difference = abs(position-height)
            cost += int(difference*(difference+1)/2)
        if(cost < lowest_cost):
            lowest_cost = cost

    print(lowest_cost)
    
if __name__ == "__main__":
    main()
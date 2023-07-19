import sys

def main():
    positions = list(map(int, open("day07input.txt", "r").readline().split(",")))
    lower = min(positions)
    upper = max(positions)

    lowest_moves = sys.maxsize
    for height in range(lower, upper+1):
        moves = 0
        for position in positions:
            moves += abs(position-height)
        if(moves < lowest_moves):
            lowest_moves = moves

    print(lowest_moves)
    
if __name__ == "__main__":
    main()
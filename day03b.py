def process(pos, data, order):
    sum = 0
    for line in data:
        sum += int(line[pos])
    criteria = order[sum >= len(data)/2]
    newdata = list(filter(lambda e : e[pos] == criteria, data))
    if len(newdata) > 1:
        return process(pos+1, newdata, order)
    else:
        return int(newdata[0], 2)
    

file = open("day03input.txt", "r")
input = file.read().split("\n")

oxygen_generator = process(0, input, ("0" "1"))
co2_scrubber = process(0, input, ("1" "0"))

print(oxygen_generator * co2_scrubber)
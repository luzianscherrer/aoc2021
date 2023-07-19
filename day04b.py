import re
import functools
import copy

SUMMAND = 1000

def parse_input(input):
    field_width = 0
    numbers = []
    fields = []
    for line in input:
        if "," in line:
            numbers = [int(_) for _ in line.split(",")];
        elif len(line) == 0:
            fields.append([])
        else:
            parsed_line = [int(_) for _ in re.split(r"\s+", " "+line)[1:]]
            field_width = len(parsed_line)
            fields[-1] += parsed_line
    return numbers, fields, field_width

def mark_fields(fields, number):
    for i in range(len(fields)):
        fields[i] = list(map(lambda a : a+SUMMAND if a == number else a, fields[i]))

def calc_result(field):
    unmarked = list(filter(lambda a : a<SUMMAND, field))
    return functools.reduce(lambda a, b : a+b, unmarked)

def check_fields(fields, field_width):
    for field in copy.copy(fields):
        for row in range(0, len(field), field_width):
            if len(list(filter(lambda a : a>=SUMMAND, (field[row:row+field_width])))) == field_width:
                if len(fields) == 1:
                    return calc_result(field), fields
                else:
                    fields.remove(field)
        if field in fields:
            for col in range(field_width):
                if len(list(filter(lambda a : a>=SUMMAND, (field[col:field_width*(field_width-1)+1+col:field_width])))) == field_width:
                    if len(fields) == 1:
                        return calc_result(field), fields
                    else:
                        fields.remove(field)
    return -1, fields

def main():
    file = open("day04input.txt", "r")
    numbers, fields, field_width = parse_input(file.read().split("\n"))

    for number in numbers:
        mark_fields(fields, number)
        sum, fields = check_fields(fields, field_width)
        if sum >= 0:
            print(sum*number)
            break

if __name__ == "__main__":
    main()

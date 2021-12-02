# https://adventofcode.com/2020/day/2

from pathlib import Path
import re

day_1_input = "day_02_input.txt"
day_1_input_path = Path(__file__).parent / day_1_input

data = day_1_input_path.read_text().splitlines()


def parse_row(row):
    return re.findall("(\\d+)-(\\d+) ([a-z]): ([a-z]+)", row)[0]


# region part1
valid_passwords_count = 0

for row in data:
    min_count, max_count, char, password = parse_row(row)

    if int(min_count) <= password.count(char) <= int(max_count):
        valid_passwords_count += 1

print(valid_passwords_count)
# endregion


# region part2
valid_passwords_count = 0

for row in data:
    first_pos, second_pos, char, password = parse_row(row)

    try:
        first = password[int(first_pos) - 1] == char
    except IndexError:
        first = False
        pass

    try:
        second = password[int(second_pos) - 1] == char
    except IndexError:
        second = False
        pass

    if first ^ second:
        # print(first_pos)
        # print(first)
        # print(second_pos)
        # print(second)
        # print(char)
        # print(password)
        valid_passwords_count += 1
        # break


print(valid_passwords_count)
# endregion

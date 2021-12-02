# https://adventofcode.com/2020/day/1

from pathlib import Path

day_1_input = "day_01_input.txt"
day_1_input_path = Path(__file__).parent / day_1_input

data = day_1_input_path.read_text().splitlines()


# region part1
def get_nums_sum_to_2020(data):
    for i1, first in enumerate(data):
        num1 = int(first)

        for i2, second in enumerate(data):
            if i1 == i2:
                # Ignore using same number twice...
                continue

            num2 = int(second)

            if num1 + num2 == 2020:
                return num1, num2


num1, num2 = get_nums_sum_to_2020(data)

print(num1)
print(num2)
print(num1*num2)
# endregion


# region part2
def get_nums_sum_to_2020(data):
    for i1, first in enumerate(data):
        num1 = int(first)

        for i2, second in enumerate(data):
            if i1 == i2:
                # Ignore using same number twice...
                continue

            num2 = int(second)

            for i3, third in enumerate(data):
                if i1 == i3 or i2 == i3:
                    continue

                num3 = int(third)

                if num1 + num2 + num3 == 2020:
                    return num1, num2, num3


num1, num2, num3 = get_nums_sum_to_2020(data)

print(num1)
print(num2)
print(num3)
print(num1*num2*num3)
# endregion

# https://adventofcode.com/2020/day/3

from itertools import cycle, islice
from pathlib import Path

day_input = "day_03_input.txt"
day_input_path = Path(__file__).parent / day_input

data = day_input_path.read_text().splitlines()

# right 3 and down 1


# region part1
def get_trees_count(data, right, down):
    row = 0
    col = 0
    trees_count = 0

    while True:
        col += right
        row += down

        if row >= len(data):
            break

        cycle_row = cycle(data[row])
        value = next(islice(cycle_row, col, col+1))

        if value == "#":
            trees_count += 1

        # print(row, col)
        # print(value)
        # print(data[row])

    return trees_count


trees_count = get_trees_count(data=data, right=3, down=1)

print(f"trees_count: {trees_count}")
# endregion

# region part2

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.


slopes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2),
]

multiply = 1

for s in slopes:
    trees_count = get_trees_count(data, right=s[0], down=s[1])
    print(f"trees count for right={s[0]} an down={s[1]} is {trees_count}")
    multiply *= trees_count

print(f"multiply: {multiply}")

# endregion

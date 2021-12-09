# https://adventofcode.com/2021/day/5

from collections import Counter
from pathlib import Path
import re

day_input = "day_05_input.txt"
day_input_path = Path(__file__).parent / day_input

data = day_input_path.read_text().splitlines()


class Grid:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append(
            (x,y)
        )

    def add_vertical_and_horizontal_line(self, x1, y1, x2, y2):
        self.add_point(x1, y1)
        self.add_point(x2, y2)

        if x1 == x2:
            min_y, max_y = y1, y2

            if min_y > max_y:
                min_y, max_y = max_y, min_y

            if min_y > max_y:
                min_y, max_y = max_y, min_y

            for curr_y in range(min_y+1, max_y):
                self.add_point(x1, curr_y)

        if y1 == y2:
            min_x, max_x = x1, x2

            if min_x > max_x:
                min_x, max_x = max_x, min_x

            for curr_x in range(min_x+1, max_x):
                self.add_point(curr_x, y1)


# region part1
grid = Grid()

for row in data:
    # print(row)
    x1, x2, y1, y2 = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", row).groups()
    grid.add_vertical_and_horizontal_line(int(x1), int(x2), int(y1), int(y2))

c = Counter(grid.points)
print(f"overlap points: {len([v for v in c.values() if v > 1])}")
# endregion

# https://adventofcode.com/2021/day/4

from pathlib import Path

day_input = "day_04_input.txt"
day_input_path = Path(__file__).parent / day_input

data = day_input_path.read_text().splitlines()


class NumberOnBoard:
    def __init__(self, number):
        self.number = int(number.strip())
        self.marked = False

    @property
    def is_marked(self):
        return self.marked

    def mark(self):
        self.marked = True

    def mark_if_equal(self, number):
        if not isinstance(number, int):
            number = int(number)

        if self.number == number:
            self.mark()

    def __repr__(self):
        return f"{self.number}" if not self.is_marked else f"*{self.number}*"


class Board:
    # 5*5
    def __init__(self, rows):
        assert len(rows) == 5
        self.rows = rows
        self.lines = []

        for row in rows:
            self.lines.append([NumberOnBoard(num) for num in row.split()])

        new_lines = []

        for i in range(len(self.lines[0])):
            col_to_line = []

            for line in self.lines:
                col_to_line.append(line[i])

            new_lines.append(col_to_line)

        self.lines.extend(new_lines)

    def __repr__(self):
        # return f"{'\n'.join(str(num) for num in line)}"
        return f"{self.lines}"

    def mark(self, number):
        for line in self.lines:
            for num in line:
                num.mark_if_equal(number)

    def check_bingo(self):
        for line in self.lines:
            if all(num.is_marked for num in line):
                return True
        return False


# region part1
bingo_nums = data[0].split(",")

i = 2

boards = []

while i < len(data):
    b = Board(data[i:i+5])
    # print(b)
    boards.append(b)
    i += 6

for num in bingo_nums:
    # print(f"****{num}*****")
    winning = []

    for b in boards:
        b.mark(num)

        if b.check_bingo():
            winning.append(b)

    if winning:
        for win in winning:
            # pass
            print("##### BINGO #######")
            for curr_line in win.lines:
                print("\t".join(str(num) for num in curr_line))

        break


# endregion


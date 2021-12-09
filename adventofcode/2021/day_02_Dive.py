# https://adventofcode.com/2021/day/1

from pathlib import Path

import requests

day_2_input = "day_02_input.txt"
day_2_input_path = Path(__file__).parent / day_2_input

if not day_2_input_path.exists():
    # Won't work, since need to login to get the input
    data = requests.get("https://adventofcode.com/2021/day/2/input").text
    day_2_input_path.write_text(data)
else:
    data = day_2_input_path.read_text().splitlines()


# region part1
depth = 0
horizontal_pos = 0


def forward(value):
    global horizontal_pos
    horizontal_pos += value


def up(value):
    global depth
    depth -= value


def down(value):
    global depth
    depth += value


def process_instructions(instructions):
    for row in data:
        instruction, value = row.split()

        func = instructions[instruction]

        func(int(value))


process_instructions(instructions={
    "forward": forward,
    "up": up,
    "down": down,
})

print(f"depth: {depth}")
print(f"horizontal_pos: {horizontal_pos}")
print(f"multiply: {depth * horizontal_pos}")
# endregion

# region part1
aim = 0
depth = 0
horizontal_pos = 0


def down(value):
    # down X increases your aim by X units.
    global aim
    aim += value


def up(value):
    # up X decreases your aim by X units.
    global aim
    aim -= value


def forward(value):
    # forward X does two things:
    # It increases your horizontal position by X units.
    # It increases your depth by your aim multiplied by X.
    global horizontal_pos, depth
    horizontal_pos += value
    depth += (aim * value)


process_instructions(instructions={
    "forward": forward,
    "up": up,
    "down": down,
})


print(f"depth: {depth}")
print(f"horizontal_pos: {horizontal_pos}")
print(f"multiply: {depth * horizontal_pos}")
print(f"aim: {aim}")
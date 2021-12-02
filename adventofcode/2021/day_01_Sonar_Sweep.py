# https://adventofcode.com/2021/day/1

from pathlib import Path

import requests

day_1_input = "day_01_input.txt"
day_1_input_path = Path(__file__).parent / day_1_input

if not day_1_input_path.exists():
    # Won't work, since need to login to get the input
    data = requests.get("https://adventofcode.com/2021/day/1/input").text
    day_1_input_path.write_text(data)
else:
    data = day_1_input_path.read_text().splitlines()


def get_increased_measurements_count(data_array):
    measurements_count = 0

    last_num = None

    for row in data_array:
        num = int(row)

        if last_num and num > last_num:
            measurements_count += 1

        last_num = num
    return measurements_count


# region part1
measurements_count = get_increased_measurements_count(data)

print(measurements_count)
# endregion

# region part2
new_data_array = []

for index, row in enumerate(data[:-2]):
    sliding_window_sum = int(row) + int(data[index+1]) + int(data[index+2])
    new_data_array.append(sliding_window_sum)

measurements_count = get_increased_measurements_count(new_data_array)

print(measurements_count)
# endregion

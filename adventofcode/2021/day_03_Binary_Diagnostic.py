# https://adventofcode.com/2021/day/3

from collections import Counter, defaultdict
from pathlib import Path

day_input = "day_03_input.txt"
day_input_path = Path(__file__).parent / day_input

data = day_input_path.read_text().splitlines()


# region part1
gamma_rate = ""
epsilon_rate = ""

for col in range(len(data[0])):
    col_0_count = 0
    col_1_count = 0

    for row in data:
        if row[col] == "0":
            col_0_count += 1
        elif row[col] == "1":
            col_1_count += 1
        else:
            raise RuntimeError("Error parsing")

    if col_1_count > col_0_count:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

print(f"gamma_rate: {gamma_rate}")
print(f"epsilon_rate: {epsilon_rate}")

gamma_rate_dec = int(gamma_rate, 2)
epsilon_rate_dec = int(epsilon_rate, 2)

print(f"gamma_rate decimal: {gamma_rate_dec}")
print(f"epsilon_rate decimal: {epsilon_rate_dec}")
print(f"power consumption: {gamma_rate_dec*epsilon_rate_dec}")

# endregion


# region part2
def get_most_bit_by_position(data, col):
    # col_data = [row[col] for row in data]
    # c = Counter(col_data)
    # if c["1"] >= c["0"]:
    #     return "1"
    # return "0"
    rows = defaultdict(list)

    for row in data:
        bit = row[col]
        rows[bit].append(row)

    if len(rows["1"]) >= len(rows["0"]):
        return rows["1"]
    return rows["0"]


def get_least_bit_by_position(data, col):
    # col_data = [row[col] for row in data]
    # c = Counter(col_data)
    # if c["0"] <= c["1"]:
    #     return "0"
    # return "1"
    rows = defaultdict(list)

    for row in data:
        bit = row[col]
        rows[bit].append(row)

    if len(rows["0"]) <= len(rows["1"]):
        return rows["0"]
    return rows["1"]


oxygen_generator_rating = ""
co2_scrubber_rating = ""

curr_data = list(data)
col = 0

while col < len(curr_data[0]):
    curr_data = get_most_bit_by_position(curr_data, col)

    if len(curr_data) == 1:
        oxygen_generator_rating = curr_data[0]
        break

    col += 1

curr_data = list(data)
col = 0

while col < len(curr_data[0]):
    curr_data = get_least_bit_by_position(curr_data, col)

    if len(curr_data) == 1:
        co2_scrubber_rating = curr_data[0]
        break

    col += 1


print(f"oxygen_generator_rating: {oxygen_generator_rating}")
print(f"co2_scrubber_rating: {co2_scrubber_rating}")

oxygen_generator_rating_dec = int(oxygen_generator_rating, 2)
co2_scrubber_rating_dec = int(co2_scrubber_rating, 2)

print(f"oxygen_generator_rating_dec: {oxygen_generator_rating_dec}")
print(f"co2_scrubber_rating_dec: {co2_scrubber_rating_dec}")
print(f"life support rating: {oxygen_generator_rating_dec * co2_scrubber_rating_dec}")

# endregion
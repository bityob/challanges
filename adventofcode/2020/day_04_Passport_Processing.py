# https://adventofcode.com/2020/day/4

from pathlib import Path
import re

day_input = "day_04_input.txt"
day_input_path = Path(__file__).parent / day_input

data = day_input_path.read_text().splitlines()

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


# region part1
valid_passports = 0
curr_passports_fields = set()

for row in data:
    fields = re.findall("([a-z]+):", row)

    if not fields:
        # empty line
        curr_passports_fields = set()
        continue

    curr_passports_fields.update(set(fields))

    # all required fields exists in the passport
    if required_fields.issubset(curr_passports_fields):
        valid_passports += 1
        curr_passports_fields = set()

print(f"valid passports: {valid_passports}")

# endregion


# region part2
def get_year(year):
    if year != 4:
        return False

    for char in year:
        if not char.isdigit():
            return False

    try:
        year = int(year)
        return year
    except:
        return False


def check_byr(fields):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    byr = fields["byr"]

    year = get_year(byr)

    if not year:
        return False

    return 1920 <= year <= 2002


def check_iyr(fields):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    iyr = fields["iyr"]

    year = get_year(iyr)

    return 2010 <= year <= 2002


def check_eyr(fields):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    eyr = fields["eyr"]

    year = get_year(eyr)

    return 2020 <= year <= 2030


def check_hgt(fields):
    hgt = fields["hgt"]

    num, cm_or_in = re.findall("(\\d+)([cmin]+)", hgt)[0]

    if cm_or_in == "cm":
        return 150 <= int(num) <= 193
    elif cm_or_in == "in":
        return 59 <= int(num) <= 76

    raise RuntimeError("parsing error")

# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


valid_passports = 0
curr_passports_fields = {}

for row in data:
    fields = {}
    # re.findall("([a-z]+):", row)
    for part in row.split():
        field,  value = part.split(":")
        fields[field] = value

    if not fields:
        # empty line
        curr_passports_fields = set()
        continue

    curr_passports_fields.update(fields)

    # all required fields exists in the passport
    if required_fields.issubset(set(curr_passports_fields.keys())):
        # Now check the validation of the values too
        if check_byr(curr_passports_fields) \
                and check_iyr(curr_passports_fields) \
                and check_eyr(curr_passports_fields) \
                and check_hgt(curr_passports_fields):
            pass
            # and check
        valid_passports += 1
        curr_passports_fields = set()

print(f"valid passports: {valid_passports}")

# endregion

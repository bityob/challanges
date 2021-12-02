#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time_period = s[-2:]
    if time_period == "PM":
        hour = s[:2]
        if hour == "12":
            return hour + s[2:-2]
        else:
            new_hour = str(int(hour) + 12)
            return new_hour + s[2:-2]
    else:
        hour = s[:2]
        if hour == "12":
            return "00" + s[2:-2]
        else:
            return s[:-2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

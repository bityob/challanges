#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min_count = 0
    max_count = 0

    max_value = min_value = None

    for score in scores:
        if min_value is None:
            min_value = score
            max_value = score
            continue

        if min_value > score:
            min_value = score
            min_count += 1

        if max_value < score:
            max_value = score
            max_count += 1

    return max_count, min_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

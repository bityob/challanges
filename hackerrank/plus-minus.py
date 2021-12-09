#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    plus = 0
    minus = 0
    zeros = 0
    
    for number in arr:
        if number == 0:
            zeros += 1
        elif number > 0:
            plus += 1
        else:
            minus += 1
            
    print(plus/n)
    print(minus/n)
    print(zeros/n)
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

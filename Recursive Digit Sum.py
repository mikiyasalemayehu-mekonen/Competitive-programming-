#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    initial_sum = sum(int(digit) for digit in n) * k
    
    # Helper function to find the super digit of a number
    def findSuperDigit(num):
        if num < 10:
            return num
        else:
            return findSuperDigit(sum(int(digit) for digit in str(num)))
    
    return findSuperDigit(initial_sum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

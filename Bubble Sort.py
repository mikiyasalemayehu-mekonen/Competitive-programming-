#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swap=0
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j]>a[j+1]:
                swap+=1
                a[j], a[j+1]=a[j+1], a[j]
    print("Array is sorted in "+str(swap)+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[len(a)-1]))


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

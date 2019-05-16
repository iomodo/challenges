#!/bin/python3

# problem link:
# https://www.hackerrank.com/challenges/pairs

import math
import os
import random
import re
import sys

def buildMap(arr):
    d = {}
    for a in arr:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    return d

# Complete the pairs function below.
def pairs(k, arr):
    d = buildMap(arr)
    res = 0
    for a in arr:
        pot = a + k
        if pot in d:
            res += d[pot]
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

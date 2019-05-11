#!/bin/python3

# problem link:
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    res = math.inf
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i-1])
        res = min(res, diff)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


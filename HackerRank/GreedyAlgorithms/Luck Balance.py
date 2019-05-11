#!/bin/python3

# problem link:
# https://www.hackerrank.com/challenges/luck-balance

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    res = 0
    importantContests = []
    for contest in contests:
        if contest[1] == 1:
            importantContests.append(contest[0])
        else:
            res += contest[0]
    importantContests.sort()
    n = len(importantContests)
    important = max(n - k,0)
    for i in range(0,important):
        res -= importantContests[i]
    for i in range(important, n):
        res += importantContests[i]
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

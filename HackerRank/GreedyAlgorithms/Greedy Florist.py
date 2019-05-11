#!/bin/python3

# problem link:
# https://www.hackerrank.com/challenges/greedy-florist

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
	c.sort()
	res = 0
	flowers = 0
	num = 0
	for i in range(n-1, -1, -1):
		if num == k:
			flowers += 1
			num = 0
		res += (flowers + 1) * c[i]
		num += 1
	return res



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()

#!/bin/python3

# problem link:
# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor

import math
import os
import random
import re
import sys


def buildDict(cost):
    d = {}
    for i in range(len(cost)):
        if cost[i] in d:
            d[cost[i]].append(i)
        else:
            d[cost[i]] = [i]
    return d

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    d = buildDict(cost)
    for i in range(len(cost)):
        potential = money-cost[i]
        if potential in d:
            if potential == cost[i] and len(d[cost[i]])>1:
                print(min(d[cost[i]][0], d[cost[i]][1])+1, max(d[cost[i]][0], d[cost[i]][1])+1)
                return
            elif potential != cost[i]:
                index = d[money-cost[i]][0]
                print(min(i,index)+1, max(i,index)+1)
                return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

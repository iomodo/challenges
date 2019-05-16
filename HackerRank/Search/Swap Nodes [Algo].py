#!/bin/python3

import os
import sys


def inorder(indexes):
    res = []
    done = 0
    index = 1
    stack = []
    while True:
        if index != -1:
            stack.append(index)
            index = indexes[index-1][0]
        else:
            if len(stack) > 0:
                index = stack.pop()
                res.append(index)
                index = indexes[index-1][1]
            else:
                break
    return res


def countDepth(indexes):
    depth = {}
    depth[1] = 1
    for i in range(len(indexes)):
        dep = 1
        if (i+1) in depth:
            dep = depth[i+1]+1
        if indexes[i][0] != -1:
            depth[indexes[i][0]] = dep
        if indexes[i][1] != -1:
            depth[indexes[i][1]] = dep
    res = {}
    for i in depth:
        if depth[i] in res:
            res[depth[i]].append(i)
        else:
            res[depth[i]] = [i]
    return res, max(depth.values())
#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    result = []
    d, maxDepth = countDepth(indexes)
    for q in queries:
        index = q
        while index <= maxDepth:
            swaps = d[index]
            for swap in swaps:
                indexes[swap-1][0], indexes[swap-1][1] = indexes[swap-1][1], indexes[swap-1][0]
            index += q
        result.append(inorder(indexes))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

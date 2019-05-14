#!/bin/python3

# problem link
# https://www.hackerrank.com/challenges/reverse-shuffle-merge/

import math
import os
import random
import re
import sys

def countCharIndexes(s):
	charIndexes = {}
	for i in range(len(s)):
		if s[i] in charIndexes:
			charIndexes[s[i]].append(i)
		else:
			charIndexes[s[i]] = [i]
	for ch, indexes in charIndexes.items():
		indexes.sort()
	return charIndexes

def countIndexMaps(s):
	indexMaps = [{} for _ in range(len(s))]
	m = {ch : 0 for ch in "abcdefghijklmnopqrstuvwxyz"}
	for i in range(len(s)):
		m[s[i]] += 1
		indexMaps[i] = m.copy()
	return indexMaps

def getWordMap(m):
	wordMap = {}
	for ch in m:
		wordMap[ch] = m[ch] // 2
	return wordMap

def getCharLastIndex(ch, charIndexes, previousIndex):
	# can be done faster with binary search
	for i in range(len(charIndexes[ch])-1, -1, -1):
		if charIndexes[ch][i] < previousIndex:
			return charIndexes[ch][i]
	return -1

def isNextChar(ch, indexMaps, charIndexes, wordMap, previousIndex):
	charLastIndex = getCharLastIndex(ch, charIndexes, previousIndex)
	if charLastIndex == -1:
		return (False, previousIndex)
	for ch, count in indexMaps[charLastIndex].items():
		if ch in wordMap and count < wordMap[ch]:
			return (False, previousIndex)
	return (True, charLastIndex)

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
	indexMaps = countIndexMaps(s)
	wordMap = getWordMap(indexMaps[-1])
	charIndexes = countCharIndexes(s)

	res = ''
	prevIndex = len(s)
	while len(wordMap) != 0:
		for ch in list(wordMap):
			if wordMap[ch] == 0:
				del wordMap[ch]
			else:
				nextChar, prevIndex = isNextChar(ch, indexMaps, charIndexes, wordMap, prevIndex)
				if nextChar:
					res += ch
					wordMap[ch] -= 1
					charIndexes[ch] = charIndexes[ch][:-1]
					break
	return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()

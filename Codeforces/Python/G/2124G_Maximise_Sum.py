# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(1) Complexity

from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInt():
	return int(readLine())

def readInts():
	return list(map(int, readLine().split()))

t = readInt() #cases
a = readInt() #length
n = readInts() #integers

#all test cases does not exceed 1,000,000


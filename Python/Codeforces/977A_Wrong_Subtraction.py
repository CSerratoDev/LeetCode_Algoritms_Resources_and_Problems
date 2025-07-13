# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity
from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInts():
	return list(map(int, readLine().split()))

n, k = readInts()

for _ in range(k):
	if n % 10 != 0:
		n -= 1
	else: 
		n //= 10
print(n)


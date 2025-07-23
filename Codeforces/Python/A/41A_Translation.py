# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity

from sys import stdin

def readLine():
	return stdin.readline().strip()

s, t = readLine(), readLine()
print('YES' if s == t[::-1] else 'NO')

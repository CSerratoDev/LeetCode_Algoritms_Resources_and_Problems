# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(1) Complexity

from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInts():
	return list(map(int, readLine().split()))
# number friends, height in the fence
n, h = readInts() #h -> height,  width -> 1 person walking, but belt person is equal -> 2
a = readLine().split() #
#minimum width of the road
width = 0
for i in range(n):
	if int(a[i]) > h:
		width += 2
	else:
		width += 1

if __name__ == '__main__':
	print(width)
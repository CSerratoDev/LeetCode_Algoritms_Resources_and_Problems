# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity

from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInts():
	return list(map(int, readLine().split()))

n = readLine()
coord_x, coord_y, coord_z = 0, 0, 0
for i in range(int(n)):
	x,y,z = readInts()
	coord_x += x
	coord_y += y
	coord_z += z
if coord_x == 0 and coord_y == 0 and coord_z == 0:
	print('YES')
else:
	print('NO')
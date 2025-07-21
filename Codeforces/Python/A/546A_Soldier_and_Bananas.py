# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(1) Complexity
from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInts():
	return list(map(int, readLine().split()))

k, n, w = readInts()
borrow = 0
while w > 0:
	borrow += k * w 
	w -= 1 
if borrow > n:
	borrow -= n
else:
	borrow = 0
print(borrow)


#Most optimal version
k, n, w = map(int, input().split())

total_cost = k * w * (w + 1) // 2
borrow = max(0, total_cost - n)

print(borrow)
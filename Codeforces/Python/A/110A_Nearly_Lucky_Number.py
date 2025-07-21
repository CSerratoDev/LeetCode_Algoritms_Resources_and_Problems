# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity

from sys import stdin

def readLine():
	return stdin.readline().strip()

def solution(numbers):
	count = 0
	for digit in numbers:
		if digit == '4' or digit == '7':
			count += 1
	if count == 4 or count == 7:
		return 'YES'
	else:
		return 'NO'

n = readLine()
print(solution(n))
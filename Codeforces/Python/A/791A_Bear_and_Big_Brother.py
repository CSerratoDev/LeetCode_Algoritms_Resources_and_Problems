# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(1) Complexity

a, b = map(int, input().split())
years = 0
while a < b:
    a *= 3
    b *= 2
    years += 1
print(years)

#Recursive version
def solution(a, b, years=0):
	if a > b:
		return years
	return solution(a * 3, b * 2, years + 1)
	
a, b = map(int, input().split())
print(solution(a, b))

#Log version
import math

a, b = map(int, input().split())
years = math.ceil(math.log(b / a, 3 / 2))
print(years)
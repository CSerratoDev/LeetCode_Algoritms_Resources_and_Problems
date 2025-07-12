# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(1) Complexity
from sys import stdin

def readLine():
	return stdin.readline().strip()

s = readLine()
count_islower = 0
count_isupper = 0
for _ in range(len(s)):
	if s[_].islower():
		count_islower += 1
	else:
		count_isupper += 1
if count_islower >= count_isupper:
	s = s.lower()
else:
	s = s.upper()
print(s)

#Most optimal version
s = input().strip()
lower_count = sum(1 for c in s if c.islower())
print(s.lower() if lower_count >= len(s) - lower_count else s.upper())

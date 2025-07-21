# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(n) Complexity

from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInt():
	return int(readLine())

n = readInt()
s = readLine()
anton, danik  = 0, 0
for _ in range(n):
	if s[_] == "A":
		anton += 1
	elif s[_] == "D":
		danik += 1
if anton > danik:
	print('Anton')
elif danik > anton:
	print('Danik')
else:
	print('Friendship')
	
#Optimal version

n = readInt()
s = readLine()

a = s.count('A')
d = s.count('D')

if a > d:
	print('Anton')
elif d > a:
	print('Danik')
else:
	print('Friendship')
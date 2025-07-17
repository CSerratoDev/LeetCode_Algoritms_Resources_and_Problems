# By: cserrato.dev https://github.com/CSerratoDev

from sys import stdin

def readLine():
	return stdin.readline().strip()

t = int(readLine())
x = []
minimum = 0
for _ in range(t):
	x.append(readLine())

for i in range(t):
	minimum = int(x[i][0])
	for j in range(len(x[i])):
		num = int(x[i][j])
		if minimum >= num:
			minimum = num
	print(minimum)
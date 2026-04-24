# By: cserrato.dev https://github.com/CSerratoDev
# Solution: 

from sys import stdin

from matplotlib.pylab import matrix

def readLine():
	return stdin.readline().strip()

def readInt():
	return int(readLine())

def readInts():
	return list(map(int, readLine().split()))

def main():
	matrix = []
	t = readInt() # cases
	for _ in range(t):
		n, m = readInts() # size of matrix
		b = readInts() # row sums
		matrix.append((n, m, b))
	print(matrix)
	
if __name__ == '__main__':
	main()
# By: cserrato.dev https://github.com/CSerratoDev
# Solution: O(1) Complexity

from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInt():
	return int(readLine())

def main():
	num = readInt()
	while True:
		num += 1
		if len(set(str(num))) == 4:
			print(num)
			break
if __name__ == '__main__':
	main()
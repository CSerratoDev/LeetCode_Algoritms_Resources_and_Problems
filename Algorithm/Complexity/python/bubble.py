import random
from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInt():
	return int(readLine())

def bubble(array):
	n = len(array)
	for i in range(n):
		for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n^2)
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
	return array

if __name__ == '__main__':
    print("size:")
	
    size_array = readInt()
	
    array = [random.randint(0,100) for i in range(size_array)]
    print(array)
    ranked_list = bubble(array)
    print(ranked_list)
import random
from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInt():
	return int(readLine())

def readInts():
	return list(map(int, readLine().split()))

def merge(array):
	if len(array) > 1:
		middle = len(array) // 2
		#Create lists
		left, right = array[:middle], array[middle:]
		#Recursive call
		merge(left)
		merge(right)
		#Iterators
		i, j, k = 0, 0, 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				array[k] = left[i]
				i += 1
			else:
				array[k] = right[j]
				j += 1
			k += 1
		while i < len(left):
			array[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			array[k] = right[j]
			j += 1
			k += 1
	return array

if __name__ == '__main__':
    print("size:")
    size_array = readInt()
    array = [random.randint(0, 100) for i in range(size_array)]
    print(array)
    print('-' * 20)
    list_merge = merge(array)
    print(list_merge)
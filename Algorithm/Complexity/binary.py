import random 
from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInt():
	return int(readLine())

def binary(array, start, end, objective):
    print(f'Finding {objective} between {array[start]} and {array[end - 1]}')
    if start > end:
        return False
    
    middle = (start + end)//2
    
    if array[middle] == objective:
        return True
    elif array[middle] < objective:
        return binary(array, middle + 1, end, objective)
    else: 
        return binary(array, start, middle - 1, objective)

if __name__ == '__main__':
    print("size:")
    size_array = readInt()
    print("objective:")
    objective = readInt()
    
    array = sorted([random.randint(0, 100) for i in range(size_array)])

    number = binary(array, 0, len(array), objective)
    print(array)
    print(f'Element {objective} {"IF it's here" if number else "It's NOT here"} in the list')
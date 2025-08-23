import random
from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInt():
	return int(readLine())

def linear(array, objective):
    match = False

    for i in array: # O(n)
        if i == objective:
            match = True
            break
    return match

if __name__ == '__main__':
    print("size:")
    size_array = readInt()
    print("objective:")
    objective = readInt()
    
    array = [random.randint(0, 100) for i in range(size_array)]

    number = linear(array, objective)
    print(array)
    print(f'Element {objective} {"IF it's here" if number else "It's NOT here"} in the list')
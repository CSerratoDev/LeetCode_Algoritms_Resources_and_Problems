#Numpy is a fundamental Python library for scientific computing.
#It allows the creation and manipulation of multidimensional arrays.
#In addition, it offers a wide range of mathematical and statistical functions.

import numpy as np

# Create a 1D array
data = [1, 2, 3]
array1d = np.array(data)
print(f"1D Array: \n{array1d}")
# Create a 2D array
data2 = [[1, 2], [3, 4]]
array2d = np.array(data2)
print(f"2D Array: \n{array2d}")
# Create a 3D array
data3 = [[[1,2,3], [4,5,6],[7,8,9]],
        [[1,2,3], [4,5,6],[7,8,9]],
        [[1,2,3], [4,5,6],[7,8,9]]]
array3d = np.array(data3)
print(f"3D Array: \n{array3d}")

# Functions to create arrays
# Create an array of zeros
z = np.zeros((2,3)) # 2 rows, 3 columns
print(f"Array of Zeros: \n{z}")
# Create an array of ones
o = np.ones((2,3,4)) # 2 rows, 3 columns, 4 depth
print(f"Array of Ones: \n{o}")
# Create an array of random numbers 
r = np.full((3,4), 7) # Fill with the number 7
print(f"Array of Random Numbers: \n{r}")

# Create an array based on a range
array_range = np.linspace(1, 10, 4) # 1 is minimum, 10 is maximum, 4 is number of elements
print(f"Array based on a range: \n{array_range}")
# Create an array based on a range with a step
array_range2 = np.arange(9) # 0 is minimum, 9 is maximum, step is 1
print(f"Array based on a range with a step: \n{array_range2}")
# Create an array based on a range with a step with a specified minimum, maximum, and step
array_range3 = np.arange(1, 11, 2) # 1 is minimum, 11 is maximum, step is 2
print(f"Array based on a range with a step: \n{array_range3}")
# Initialize an array with random values 
array_random = np.random.rand(2, 3, 2) # 2 rows, 3 columns, 2 depth
print(f"Array with Random Values: \n{array_random}")
# Initialize an array with random values with an normal distribution
array_random2 = np.random.randn(2, 4) # 2 rows, 4 columns
print(f"Array with Random Values (Normal Distribution): \n{array_random2}")
"""
import matplotlib.pyplot as plt # Importing matplotlib for plotting
m = np.random.randn(1000000) # Generate 1 million random values from a normal distribution
plt.hist(m, bins=200) # Histogram of the random values
plt.show() # Display the histogram
"""
# Caracteristics of arrays
array = np.array([[1, 2, 3], [4, 5 , 6], [7, 8, 9]]) # Create a 2D array
print(f"Array: \n{array}") # Display the array
print(f"ndim: {array.ndim}") # Number of dimensions of the array
# Each dimension is called an axis
# The number dimensions is called the rank of the array
print(f"Shape: {array.shape}") # Shape of the array corresponds longitude of each axis
print(f"Size: {array.size}") # Number of elements in the array
print(f"Data Type: {array.dtype}") # Data type of the array


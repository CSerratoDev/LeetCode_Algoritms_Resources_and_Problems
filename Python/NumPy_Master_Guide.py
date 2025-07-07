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
z = np.zeros((2,3))                         #2 rows, 3 columns
print(f"Array of Zeros: \n{z}")
# Create an array of ones
o = np.ones((2,3,4))                        #2 rows, 3 columns, 4 depth
print(f"Array of Ones: \n{o}")
# Create an array of random numbers 
r = np.full((3,4), 7)                       #Fill with the number 7
print(f"Array of Random Numbers: \n{r}")

# Create an array based on a range
array_range = np.linspace(1, 10, 4)                                 #1 is minimum, 10 is maximum, 4 is number of elements
print(f"Array based on a range: \n{array_range}")
# Create an array based on a range with a step
array_range2 = np.arange(9)                                         #0 is minimum, 9 is maximum, step is 1
print(f"Array based on a range with a step: \n{array_range2}")
# Create an array based on a range with a step with a specified minimum, maximum, and step
array_range3 = np.arange(1, 11, 2)                                  #1 is minimum, 11 is maximum, step is 2
print(f"Array based on a range with a step: \n{array_range3}")
# Initialize an array with random values 
array_random = np.random.rand(2, 3, 2)                  #2 rows, 3 columns, 2 depth
print(f"Array with Random Values: \n{array_random}")
# Initialize an array with random values with an normal distribution
array_random2 = np.random.randn(2, 4)                   #2 rows, 4 columns
print(f"Array with Random Values (Normal Distribution): \n{array_random2}")
"""
import matplotlib.pyplot as plt # Importing matplotlib for plotting
m = np.random.randn(1000000) # Generate 1 million random values from a normal distribution
plt.hist(m, bins=200) # Histogram of the random values
plt.show() # Display the histogram
"""
# Caracteristics of arrays
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) #Create a 2D array
print(f"Array: \n{array}")                          #Display the array
print(f"ndim: {array.ndim}")                        #Number of dimensions of the array
# Each dimension is called an axis
# The number dimensions is called the rank of the array
print(f"Shape: {array.shape}")      #Shape of the array corresponds longitude of each axis
print(f"Size: {array.size}")        #Number of elements in the array
print(f"Data Type: {array.dtype}")  #Data type of the array

# Manipulate or filter data of array
array_1d = np.arange(1, 10, 1)              #Create a 1D array
print(f"Array one-dimensional: {array_1d}") 
print(f"index: {array_1d[5]}")              #index
print(f"slicing [n:n] {array_1d[2:4]}")     #slicing, 2 is index inclusive, 4 is index exclusive, start, stop, step
print(f"slicing [n:] {array_1d[4:]}")       #No limit indicated in stop only start
print(f"slicing [n::n] {array_1d[0::3]}")   #slicing with start, stop, step

array_2d = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])    #Create a 2D array
print(f"Array two-dimensional \n{array_2d}")
print(f"Indexing for column [n,n] {array_2d[0,2]}")     #row, column
print(f"Indexing for rows [n:] {array_2d[2:]}")         #index for rows
print(f"Indexing combine [n:n, n] {array_2d[0:3, 2]}")  #Is a way to combine row slicing and column selection in a array.

# Indexing with slices
print(f"[:n,n:] \n{array_2d[:2,1:]}")    # Selects rows 0 and 1, columns from index 1 to end
print(f"[n] {array_2d[2]}")              # Selects the entire row at index 2
print(f"[n, :] {array_2d[2, :]}")        # Selects all columns in row at index 2
print(f"[n:, :] {array_2d[2:, :]}")      # Selects rows from index 2 to end, all columns
print(f"[:, :n] \n{array_2d[:, :2]}")    # Selects all rows, columns 0 and 1
print(f"[n, :n] {array_2d[1, :2]}")      # Selects columns 0 and 1 from row at index 1
print(f"[n:n, :n] {array_2d[1:2, :2]}")  # Selects row 1 only, columns 0 and 1 (returns a 2D array)

# Change of array dimensions and lengths
d = np.arange(12)                #Create a 1D array with 12 elements
print(f"Shape: {d.shape}")       #Print the shape of the array
print(f"Array after shape: {d}") #Print the array

d.shape = (4, 3)                            #Reshape the array to 4 rows and 3 columns
print(f"Array after Shape (n, n): \n{d}")   #Print the reshaped array

# Modifications in one array will modify another array (views share data)
e = d.reshape(3, 4)                         #Reshape d to 3 rows and 4 columns (creates a view)
print(f"Array after reshape: {e.shape}")    #Print the shape of e
print(f"Array e: \n{e}")                    #Print the reshaped array e

e[0, 1] = 20                                        #Modify an element in e
print(f"Array after modifications in e: \n{e}")     #Print e after modification
print(f"Comparation with d \n{d}")                  #Show that d is also modified (since e is a view)

# Unwrap the array, returning a new single-dimensional array
print(f"Array new: {d.ravel()}")
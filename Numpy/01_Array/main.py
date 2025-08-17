# There are 3 types of Arrays in Numpy
# 1- 1D Array
# 2- 2D Array
# 3- 3D Array

import numpy as np

# Demonstration of 1D Array
one_d_array = np.array([1, 2, 3, 4, 5])
print(f"1D Array: {one_d_array}")

# Demonstration of 2D Array
# In 2D Array, we have rows and columns

two_d_array = np.array([[1, 2, 3], [4, 5, 6],  [7,8,9]])
                        # Row        # Column
print(f"2D Array:\n{two_d_array}")

# Demonstration of Multi-D Array / Matrix / 3D-Array 
# In 3D Array, we have multiple 2D arrays stacked together
# They are almost similar to 2D array 

three_d_array = np.array([[1,2,3], [5,6,7], [12,56,81]])
print(f"Three D Array:\n{three_d_array}")

# Creation of Array

# Method 1:
# from python List 
# Syntax 
lst = [1,2,3], [5,6,7]
np_lst = np.array([lst])
print(f"Array created by Python List:\n {np_lst}")

# Creating 2D array from Python list
a = [10,25,36]
b = [15,62,28]
arr = np.array([a,b])
print( f"Created 2D array from python list: \n{arr}")

# Method 2:
# From Default Values

zero_arr = np.zeros((3, 4))  # Creates a 3x4 array filled with zeros
print(f"Array of Zeros:\n{zero_arr}")

one_arr = np.ones((2, 3))  # Creates a 2x3 array filled with ones
print(f"Array of Ones:\n{one_arr}")

two_arr = np.full((2, 2), 2)  # Creates a 2x2 array filled with the value 2
print(f"Array of Twos: \n{two_arr}")


# Creating sequence of Numbers

seq_arr = np.arange(0, 10, 2)  # Creates an array with values from 0 to 10 with a step of 2
print(f"Array with Sequence of Numbers:\n{seq_arr}")

# Creating Identity Matrix

identity_matrix = np.eye(3)  # Creates a 3x3 identity matrix
print(f"Identity Matrix:\n{identity_matrix}")
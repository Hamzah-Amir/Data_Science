# There are multiple attributes that we can use to identify properties of Arrays

# 1- Shape Attribute
# 2- Size Attribute
# 3- ndim Attribute
# 4- dtype Attribute

# Demontsration of shape attribute

import numpy as np
arr = np.array([[1,2,3],
                [4,5,6]])
print(f"Shape of the array is: {arr.shape}")  # Output: (2, 3)

# Demonstration of size attribute
# Using same array as above
print(f"Size of the array is: {arr.size}")  # Output: 6

# Demonstration of ndim attribute
# Using same array as above
print(f"Number of dimensions in this array are: {arr.ndim}")

# Demonstration of dtype attribute
dtype_array = np.array([20,30,40.5])
print(f"Data type of the array is: {dtype_array.dtype}") # Output: int64 (or int32 depending on the system)

# Changing type of array using astype method
new_dtype_array = dtype_array.astype(int)
print(new_dtype_array)
print(f"New data type of the array is: {new_dtype_array.dtype}")  # Output: int64
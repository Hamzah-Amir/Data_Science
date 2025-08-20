# In Numpy it is essential to handle missing values to handle error or crashing 
# There are 3 most used methods used for handling these

# 1- isnan()
# 2- nan)to_num
# 3- isinf

import numpy as np
# Demonstration of isnan
arr = np.array([0,
1,2,np.nan,4,5,np.nan,7])
print(np.isnan(arr))

# Demonstration of nan_to_num
# It is used when a missing value is found or filled in the array 
arr = np.nan_to_num(arr, nan=3)
print(arr)

# Demonstration of ininf
# It is used to check if an infinite value presents in array
print(np.isinf(arr))
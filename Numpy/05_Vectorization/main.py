# Vectorization is a process of applying an operation on entire array without using loops
# It is same as broadcasting including both syntax and work

import numpy as np

arr1 = np.array([1,2,3,4,8,12])
arr2 = np.array([88,60,16,32,51, 56])
result = arr1 + arr2

print(result)
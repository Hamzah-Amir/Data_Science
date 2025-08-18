# Operators in Numpy

import numpy as np
arr = np.array([10, 20, 30, 40, 50])

# Arithmetic Operations
print("Arithmetic Operations :")
print("Addition :", arr + 5)          # Output: [15 25 35 45 55]
print("Subtraction :", arr - 5)       # Output: [ 5 15 25 35 45]
print("Multiplication :", arr * 2)    # Output: [20 40 60 80 100]
print("Division: ", arr / 2)          # Output: [5 10 15 20 25]
print("Exponential: ", arr ** 2)      # Output: [100 400 900 1600 2500]
print("Floor Division: ", arr // 2)   # Output: [5 10 15 20 25]
print("Modulus: ", arr % 2)           # Output: [0 0 0 0 0]
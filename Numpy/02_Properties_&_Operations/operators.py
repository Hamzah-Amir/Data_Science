# Operators in Numpy

import numpy as np
arr = np.array([10, 20, 30, 40, 50])

# Demonstration of Arithmetic Operations
print("Arithmetic Operations :")
print("Addition :", arr + 5)          # Output: [15 25 35 45 55]
print("Subtraction :", arr - 5)       # Output: [ 5 15 25 35 45]
print("Multiplication :", arr * 2)    # Output: [20 40 60 80 100]
print("Division: ", arr / 2)          # Output: [5 10 15 20 25]
print("Exponential: ", arr ** 2)      # Output: [100 400 900 1600 2500]
print("Floor Division: ", arr // 2)   # Output: [5 10 15 20 25]
print("Modulus: ", arr % 2)           # Output: [0 0 0 0 0]

# Demonstration of Aggregration functions
print("\nAggregation Functions :")
print("Sum: ", np.sum(arr))            # Output: 150
print("Mean: ", np.mean(arr))          # Output: 30.0
print("Median: ", np.median(arr))      # Output: 30.0
print("Standard Deviation: ", np.std(arr))  # Output: 14.142135623730951
print("Variance: ", np.var(arr))       # Output: 200.0
print("Minimum: ", np.min(arr))        # Output: 10
print("Maximum: ", np.max(arr))        # Output: 50
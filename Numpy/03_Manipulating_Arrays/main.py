# We can add remove or split items in array using follwing commands
# 1- insert()
# 2- append() (used to add element in last of array)
# 3- concatinate() (Used to add to arrays)
# 4- delete() (Used to delete an element from array)
# 5- vstack() (Used to vertically stack arrays)
# 6- split() (Used to split array into equal parts)
# 2- hsplit() (To horizontally split array)
# 7- vsplit() (To vertically split arrays)


# Note is doesnot change original array but create a new array

# Demonstration of insert Function

import numpy as np
arr = np.array([1,2,3])
arr = np.insert(arr, 3, 4, axis=None)
print(arr)

# Inserting element in 2D array

array_2d = np.array([[1,2], [3,4]])
np.insert(array_2d, 2, [5,6], axis=0)
print(array_2d)

# Demonstration of append function

arr = np.append(arr, [5,6])
print(arr)

# Demonstration of concatenate function
arr2 = np.array([7,8,9])
array = np.concatenate((arr, arr2), axis=0)
print(array)

# Demonstration fo delete function

array = np.delete(array,8,axis=0)
print("Deleting element from array",array)

# Demonstration of hstack

arr_1 = np.array(["a","b",'c'])
arr_2 = np.array(["d","e","f"])
stack_arr = np.hstack((arr_2, arr_1))
print(stack_arr)

# Demonstration of vstack

stack_arr = np.vstack((arr_1, arr_2))
print(stack_arr)

# Demonstration of split()
print(np.split( "Equally splitted array",stack_arr,2))

# Demonstration of vstack

print(np.vsplit(stack_arr, (2,3)))

# Demonstration of hstack

print(np.hsplit(stack_arr, (2,3)))
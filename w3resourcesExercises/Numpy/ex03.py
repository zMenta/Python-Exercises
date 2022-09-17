import numpy as np


array = np.array([5, 9, 0, 2])
array2 = np.array([2, 6, 1, 8])


# np.all verifies with all values in the array are True
# Definition: Test whether all array elements along a given axis evaluate to True.

# 0 is considered False

print(np.all(array))
print(np.all(array2))

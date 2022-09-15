import sys
import math

# array_size = sys.stdin.readline()
# array = sys.stdin.readline()

array_size = 4
# array = [10, 12, 14, 16]

array_size = 11
array = [2, 5, 9, 20, 14, 6, 8, 1, 24, 30, 8]

array = [2, 5, 9, 20, 14, 8, 1, 24, 30, 8]
arrayD  = [8, 5, 9, 20, 8, 14, 1, 24, 30, 2]

if len(array) % 2 == 0:
    array_half_size = int(len(array) / 2) - 1
else:
    array_half_size = math.ceil(len(array) / 2) - 1
    

for i in range(array_size):
    """organize array"""
    
    if array[i] % 2 == 0 and array[-1-i] % 2 == 0:
        array[i], array[-1-i] = array[-1-i], array[i]
        
    if i == array_half_size:
        break

for num in array:
    """Print output array"""
    print(num, end=" ")

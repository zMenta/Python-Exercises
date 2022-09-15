import sys

# array_size = sys.stdin.readline()
# array = sys.stdin.readline()

array_size = 5
array = [10, 10, 20, 20, 30, 30]

lowest_sum = sum[array]
highest_sum = array[0]


for i in range(len(array)):
    current_sum = 0
    for j in range(len(array)):
        if i == j:
            continue
            
        current_sum += array[j]
    
    print(current_sum)
    
    if current_sum > highest_sum:
        highest_sum = current_sum
    
    if current_sum < lowest_sum:
        lowest_sum = current_sum

# print(highest_sum, end=' ')
# print(lowest_sum)
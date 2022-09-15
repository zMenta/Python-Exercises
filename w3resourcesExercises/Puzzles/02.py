# 1. Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.

array1 = [19, 19, 15, 5, 3, 5, 5, 2]
array2 = [19, 15, 15, 5, 3, 3, 5, 2]
array3 = [19, 19, 5, 5, 5, 5, 5]


def verify_list(array: list):
    nineteen_counter = 0
    five_counter = 0

    for num in array:
        if num == 19:
            nineteen_counter += 1
        elif num == 5:
            five_counter += 1

    if nineteen_counter == 2 and five_counter >= 3:
        return True

    return False


print(verify_list(array1))
print(verify_list(array2))
print(verify_list(array3))

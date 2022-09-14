# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def verify_number(number: int):
    """Validates a number sequence if there are any number that repeat itself.

    Args:
        number (int): Number sequence to validate

    Returns:
        bool: Returns True if a number in the sequence repeat itself.
    """
    string_number = str(number)
    number_size = len(string_number)
    counter = 0

    for current_number in string_number:
        counter += 1
        for i in range(counter, number_size):
            if string_number[i] == current_number:
                return True
            
    return False


print(verify_number(1406908))
print(verify_number(1956))

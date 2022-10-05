
array = [1, 30, 1, 2]

# array = [10, 5, 3]

def main():

    profit = 0
    for i in range(len(array)):
        if array[i] < array[i+1]:
            profit += array[i+1] - array[i]
            
        i += 1
        
        if i == len(array) - 1:
            break
        
    print(profit)


if __name__ == "__main__":
    main()
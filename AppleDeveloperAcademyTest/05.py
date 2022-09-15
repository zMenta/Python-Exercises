
array = [0, 1, 1, 1]
array = [1, 1]

moves_array = [-1] * len(array)


for i in range(len(array)):
    current_moves = 0 
    
    for j in range(len(array)):
        if array[j] != 0:
            current_moves += abs(j - i)

    moves_array[i] = current_moves
    

for moves in moves_array:
    print(moves, end=" ")
        
        


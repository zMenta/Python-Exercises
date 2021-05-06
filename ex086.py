#In one list make a 3x3 grid and fill the spaces of the grid using user answers. Show the user the corresponding values typed for the grid.

#grid = [[1,2,3],[4,5,6],[7,8,9]] Grid example 

grid = [[], [], []]

"""
For organization and understanding

[0,0] [0,1] [0,2]

[1,0] [1,1] [1,2]

[2,0] [2,1] [2,2]
"""
for row in range(3):
    for column in range(3):
        grid[row].append(int(input(f"Please type an number to fill the grid space {row},{column} :")))

print("="*60)
print(grid[0])
print(grid[1])
print(grid[2])

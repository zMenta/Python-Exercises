# ex087 + a) The sum of all even numbers typed. B) The sum of all numbers of the column index 2 
# C) the biggest value typed in the row index 2

grid = [[], [], []]
even_sum = 0
column_sum = 0

for row in range(3):
    for column in range(3):
        number = (int(input(f" Type an integer number for the {row} , {column} position: ")))
        grid[row].append(number)

        if number%2 == 0:
            even_sum += number
        
        if column == 2:
            column_sum += number

print("-"*40)
for i in range(3):
    print(grid[i])
print("-"*40)
print(f"The sum of the even numbers are: {even_sum}")
print(f"The sum of the column 2 is: {column_sum}")
print(f"The highest number of the row 2 is: {max(grid[2])}")
print("-"*40)

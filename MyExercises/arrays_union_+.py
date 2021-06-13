
x = [3,8,4,2,1,6,8,7,11,9]
y = [2,1,5,12,3,0,1,4,5,6]

# function to make the union of arrays x and y.
def union(x,y):
    u = [] #Union list containing the union of x with y.

    for i in x:
        if i not in u:
            u.append(i)

    for i in y:
        if i not in u:
            u.append(i)

    print(u)

union(x,y)

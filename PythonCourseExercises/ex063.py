#Fibonacci

c = 0
num = 7
fiba = [0,1]

num = int(input("Please type how many items to show:"))

while c != num:
    print(fiba[-1])
    result = fiba[-1] + fiba[-2]
    fiba.append(result)
    
    c += 1
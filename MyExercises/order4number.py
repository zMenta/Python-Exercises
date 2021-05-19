#order numbers a,b,c,d. Lowest to highest 

a = int(input("Type a number A: "))
b = int(input("Type a number B: "))
c = int(input("Type a number C: "))
d = int(input("Type a number D: "))

while(a > b or b > c or c > d):

    if a > b:
        a, b = b, a

    if b > c:
        b, c = c, b

    if c > d:
        c, d = d, c
    
print(f"{a},{b},{c},{d}")

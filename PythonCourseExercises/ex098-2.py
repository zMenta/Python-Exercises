
from time import sleep

def count(s, e , p):  #s = start | e = end | p = pace
    print(f"Start: {s} | End: {e} | Pace: {p}")
    
    if p == 0:
        p = 1

    if p < 0:
        p *= -1

    num = s  
    if s < e:
        while num <= e:
            print(f"{num} ",end="", flush=True)
            sleep(0.12)
            num += p
    else: 
        while num >= e:
            print(f"{num} ",end="", flush=True)
            sleep(0.12)
            num -= p
        

#Main Body 
count(0,100,10)
print()
print("-"*50)
count(100,0,10)
print()
print("-"*50)
count(10,0,-3)
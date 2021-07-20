#Create a title function 

def title(msg):
    sz = len(msg) #sz = size
    sz += 4

    print("~"*sz)
    print(f"{'':2}{msg}")
    print("~"*sz)


#Main Body
title("carl")
title("Bob magnoson")

#Create a function that reads an indetermined numbers of grades. Then return a dictionary containing the amount of grades listed, the highest grade, the lowest and the average of the grades. And an optional "situation" parameter, if true return the situation of the class, "bad,average,good".

def grade(*g, situ=False):
    '''
    Function that reads a lot of grades and reuturn a dictionary.
    :param: g -> grade
    :param: situ -> Situation *If situation is True, will add to the dictionary a situation key and value of bad,average or good class situation.
    '''
    # i = Index | v = value
    for i,v in enumerate(g): 
        #First value is the biggest and lowest value.
        if i == 0:
            #hi = highest value
            #lw = lowest value
            hi = v
            lw = v
        else:
            #First if to indentify the highest number, second one to the lowest number.
            if hi < v:
                hi = v
            
            if lw > v:
                lw = v
        
        #resu = result
        resu = {
        "quantity": len(g),
        "high": hi,
        "low": lw,
        "average": (sum(g)/len(g))
    }

    #Analyses if situation is True and apply the corresponding situation of the class. "bad","average" or "good"
    if situ == True:
        if resu["average"] < 6:
            resu.update({"situation": "bad"})
        elif resu["average"] < 8:
            resu.update({"situation": "average"})
        else: 
            resu.update({"situation": "good"})

    return resu


#Main Body
a = grade(10,8,8,situ=False)
print(a)


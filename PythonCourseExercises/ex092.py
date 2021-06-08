#Work permit reader. Read the data about a person and says how many years she/he will retire (considering of 35 years of contribution).

from datetime import  date
this_year = date.today().year

wp = {} # wp = work permit

#adding info in the work permit 
wp["name"] = str(input("Please type your name: "))
wp["age"] = this_year - int(input("Please type the year that you're born."))
wp["id"] = int(input("Please type you Work Permit ID (0 if you don't have one): "))

if wp["id"] != 0:
    wp["retire"] = this_year - int(input("The year that you started working: "))
    wp["retire"] += 35
    wp["salary"] = int(input("Please digit your salary $"))
    
print("-"*30)

for key,value in wp.items():
    print(f"{key} is {value}")
    
print("-"*30)

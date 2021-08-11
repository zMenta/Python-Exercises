#Create a function that has the year of birth as a parameter. Inform the user if his vote is optional,denied or mandatory.

from datetime import date


#Functions

def vote(birth):
    """
    param: birth = year of birth

    *Uses datetime -> date.*

    Function to return the status of vote, depending on the age of the person.
    <16 denied, <18 optional, <60 mandatory, >60 optional.
    """
    age = date.today().year - birth
    
    print(f"With {age} years: VOTE - ", end="")
    if age < 16:
        print("DENIED")
    elif age < 18 or age > 60:
        print("OPTIONAL")
    elif age < 60:
        print("MANDATORY")      
#Main Body

vote(1988)
vote(2005)
vote(2008)
vote(1967)
vote(1984)
vote(1950)
vote(2004)


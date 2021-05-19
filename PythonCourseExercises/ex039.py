#Alistamento 

#DEBUG
"""
todaydate = datetime.date.today()

print("{}".format(todaydate))

ano = datetime.date(2001,1,1)

print("{}".format(ano))

print(todaydate.year - ano.year)

"""

import datetime

birth = int(input("Por favor digite o seu ano de nascimento:"))


TODAY = datetime.date.today()
birth = datetime.date(birth,1,1)

age = TODAY.year - birth.year

if age < 18:
    print("Você precisa se alistar em {} anos. Você tem {} anos.".format(18-age, age))
elif age > 18:
    print("Você deixou passar o alistamento e está atrasado por {} anos. Você tem {} anos.".format(age-18, age))
else:
    print("Você precisa se alistar, você tem {} anos".format(age))


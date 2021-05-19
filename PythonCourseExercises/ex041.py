#Calculador de fachetária de nadador

import datetime

birth = int(input("Please type your year of birth."))

TODAY = datetime.date.today()
birth = datetime.date(birth,1,1)
age = TODAY.year - birth.year

if age <= 9:
    print("Você tem {} anos, e pertence a categoria MIRIM".format(age))
elif age <= 14:
    print("Você tem {} anos, e pertence a categora INFANTIL".format(age))
elif age <=19:
    print("Você tem {} anos, e pertence a categora JUNIOR".format(age))
elif age <=20:
    print("Você tem {} anos, e pertence a categora SÊNIOR".format(age))
else:
    print("Você tem {} anos, e pertence a categora MASTER".format(age))


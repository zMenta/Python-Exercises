#Leitor de pessoas
#Mostra o homem mais velho, mulher abaixo de 20 anos e a média de todas as idades.

young = 0
age_total = 0
oldest = 0
rang = 4

for c in range(0,rang):
    people = (input("Please type your Sex(M or F) and How old you are. Separate by commas. Example: F,19:")).replace(" ", "").upper()
    people = people.split(",")
    age = int(people[1])
    age_total += age

    if people[0] == "M" and age > oldest:
        oldest = age

    if people[0] == "F" and age < 20:
        young += 1

average = age_total / rang

print("""

De todas as pessoas a média de suas idades é {:.1f} anos.

O homem mais velho do grupo possue {} anos.

E {} mulhere(s) têm menos de 20 anos.

""".format(average, oldest, young))
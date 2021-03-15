#Contador de A 

word = input("Type anything: ").strip()

print("There is {} A's.".format(word.upper().count("A")))
print("The first A appears in the {}nd position.".format(word.upper().find("A")+1))
print("The last A appears in the {}nd postiion.".format(word.upper().rfind("A")+1))
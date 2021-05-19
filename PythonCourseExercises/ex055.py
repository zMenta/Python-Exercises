#Leitor de pesos de 5 pessoas.

heavy = 0 
light = 0

for c in range(0,5):
    value = int(input("Please type your weight:"))
    if value > heavy:
        heavy = value
    if value > -light:
        light = value

print("\nThe person who is heaviest weights {}, and the lightest weights {}.\n".format(heavy, light))
   

## Sua cidade começa com o nome santo?

city = input("Digite o nome de uma cidade: ").strip()


#First Method using split

#split_city = city.split()
#santo = split_city[0].upper()
#print(santo.find("SANTO"))

# IF returns -1 , means that the word "SANTO" is not found.


#Second method

print("Sua cidade começa com o nome 'Santo': {}".format(city[0:5].upper() == "SANTO"))
#Bus ticket calculator 

km = int(input("Please type the distance in KM of your travel:"))

if km <= 0:
    print("Invalid KM")
elif km <= 200:
    print("It will cost {}$ for a ticket, for a {}km travel.".format(km*0.50, km))
else:
    print("It will cost {}$ for a ticket, for a {}km travel.".format(km*0.45, km))

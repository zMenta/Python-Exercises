#lista de preços 

products = ("Pen", 2.40, "Chicken", 7.50, "Bread", 3.75, "Pancakes", 2.75, "Computer", 874.85)

print("="*50)
print("{:^50}".format("PRICE LIST"))
print("="*50)

c = 0

while c in range(0,len(products)):
    print(f"{products[c]:.<50}", end="")
    c += 1
    print(f"R$ {products[c]:>7}")
    c += 1

    if c == 7:
        break

print("="*50)
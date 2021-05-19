#Police Guy

km = int(input("You scan the car velocity of an car.And you scan for km/h:"))

if km < 0:
    print("Well, that don't seen right. This device must be broken")
elif km <= 80:
    print("This car is inside the speed limit.")
elif km >= 300:
    print("Is that a speed demon?")
else:
    print("This car is over the speed limit. And I should stop him and charge a ${:.2f} ticket.".format((km-80)*7))

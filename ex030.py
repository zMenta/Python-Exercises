#Even or Odd number

num = int(input("Type a whole number:"))

result = num % 2

if result == 0:
    print("{} is an even number.".format(num))
else:
    print("{} is an odd number.".format(num))
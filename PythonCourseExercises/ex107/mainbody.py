from package import calculations 

value = 100
percen = 80

print(f"Half price of {value}: {calculations.halfValue(value)}")
print(f"Double price of {value}: {calculations.doubleValue(value)}")
print(f"Increase price of {value} by {percen}%: {calculations.raiseValue(value,percen)}")
print(f"Lower price of {value} by {percen}%: {calculations.lowerValue(value,percen)}")

def halfValue(value):
    return value/2


def doubleValue(value):
    return value*2


def raiseValue(value, percentual=1):
    percentageValue = (value*percentual) /100
    return value + percentageValue

def lowerValue(value, percentual=1):
    percentageValue = (value*percentual) / 100
    return value - percentageValue

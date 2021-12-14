def halfValue(value, format=False):
    new_value =  value/2
    if format == True:
        new_value = money(new_value)
    return new_value


def doubleValue(value, format=False):
    new_value =  value*2
    if format == True:
        new_value = money(new_value)
    return new_value

def raiseValue(value, percentual=1, format=False):
    percentageValue = (value*percentual) /100
    new_value = value + percentageValue
    if format == True:
        new_value = money(new_value)
    return new_value


def lowerValue(value, percentual=1, format=False):
    percentageValue = (value*percentual) /100
    new_value = value - percentageValue
    if format == True:
        new_value = money(new_value)
    return new_value


def money(value):
    formatted_string = f"R${value:.2f}"
    return formatted_string

def summary(value, percen_raise=1, percen_lower=1):
    print("-"*40)
    print(f"{'SUMMARY OF THE VALUE':^40}")
    print("-"*40)
    print(f"{'BASE VALUE:':<20}{money(value):>20}")
    print(f"{'DOUBLE VALUE:':<20}{doubleValue(value,True):>20}")
    print(f"{'HALF VALUE:':<20}{halfValue(value,True):>20}")
    print(f"{percen_raise}{'% VALUE INCREASE:':<18}{raiseValue(value,percen_raise, True):>20}")
    print(f"{percen_lower}{'% VALUE DECREASE:':<18}{lowerValue(value,percen_raise, True):>20}")
    print("-"*40)


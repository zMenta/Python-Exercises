debts = [['Alex', 'Blake', '5'], ['Blake', 'Alex', '3'], ['Casey', 'Alex', '7'], ['Casey', 'Alex', '4'], ['Casey', 'Alex', '2']]

debts = [['Blake', 'Alex', '7'], ['Blake', 'Alex', '3'], ['Alex', 'Blake', '4'], ['Blake', 'Alex', '1'], ['Alex', 'Blake', '7']]

def smallestNegativeBalance(debts) -> list:
    persons = {}
    for i in range(len(debts)):
        if debts[i][0] not in persons:
            persons[debts[i][0]] = 0
    
    for i in range(len(debts)):
        debtor = debts[i][0]
        creditor = debts[i][1]
        value = int(debts[i][2])
        
        persons[debtor] -= value
        persons[creditor] += value
        
    in_debt = []
    maximum_debt = -1
    for person in persons:
        if persons[person] < maximum_debt:
            maximum_debt = persons[person]


    for person in persons:
        if persons[person] == maximum_debt:
            in_debt.append(person)


    if len(in_debt) == 0:
        in_debt.append("Nobody has a negative balance")
    
    print(persons)
    return sorted(in_debt) 
    
print(smallestNegativeBalance(debts))
#Empréstimo para comprar HOUSE

#Text Colors
colors = {
    "red":"\033[1;31m", 
    "normal":"\033[0;0;0m"
    }

#Title box
print("===="*20)
print("{:|<2}{}{:|>2}".format("","Empréstimo para sua Casa".center(76),"")) 
print("="*80)

price = float(input("Por favor digite o valor da casa que você pretende comprar."))
years = float(input("Digite em quantos anos você pretende pagar a casa."))
salary = float(input("Por fim, digite o seu salário."))

minimal = years * 12
mon_payment =  price / minimal

#Debug

print(mon_payment)
print(years*12)
print(salary*0.3)



if mon_payment >= salary*0.3:
    print("{}Empréstimo Inválido!{}".format(colors["red"], colors["normal"]))
else:
    print("="*80)
    print("{:|<2}{}{:|>2}".format("","Você terá que pagar ${:.2f} por mês durante {:.0f} anos.".format(mon_payment, years).center(76), ""))
    print("{:|<2}{}{:|>2}".format("","Obrigado por escolher nosso empréstimo.".center(76), ""))
    print("="*80)
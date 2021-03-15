#Tabuada V2

tab = int(input("Digite o número que você deseja ver a tabuada(1-10):"))

if tab < 1 or tab > 10:
    print("Tabuada Inválida")
else:
    print("\nTabuada do {} é :".format(tab))
    numtab = tab*10
    counter = 0
    for c in range(0,numtab+1,tab):
        if c > 0:
            counter += 1
            print("{:2} X {:2} == {:2}".format(counter, tab, c))
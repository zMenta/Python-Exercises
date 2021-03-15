#Progressão Aritimética

primeiro_termo = int(input("Digite o primeiro termo da PA:"))
razao = int(input("Agora digite a razão dessa mesma PA:"))

termos = primeiro_termo + (10*razao)
s = 0
for c in range(primeiro_termo, termos , razao):
    s += 1
    print("{:4} | {:2}".center(10).format(c, s))
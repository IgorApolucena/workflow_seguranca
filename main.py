print("(1)Dp. D.S \n (2)Dp. Marketing \n (3)Dp. Recursos Humanos \n (4)Dp. Pesquisa e Desenvolvimento")
print()

dp = str(input("Qual é o seu Dp?: "))
op = ["1","2","3","4"]

while (dp not in op):
    print()
    print("Opção errada! Digite novamente")
    print()
    print("(1)Dp. D.S \n (2)Dp. Marketing \n (3)Dp. Recursos Humanos \n (4)Dp. Pesquisa e Desenvolvimento")
    print()
    dp = str(input("Qual é o seu Dp?: "))

if (dp == "1"):
    print("Seu DP precisa de Laptops com alto desempenho")
elif (dp == "2"):
    print("Seu DP precisa de Tablets")
elif (dp == "3"):
    print("Seu DP precisa de DeskTops")
else:
    print("Seu DP precisa de equipamentos de última geração")

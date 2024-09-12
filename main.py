# Risco Pedido

val = dias = 0

def pedido(val,dias):
    val = float(input("Digite o valor do pedido: "))
    dias = int(input("Digite os dias para entrega: "))

    if (val < 100) or (dias > 7 ):
        print("Entrega normal")
    elif(val >= 100 and val <= 500) or (dias >= 4 and dias <= 7):
        print("Entrega prioritária")
    elif (val > 500) or (dias <= 4):
        print("Entrega urgente")
    else:
        print("Opção Inválida!")

pedido(val,dias)

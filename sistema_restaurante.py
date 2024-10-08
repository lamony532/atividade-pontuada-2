"""
Informe o número da turma: 
Turma - G93313

Nome completo dos componentes.
1 - lara de araujo
2 - lamony das merces silva
"""


import os

# Limpa o terminal.
os.system("cls || clear") 

#mostrando menu
print("""
pratos do dia:
1- macarrão(R$18)
2- lasanha(R$25)
3- batata recheada(R$22)
4- strogonoff(R$23)
5- risoto(R$30)
6- hamburguer(R$26)
7- camarão á milanesa(R$38)

""")

#declarando variáveis
precos = []
pratos = []
pagamento = 0
desconto = 0
total_final = 0
    
#fazendo pedido
while True:
    print("deseja fazer mais um pedido?")
    codigo_prato = int(input("digite o código do prato ou 0 para finalizar pedido:"))
    
    if codigo_prato == 0:
        break
    else:
        match(codigo_prato):
            case 1:
                precos.append(18)
                pratos.append("1-macarrao ")
            case 2:
                precos.append(25)
                pratos.append("2-lasanha ")
            case 3:
                precos.append(22)
                pratos.append("3-batata recheada ")
            case 4:
                precos.append(23)
                pratos.append("4-strogonoff ")
            case 5:
                precos.append(30)
                pratos.append("5-risoto ")
            case 6:
                precos.append(26)
                pratos.append("6-hamburguer ")
            case 7:
                precos.append(38)
                pratos.append("7-camarão á milanesa ")
            case _ :
                print("código de prato inválido, tente novamente")


#somando preços   
valor_total = sum(precos)

#calculando pagamento
while True:
    forma_pagamento = input("Escolha a forma de pagamento (1 - À vista, 2 - Cartão de crédito): ")
    if forma_pagamento == '1':
        desconto = valor_total * 0.10
        total_final= valor_total - desconto
        pagamento = "À vista"
        break
    elif forma_pagamento == '2':
        desconto = valor_total * 0.10
        total_final = valor_total + desconto
        pagamento = "Cartão de crédito"
        break
    else:
        print("Forma de pagamento inválida. Tente novamente")

#exibindo dados  
os.system("cls || clear")
print("====resumo da compra====")
print(f"subtotal:: R${valor_total}")
print(f"pratos pedidos: {pratos}")
print(f"Forma de pagamento: {pagamento}")
print(f"Valor do desconto ou acréscimo aplicado: R$ {desconto:.2f}")
print(f"Valor final a ser pago: R$ {total_final:.2f}")
    







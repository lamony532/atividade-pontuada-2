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
precos = []
pratos = []
    

while True:
    print("faça seu pedido!")
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


    
valor_total = sum_precos


print(f"valor sem acrésimo ou desconto: R${valor_total}")
print(f"pratos pedidos: {pratos}")

def calcular_total(total):
    forma_pagamento = input("Escolha a forma de pagamento (1 - À vista, 2 - Cartão de crédito): ")
    if forma_pagamento == '1':
        desconto = total * 0.10
        total_final = total - desconto
        return total_final, desconto, "À vista"
    elif forma_pagamento == '2':
        acrescimo = total * 0.10
        total_final = total + acrescimo
        return total_final, acrescimo, "Cartão de crédito"
    else:
        print("Forma de pagamento inválida. Considerando à vista por padrão.")
        desconto = total * 0.10
        total_final = total - desconto
        return total_final, desconto, "À vista"

# main.py
from cardapio import exibir_cardapio
from pedido import fazer_pedido
from pagamento import calcular_total

def main():
    cardapio = exibir_cardapio()
    pedido, total = fazer_pedido(cardapio)

    if pedido:
        print("\nSeu pedido:")
        for nome, preco in pedido:
            print(f"{nome} - R$ {preco:.2f}")

        print(f"\nSubtotal: R$ {total:.2f}")
        total_final, valor_modificacao, forma_pagamento = calcular_total(total)

        print(f"Forma de pagamento: {forma_pagamento}")
        print(f"Valor do desconto ou acréscimo aplicado: R$ {valor_modificacao:.2f}")
        print(f"Valor final a ser pago: R$ {total_final:.2f}")
    else:
        print("Nenhum pedido foi realizado.")

if __name__ == "__main__":
    main()






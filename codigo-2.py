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
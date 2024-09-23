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
01- macarrão(R$18)
02- lasanha(R$25)
03- batata recheada(R$22)
04- strogonoff(R$23)
05- risoto(R$30)
06- hamburguer(R$26)
07- camarão á milanesa(R$38)

""")

while codigo_prato != 0:
    codigo_prato = int(input("digite o código do prato ou 0 para finalizar pedido: "))
    precos = []
    match(codigo_prato):
        case 1:
            precos.append(18)
        case 1:
            precos.append(25)
        case 1:
            precos.append(22)
        case 1:
            precos.append(18)





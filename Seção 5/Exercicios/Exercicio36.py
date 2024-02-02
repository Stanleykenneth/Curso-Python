"""
36 - Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor.
     Para Calcular a comissão, considere a tabela abaixo:

     Venda mensal:                                                    Comissão:
     Maior ou igual a R$ 100.000,00                                   R$ 700,00 + 16% das vendas
     Menor que R$ 100.000,00 e ou maior ou igual R$ 80.000,00         R$ 650,00 + 14% das vendas
     Menor que R$ 80.000,00 e ou maior ou igual R$ 60.000,00          R$ 600,00 + 14% das vendas
     Menor que R$ 60.000,00 e ou maior ou igual R$ 40.000,00          R$ 550,00 + 14% das vendas
     Menor que R$ 40.000,00 e ou maior ou igual R$ 20.000,00          R$ 500,00 + 14% das vendas
     Menor que R$ 20.000,00                                           R$ 400,00 + 14% das vendas
"""

def calcular_comissao(venda_mensal):
    if venda_mensal >= 100000:
        comissao = 700 + 0.16 * venda_mensal
    elif venda_mensal >= 80000:
        comissao = 650 + 0.14 * venda_mensal
    elif venda_mensal >= 60000:
        comissao = 600 + 0.14 * venda_mensal
    elif venda_mensal >= 40000:
        comissao = 550 + 0.14 * venda_mensal
    elif venda_mensal >= 20000:
        comissao = 500 + 0.14 * venda_mensal
    else:
        comissao = 400 + 0.14 * venda_mensal

    return comissao


def formatar_valor(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')


venda_mensal = float(input("Digite o valor da venda mensal:\n R$ "))

comissao = calcular_comissao(venda_mensal)

print(f"A comissão a ser paga é: {formatar_valor(comissao)}")

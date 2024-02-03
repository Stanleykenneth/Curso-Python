"""
05 - Faça um programa que peça para digitar 10 valores e some-os.
"""

qtd = 10
soma = 0
for n in range(1, qtd+1):
    num = int(input(f"Informe o valor {n}/{qtd} valor:\n "))
    soma = soma + num
print(f"A soma dos valores é {soma}")
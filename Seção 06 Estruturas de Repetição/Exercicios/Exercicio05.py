"""
05 - Faça um programa que peça para digitar 10 valores e some-os.
"""

qtd = 10
soma = 0
for n in range(1, qtd+1):
    num = float(input(f"Informe o sálario {n}/{qtd} valor:\n R$"))
    soma = soma + num
print(f"A soma dos salários é R${soma:.2f}")
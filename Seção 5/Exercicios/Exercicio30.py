"""
30 - Faça um programa que receba três números e mostre-os em ordem crescente.
"""
def ordenar_numeros(num1, num2, num3):
    numeros_ordenados = sorted([num1, num2, num3])
    return numeros_ordenados

num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))
num3 = int(input("Digite o terceiro número:\n"))

numeros_ordenados = ordenar_numeros(num1, num2, num3)
print(f"Números em ordem crescente: {numeros_ordenados}")
"""
06 - Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
     assim como a diferença entre eles.
"""

num1 = int(input("Digite o valor do primeiro número:\n"))
num2 = int(input("Digite o valor do segundo número:\n"))

if num1 > num2:
    print(f"O primeiro número {num1} é maior que o segundo número {num2} e sua diferença é {num1 - num2}")
else:
    print(f"O Segundo número {num2} é maior que o Primeiro número {num1} e sua diferença é {num2 - num1}")
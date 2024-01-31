"""
07 - Faça um programa que receba dois números e mostre o maior.
     Se por acaso, os dois números forem iguais, imprima a mensagem Números iguais.
"""

num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

if num1 > num2:
    print(f"O primeiro número {num1} é maior que o Segundo número {num2}")
elif num2 > num1:
    print(f"O segundo número {num2} é maior que o primeiro numero {num1}")
else:
    print("Os números são iguais!")
"""
12 - Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido".
     Se for positivo, calcular o logaritmo deste número.
"""

import math

numero = int(input("Digite um número inteiro:\n"))
if numero < 0:
    print("Número inválido")
else:
    log_numero = math.log10(numero)
    print(f"O logaritmo de {numero} é {log_numero}")
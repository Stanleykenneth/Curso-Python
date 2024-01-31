"""
03 - Leia um número Real. Se o número for positivo imprima a raiz quadrada.
     Do contrário imprima o número ao quadrado.
"""
import math

num = float(input('Digite um número:\n'))

if num > 0:
    raiz = round(math.sqrt(num))
    print(f"A raiz de {num} é {raiz}")
elif num < 0:
    quadrado = num * num
    print(f"O quadrado de {num} é {quadrado}")
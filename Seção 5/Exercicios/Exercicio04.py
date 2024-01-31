"""
04 - Faça um programa que leia um número e, caso ele seja positvo, calcule e mostre:
     . O número adigitado ao qudrado
     . A raiz quadrada do número digitado
"""
import math

num = float(input("Digite um número:\n"))

if num > 0:
   raiz = round(math.sqrt(num))
   print(f"A raiz de {num} é {raiz}")
   print("")

   quadrado = num * num
   print(f"O número ao quadrado {num} é {quadrado}")
else:
    print("Número inválido. Digite um número Positivo!")
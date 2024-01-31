"""
11 - Escreva um programa que leia um número inteiro maior do que zero de evolva, na tela, a
     soma de todos os seus algarismos. Por exempl, ao número 251 coresponderá o valor 8(2 + 5 + 1).
     Se o número lido não for maior que zero, programa terminará com a mensagem "Número inválido".
"""

numero = int(input("Digite um número:\n"))

if numero <= 0:
    print("Número inválido!")
else:
    numero_str = str(numero)
    soma = sum(int(digito) for digito in numero_str)
    print(f"A soma dos algarismos de {numero} é {soma}")
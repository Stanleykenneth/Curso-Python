"""
02 - Escreva um programa que na tela, de 1 até 100, de 1 em 1, 2 vezes.
     A primeira ves deve usar a estrutura de repetiçao for, a segunda while.

"""
print("Loop for")
for num in range(1, 100+1):
    print(num ,'', end='')

print("")
print("")
print("Loop While")
numero = 1
while numero <= 100:
    print(numero,'', end='')
    numero = numero + 1

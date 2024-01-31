"""
18 - Faça um programa que mostre ao usuário um menu com 4 operações matemática (as básicas, por exemplo).
     O usuário escolhe umas das opções e o seu programa então pede dois valores e realiza a operação,
     mostrando o resultado e saindo.
"""

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
      return x / y
    else:
        return "divisão por zero não é permitida!"

print("Escolha a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Digite o número da operação desejada (1, 2, 3, ou 4):\n ")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if opcao == '1':
    resultado = soma(valor1, valor2)
    print(f"Resultado da soma: {resultado}")
elif opcao == '2':
    resultado = subtracao(valor1, valor2)
    print(f"Resultado da subtração: {resultado}")
elif opcao == '3':
    resultado = multiplicacao(valor1, valor2)
    print(f"Resultado da multiplicação: {resultado}")
elif opcao == '4':
    resultado = divisao(valor1, valor2)
    print(f"Resultado da divisão: {resultado}")
else:
    print("Opção inválida.")
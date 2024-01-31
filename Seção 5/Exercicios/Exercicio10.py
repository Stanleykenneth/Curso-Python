"""
10 - Faça um programa que receba altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
     utilizando as seguintes fórmulas(onde h corresponde a altura).

     Homens: (72.7 * h) - 58
     Mulheres: (62.1 * h) - 44.7

"""

h = float(input('Digite sua altura:\n'))
peso = float(input('Digite o seu peso:\n'))
sexo = input("Digite o seu sexo:\n")

imc = peso / (h ** 2)

if sexo == "masculino":
    if imc < 18.5:
        print(f"Seu imc é {round(imc, 2)}...Você está abaixo do peso.")
    elif 18.5 <= imc < 24.9:
        print(f"Seu imc é {round(imc, 2)}...Seu peso está normal.")
    elif 25 <= imc < 29.9:
        print(f"Seu imc é {round(imc, 2)}...Você está com sobrepeso.")
    else:
        print(f"Seu imc é {round(imc, 2)}...Você está obeso.")

elif sexo == "feminino":
    if imc < 18.5:
        print(f"Seu imc é {round(imc, 2)}...Você está abaixo do peso.")
    elif 18.5 <= imc < 24.9:
        print(f"Seu imc é {round(imc, 2)}...Seu peso está normal.")
    elif 25 <= imc < 29.9:
        print(f"Seu imc é {round(imc, 2)}...Você está com sobrepeso.")
    else:
        print(f"Seu imc é {round(imc, 2)}...Você está obeso.")




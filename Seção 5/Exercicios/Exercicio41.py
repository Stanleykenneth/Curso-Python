"""
41 - Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de
     acordo com a tablea abaixo:

     IMC:                        CLASSIFICAÇÃO:
     < 18.5                         Abaixo do peso
     18.5 - 24.9                    Saudável
     25.0 - 29.9                    Peso em excesso
     30.0 - 34.9                    Obesidade Grau I
     35.0 - 39.9                    Obesidade Grau II (severa)
     >= 40.0                        Obesidade Grau III (morbida)
"""


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        classificacao = "Saudável"
    elif 25.0 <= imc <= 29.9:
        classificacao = "Peso em excesso"
    elif 30.0 <= imc <= 34.9:
        classificacao = "Obesidade Grau I"
    elif 35.0 <= imc <= 39.9:
        classificacao = "Obesidade Grau II (severa)"
    else:
        classificacao = "Obesidade Grau III (mórbida)"

    return imc, classificacao

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))


imc, classificacao = calcular_imc(peso, altura)


print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")

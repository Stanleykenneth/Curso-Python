"""
19 - Faça um programa para verificar se um determinado número inteiro é divisivel por 3 ou por 5,
     mas não simultaneamente pelos dois.
"""

def verifica_numero(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "O Número é divisível por 3 e por 5."

    elif numero % 3 == 0:
        return "O Número é divisivel por 3."

    elif numero % 5 == 0:
        return "O Número é divisivel por 5."

    else:
        return "O número não divisível por 3 e nem por 5."

numero = int(input("Digite um número inteiro:\n"))
res = verifica_numero(numero)
print(res)
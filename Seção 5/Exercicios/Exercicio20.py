"""
20 - Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e,
     se forem, se é um triângulo escaleno, equilátero ou isóseles, considerando os seguintes conceitos:

     . O comprimento de cada lado de um triângulo é menor do que a soma dos outros lados.
     . Chama-se equilátero o triângulo que tem três lados iguais.
     . Denomina-se isósceles o triângulo que tem o comprimento de dois lados iguais.
     . Recebe o nome de escaleneo o triângulo que tem três lados diferentes.
"""

a = int(input("Digite o valor de A:\n"))
b = int(input("Digite o valor de B:\n"))
c = int(input("Digite o valor de C:\n"))

if (a < b + c) and (b < a + c) and (c < a + b):
    print("É Triângulo!")

elif (a == b) and (b == c):
    print("É Equilátero!")

elif (a == b) or (a == c) or (b == c):
    print("É Isósceles!")

elif (a != b) and (b != c) and (a != c):
    print("É Escaleno")
else:
    print("Estes valores não forma um triângulo!")
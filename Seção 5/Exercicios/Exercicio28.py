"""
28 - Faça um prograra que leia três números inteiros positivos e efetue o cálculo de umas das seguintes
     médias de acordo com um valor numérico digitado pelo usuário:

     a: Geométrica: raiz(x * y * z)
     b: Ponderada: x + 2 * y +  3 * z/ 6
     c: Harmônica: 1 / 1/x + 1/y + 1/z
     d: Aritmética: x + y + x / 3
"""
import math

def geometrica(x, y, z):
    num = x * y * z
    rais_num = math.sqrt(num)
    return rais_num

def ponderada(x, y, z):
    media = (x + (2 * y) + (3 * z)) / 6
    return media

def harmonica(x, y, z):
    har = 1 / ((1/x) + (1/y) + (1/z))
    return har

def aritmetica(x, y, z):
    media = (x + y + z) / 3
    return media


print("Escolha em qual medida deseja calcular os valores:\n")
print("1 - Geométrica")
print("2 - Ponderada")
print("3 - Harmônica")
print("4 - Aritmética")

opcao = input("Digite o número da operação desejada (1, 2, 3, ou 4):\n ")

x = float(input("Digite o valor de x:\n"))
y = float(input("Digite o valor de y:\n"))
z = float(input("Digite o valor y:\n"))

if opcao == "1":
   res = geometrica(x, y, z)
   print(f"O cálculo geométrico das seguintes medias é {round(res)}")

elif opcao == "2":
    res = ponderada(x, y ,z)
    print(f"O cálculo ponderado das seguintes medias é {round(res)}")

elif opcao == "3":
    res = harmonica(x, y, z)
    print(f"O cálculo harmonico das segunites medidas é {round(res)}")

elif opcao == "4":
    res = aritmetica(x, y, z)
    print(f"O cálculo aritmético das seguintes medidas é {round(res)}")

else:
    print("Opção inválida!")
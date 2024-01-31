"""
21 - Leia um valor de massa em libras e apresente-o convertido em quilogramas.
     A fórmula de conversão é K = l * 0.45, sendo k(Quilograma) L(Libras).
"""

libras = float(input("Digite o valor da massa em Libras:\n"))
print(f"{round(libras)}\L")

kg = libras * 0.45

print(f"O valor da massa digitado em Libras foi {round(libras)}\L e convertido em Quilogramas é {round(kg)}\Kg")
"""
20 - Leia um valor de massa em quilograma e apresente-o convertido em libras.
     A fórmula de conversão é: L = K / 0.45, sendo K(Quilograma) e L(libras).
"""

kg = float(input("Digite o valor da massa em Quilograma:\n"))
print(f"{kg}/kg")

libras = kg / 0.45
print(f"O valor da massa digitado em Quilograma foi {kg}/kg e convertido em Libras é {libras}/L")
"""
18 - Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros.
     A fórmula é: L = 1000 * M, sendo l(Litros) e M(Metros Cúbicos).
"""
mc = float(input("Digite o valor do volume:\n"))
print(f"{mc}/m³")

litros = 1000 * mc
print(f"O valor digitado em metros cúbicos foi {mc}/m³ e convertido em litros é {round(litros)}/L")
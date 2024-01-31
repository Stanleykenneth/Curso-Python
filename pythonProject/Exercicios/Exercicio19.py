"""
19 - Leia um valor em Litros e apresente-o convertidos em metros cúbicos m³.
     a fórmula de conversão é: L / 1000.
"""

litros = float(input("Leia um vlaor em Litros:\n"))
print(f"{round(litros)}/L")

mc = litros / 1000
print(f"O valor digitado em litros foi {round(litros)}/L e convertidos em metros cúbicos é {round(mc)}/m³")
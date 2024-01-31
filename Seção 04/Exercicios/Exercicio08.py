"""
08 - Leia  uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
     A fórmula  de conersão é: C = K - 273.15,sendo C(Celsius) e K(Kelvin).
"""

num = float(input("Digite a temperatura em kelvin:\n"))
print(f"{num}.K")
print("")

convert = num - 273.15
print(f"A temperatura em Kelvin é {num}.K e convertida em grau Celsius é {round(convert)}.C")

"""
09 - Leia  uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
     A fórmulade conversão é: K = C + 273.15, sendo C(Celsius) e K(Kelvin).
"""
num = int(input("Digite a temperatura em grau Celsius:\n"))
print(f"{num}.C")

convert = num + 273.15
print(f"A temperatura em Celsius {num}.C, convertida em Kelvin é: {convert}.K")
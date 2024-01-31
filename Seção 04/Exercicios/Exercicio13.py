"""
13 - Leia uma distância em quilômetros e apresente-a convertida em milhas.
     A fórmula de conversão é: M = K / 1.61, sendo K(Quilômetros) e M(Milhas).
"""

Km = int(input("Digite uma distância em Quilômetros:\n"))
print(f"{Km}/Km")

convert = Km / 1.61
print(f"A distância em quilômetros {Km}/Km convertida em milhas é: {convert}/M")
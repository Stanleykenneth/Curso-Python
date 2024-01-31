"""
12 - Leia uma distância em milhas e apresente-a convertida em em quilômetros.
     A fórmula de conversão é: K = 1.61 * M, sendo K(Quilômetros) e M(Milhas).
"""

milhas = float(input("Digite a distância em Milhas:\n"))
print(f"{milhas}/M")

print("")

convert = 1.61 * milhas
print(f"A distância em Milhas {milhas}/M convertida em Quilômetros é: {round(convert)}/Km")
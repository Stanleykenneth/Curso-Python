"""
12 - Leia uma distância em milhas e apresente-a convertida em quilômetros.
     A fórmula de conversão é: K = 1.61 * M, sendo K(Quilômetros) e M(Milhas).
"""
milhas = float(input("Digite uma distância em milhas:\n"))
print(f"{milhas}/M")

convert = 1.61 * milhas
print(f"As milhas {milhas}/M convetida em Quilômetros é: {round(convert)}/K")
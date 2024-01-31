"""
13 - Leia uma distância em Quilômetros e apresente-a convertida em milhas.
     A fórmula é: M = K / 1.61, sendo k(Quilômetros) e M(milhas)
"""
Km = float(input("Digite uma distância em Quilômetros:\n"))
print(f"{Km}/km")

Milhas = Km / 1.61
print(f"A distância digita em Quilômetros foi {Km}/km e convertida em milhas é {Milhas}/M")
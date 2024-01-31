"""
15 - Laeia um ângulo em radianos e apresente-o em graus.
     A fórmula  de conversão é: G = R * 180/ PI.
"""
import math

radiano = float(input("Digite um ângulo em Graus:\n"))
print(f"{radiano}")

grau = radiano * (180 / math.pi)
print(f"O ângulo digitado em radiano {radiano} convertido em Graus é {round(grau)}°")



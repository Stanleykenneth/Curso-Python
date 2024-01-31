"""
15 - Leia um ângulo em radianos e apresente-o convertidos em Graus.
     A formula é: G = R * 180/ pi, sendo G(Grau) e R(radianos).
"""
import math

radiano = float(input("Digite um ângulo em Radiano:\n"))
print(f"{radiano}")

grau = radiano * 180 / math.pi
print(f"O ângulo digitado em radiano é {radiano} e convertido em Graus é {grau}")
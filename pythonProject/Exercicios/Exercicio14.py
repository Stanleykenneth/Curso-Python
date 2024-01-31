"""
14 - Leia um ângulo e, graus e apresente-o convertido em radianos.
     A fórmula de conversão é: R = G * PI / 180, sendo G(Grau) e R(Radiano)

"""
import math

grau = float(input("Digite um ângulo em graus.\n"))
print(f"{grau}°")

radiano = grau * (math.pi / 180)
print(f"O Grau digitado {grau}° e convertido em Radianos é {radiano}")
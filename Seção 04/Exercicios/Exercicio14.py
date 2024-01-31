"""
14 - Leia um ângulo em grau e apresente-o convertido em radianos.
     A formula de conversão  é R = G * pi/180, sendo G o ângulo em Graus
     e R em radianos e PI = 3.14.
"""
import math

angulo = float(input("Digite um angulo:\n"))
print(f"{angulo}")

converte = angulo * math.pi / 180
print(f"O ângulo digita foi {angulo} e sua conversão em Radiano é {converte}")
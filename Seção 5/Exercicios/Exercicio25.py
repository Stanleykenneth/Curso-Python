"""
25 - Calcule as raizes da equação de 2º grau.
     Lembrando que:

     x = -b + - raiz de delta / 2 * a
     onde:
     Delta = b * b - 4 * a * b
"""
import math

def calcular_raizes(a, b, c):

    delta = b ** 2 - 4 * a * c

    if delta > 0:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        return x1, x2
    elif delta == 0:
        x = -b / (2 * a)
        return x,
    else:
        return "Não há reaizes reais, pois o delta é negativo."

a = float(input("Digite o coeficente 'A':\n"))
b = float(input("Digite o coeficente 'B':\n"))
c = float(input("Digite o coeficente 'C':\n"))

raizes = calcular_raizes(a, b, c)

if isinstance(raizes, str):
    print(raizes)
else:
    print(f"As raizes da equação são: {raizes}")
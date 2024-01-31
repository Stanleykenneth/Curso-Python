"""
16 - Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
     A fórmula é: C = P * 2.54, sendo C(centimetros) e P(Polegadas).
"""

polegada = float(input("Digite o valod de um comprimento em polegadas:\n"))
print(f"{polegada}\"")

centimetro = polegada * 2.54
print(f"O valor digitado em polegadas foi {polegada}\" e o valor convertido em Centimetros é {centimetro}/Cm")
"""
16 - Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
     A fórmula de conversão é: C = P * 2.54, sendo  C(Centimetros) e P(Polegadas).

"""
pelegadas = float(input("Digite o valor da polegada:\n"))
print(f"{pelegadas}")

centimetro = pelegadas * 2.54
print(f"A pelegada digitada foi {pelegadas} e sua conversão em Centimetros é {centimetro}")
"""
17 - Leia um valor de comprimento em centimetro e apresente-o convertido em Poloegadas.
     A formula de conversão é: P = C / 2.54.
"""
centimetros = float(input("Digite um valor em centimetros:\n"))
print(f"{centimetros}")

pologadas =  centimetros / 2.54
print(f"O comprimento digitado foi {centimetros}/Cm e convertidos em polegadas é {pologadas}\"")

"""
    10 - Leia uma velocidade em km/h (quilômetros por hr) e apresente-a em m/s (metros por segundo).
         A fórmula de conversão é: M = K/3.6, sendo K(km/h) e M(m/s).
"""

km = int(input("Digite a a velocidade:\n"))
print(f"A velocidade é {km}km/h")

convert = km/3.6
ms_formatado = round(convert, 2)
print(f"A velocidade convertida em metros por segundo é: {ms_formatado}.m/s")
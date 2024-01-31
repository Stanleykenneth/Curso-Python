"""
11 - Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida km/h (Quilôimetros por hora).
     A fórmula de conversão é: K = M * 3.6, sendo K(km/h) e M(m/s).
"""
m = float(input("Digite a velocidade em metros por segundos:\n"))
print(f"{m}m/s")
convert = m * 3.6
print(f"A velocidade {m}m/s convertida em Quilômetros por hora é de: {round(convert)}km/h")
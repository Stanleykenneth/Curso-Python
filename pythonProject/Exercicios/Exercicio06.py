"""
06 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
     A fórmula de conversão é: F = C *(9.0/5.0)+ 32.0, sendo F (Temperatura Fahrenheit)
     e C(Temperatura em Celsius).
"""

temperatura = int(input("Digite a teperatura em graus Celsius:\n"))
print(f"{temperatura}.C")

convert_Temp = temperatura * (9.0 / 5.0) + 32.0
print(f"A temperatura de {temperatura}.C grau Celsius convertida para Fahrenheit é: {convert_Temp}.F")



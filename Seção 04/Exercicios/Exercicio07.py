"""
07 - Leia uma temperatura em graus Fahreinheit e apresente-a convertida em graus Celsius.
     A fórmula de conversão é: C = 5.0 * (F - 32.0)/ 9.0, sendo que C(Celsius) e F(Fahreinheit).
"""

temperatura = float(input("Digite a temperatura em Fahreinheit:\n"))
print(f"{temperatura}.F")
print("")

convert_temp = 5.0 * (temperatura - 32.0) / 9.0
print(f"A temperatura {temperatura}F convertida em graus Celsius é: {round(convert_temp)}.C")



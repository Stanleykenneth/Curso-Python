"""
17 - Faça um programa que calcule e mostre a área de um trapézio.
     Sabe-se que: a = (base maior + base menor) * altura / 2.
     Lembre-se: A base mairo e menor dever ser números maiores que zero.
"""

baseMaior = float(input("Digite o valor da base maior:\n"))
baseMenor = float(input("Digite o valor da base menor:\n"))
altura = float(input("Digite o valor da altura:\n"))

trapezio = ((baseMaior + baseMenor) * altura) / 2

print(f"O valor calculado do trapézio é {trapezio}")
"""
31 - Faça um programa que receba a altura e o peso de uma pessoa. De acordo coma a tabela a seguir
     verifique e mostre qual classificação dessa pessoa.

     altura:                       peso:
     Menor que 1,20                Até 60 A
                                   Entre 60 e 90(Inclusive) D
                                   Acima de 90 G

     De 1,20 a 1,70                Até 60 B
                                   Entre 60 e 90(Inclusive) E
                                   Acima de 90 H

     Maior que 1,70                Até 60 C
                                   Entre 60 e 90(Inclusive) F
                                   Acima de 90 I

"""

altura = float(input("Digite su altura:\n"))
peso = float(input("Digite o seu peso:\n"))

if altura <= 1.20:
    if peso <= 60:
        print("Categoria A")
    elif 60 < peso <= 90:
        print("Categoria D")
    elif peso > 90:
        print("Categoria G")

elif 1.20 < altura <= 1.70:
    if peso <= 60:
        print("Categoria B")
    elif 60 < peso <= 90:
        print("Categoria E")
    elif peso > 90:
        print("Categoria H")

elif altura > 1.70:
    if peso <= 60:
        print("Categora C")
    elif 60 < peso <= 90:
        print("Categori F")
    elif peso > 90:
        print("Categoria I")



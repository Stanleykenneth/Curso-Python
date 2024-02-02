"""
34 - Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a tabela abaixo,
     quando o aluno tem mais de 20 faltas ocorre uma reduçao de conceito.

     nota:              Conceito(até 20 Faltas)     Conceito (Mais de 20 faltas)
     9.0 até 10.0                  A                              B
     7.5 até 8.9                   B                              c
     5.0 até 7.4                   c                              d
     4.0 até 4.9                   d                              e
     0.0 até 3.9                   e                              e
"""

nota = float(input("Digite a sua nota:\n"))
faltas = int(input("Digite a quantidade de faltas:\n"))

if 9.0 < nota <= 10.0:
    if faltas <= 20:
       print("Conceito A")
    elif faltas > 20:
        print("Conceito B")
elif 7.5 < nota <= 8.9:
    if faltas <= 20:
        print("Conceito B")
    elif faltas > 20:
        print("Conceito C")
elif 5.0 < nota <= 7.4:
    if faltas <= 20:
       print("Conceito C")
    elif faltas > 20:
        print("Conceito D")
elif 4.0 < nota <= 4.9:
    if faltas <= 20:
       print("Conceito D")
    elif faltas > 20:
        print("Conceito E")
elif 0.0 < nota <= 3.9:
    if faltas <= 20:
       print("Conceito E")
    elif faltas > 20:
        print("Conceito E")

else:
    print(" A nota não entra no conceito avaliativo!")
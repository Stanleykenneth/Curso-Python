"""
14 - A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10,
     respectivamente, a um trabalhode laboratório, a uma avaliação semestrel e a um exame final. A média da três notas
     mencionadas anteriormente obedece aos pesos:
     Trabalho de laboratório: 2;
     Avaliação semestral: 3;
     Exame final: 5;
     De acordo com o resultado, mostre na tela se o aluno está reprovado (Média entre 0 e 2.9), de recupaeração (entre 3 e 4.9)
     ou se foi aprovado. Faça todas as verificações necessárias.
"""

lab = float(input("Digite o valor da nota do Trabalho de Laboratório:\n"))
avalia_Seme = float(input("Digite o valor da nota da Avaliação Semestral:\n"))
exameFinal = float(input("Digite a nota do Exame Final:\n"))


media = ((2 * lab) + (3 * avalia_Seme) + (5 * exameFinal)) / 10


if 0 <= media <= 2.9:
    print(f"A média é {media}. Aluno Reprovado!")

elif 3.0 <= media <= 4.9:
    print(f"A média é {media}. Aluno em Recuperação!")

elif media >= 5.0:
    print(f"A média é {media}. Aluno Aprovado!")

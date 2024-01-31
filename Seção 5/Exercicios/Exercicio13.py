"""
13 - Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda
     prova têm peso 1 e a terceira tem peso 2. Ao final, mostar a média do aluno e indicar se o aluno
     foi aprovado ou repovado. A nota para aprovação deve ser igual ou superior a 60 pontos.
"""

nota1 = float(input("Digite a nota da primeira prova:\n"))
nota2 = float(input("Digite a nota da segunda prova:\n"))
nota3 = float(input("Digite a nota da terceira prova:\n"))

media_ponderada = (nota1 + nota2) + (2 * nota3) / 4
print(f"Média ponderada: {media_ponderada}")

if media_ponderada >= 60:
    print("Aluno aprovado!")
else:
    print("Aluno repovado!")
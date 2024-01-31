"""
22 - Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
     As condições para a aposentadoria são:
     . Ter pelo menos 65 anos.
     . Ou ter trabalhado pelo menos de 30 naos.
     . Ou ter pelo menos 60 e trabalhado pelo menos de 25 anos.
"""

idade = int(input("Digite sua idade:\n"))
tempoServico = int(input("Digite o tempo de serviço:\n"))

if idade >= 65:
    print("Parabéns, você já pode se aposentar!")

elif tempoServico >= 30:
    print("Parabéns, você já pode se aposentar!")

elif idade >= 60 or tempoServico >= 25:
    print("Parabéns, você já pode se aposentar!")

else:
    porIdade = 65 - idade
    porTempo = 30 - tempoServico
    print(f"Continue, falta {porIdade} anos para você se aposentar por idade ou {porTempo} anos para se aposentar por tempo de serviço.")



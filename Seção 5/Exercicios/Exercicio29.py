"""
29 - Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros
     menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta:
     qual é a soma de a + b, onde a e b são os números aleatórios. Peça a resposta. Faça cinco pergunta
     ao aluno, e mostre para ele as perguntas e as respostas corretas elém de quantas vezes o aluno acertou.
"""

import random

def gerar_pergunta():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    return a, b

def verificar_resposta(a, b, resposta):
    return a + b == resposta


pontuacao = 0
tentativas = 0
total_perguntas = 5

while tentativas < total_perguntas:
    a, b = gerar_pergunta()
    pergunta = f"Qual é a soma de {a} + {b}?\n "

    try:
        resposta = int(input(pergunta))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if verificar_resposta(a, b, resposta):
        print("Correto!\n")
        pontuacao += 1
    else:
        print(f"Incorreto. A resposta correta é {a + b}.\n")

    tentativas += 1

print(f"Você acertou {pontuacao} de {total_perguntas} perguntas.")

"""for _ in range(5):
    a, b = gerar_pergunta()
    pergunta = f"Qual é a soma de {a} + {b}?\n "

    try:
        resposta = int(input(pergunta))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if verificar_resposta(a, b, resposta):
        print("Correto!\n")
        pontuacao += 1
    else:
        print(f"Incorreto. A resposta correta é {a + b}.\n")

print(f"Você acertou {pontuacao} de 5 perguntas.")
"""
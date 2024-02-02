"""
33 - Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo,
     calcule e escreva o preço novo, escreva uma mensagem em função do preço novo(de acordo com asegunda tabela).

     PREÇO ANTIGO:             PERCENTUAL DE AUMENTO:
     Até R$ 50                          5%
     entre R$50 e R$100                 10%
     acima de R$100                     15%

     PREÇO NOVO:                       MENSAGEM:
     Até R$80                          Barato
     entre R$80 e R$120(inclusive)     Normal
     entre R$120 e R$200(inclusive)    Caro
     Acima de R$200                    Muito Caro
"""

preco_antigo = float(input("Digite o preço antigo:\n "))

if preco_antigo <= 50:
    percentual_aumento = 0.05
elif preco_antigo <= 100:
    percentual_aumento = 0.10
else:
    percentual_aumento = 0.15


preco_novo = preco_antigo * (1 + percentual_aumento)

if preco_novo <= 80:
    mensagem = "Barato"
elif preco_novo <= 120:
    mensagem = "Normal"
elif preco_novo <= 200:
    mensagem = "Caro"
else:
    mensagem = "Muito Caro"


print(f"Novo preço: R${preco_novo:.2f}")
print(f"Mensagem: {mensagem}")

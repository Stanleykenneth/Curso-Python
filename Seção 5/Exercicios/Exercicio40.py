"""
40 -  O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão
      do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o
      custo de fábrica, de acordo com a tablea abaixo. Leia o custo de fábrica e escreva ao consumidor.

      CUSTO DE FÁBRICA:                  % DO DISTRIBUIDOR:          % DOS IMPOSTOS:
      Até R$12.000,00                            5                        isento
      entre R$12.000,00 e 25.000,00              10                          15
      acima de R$25.000,00                       10                          20
"""


def calcular_custo_consumidor(custo_de_fabrica):
    if custo_de_fabrica <= 12000:
        percentual_distribuidor = 5
        percentual_impostos = 0
    elif 12000 < custo_de_fabrica <= 25000:
        percentual_distribuidor = 10
        percentual_impostos = 15
    else:
        percentual_distribuidor = 10
        percentual_impostos = 20

    # Calcula a comissão do distribuidor e os impostos
    comissao_distribuidor = (percentual_distribuidor / 100) * custo_de_fabrica
    impostos = (percentual_impostos / 100) * custo_de_fabrica

    # Calcula o custo ao consumidor
    custo_consumidor = custo_de_fabrica + comissao_distribuidor + impostos

    return custo_consumidor

# Leitura do custo de fábrica
custo_de_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

# Calcula e exibe o custo ao consumidor
custo_final = calcular_custo_consumidor(custo_de_fabrica)
print(f"O custo ao consumidor é: R$ {custo_final:.2f}")

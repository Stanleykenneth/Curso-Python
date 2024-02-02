"""
39 - Uma empresa decide dar aumento aos seus funcionários de acordo com uma tabela que considera osalário atual
     e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento prorporcionalmente
     maior do que os funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá
     receber um bonus adicional de salário. Faça um programa que leia:
     .O valor do salário atual do funcionário;
     .O tempo de serviço desse funcionário na empresa(número de anos de trabalho na empresa).

     Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário
     final resjustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

     SALÁRIO ATUAL:                 REAJUSTE(%):                 TEMPO DE SERVIÇO:           BÔNUS:
     Até 500,00                         25%                        Abaixo de 1 ano           Sem Bônus
     Até 1000,00                        20%                        De 1 ano a 3 anos         100,00
     Até 1500,00                        15%                        De 4 ano a 6 anos         200,00
     Até 2000,00                        10%                        De 7 ano a 10 anos        300,00
     Acima de 2000,00                   Sem reajuste               Mais de 10 anos           500,00
"""
def calcular_aumento(salario_atual, tempo_servico):
    if salario_atual <= 500:
        reajuste_percentual = 0.25
        bonus = 0
    elif salario_atual <= 1000:
        reajuste_percentual = 0.20
        bonus = 100
    elif salario_atual <= 1500:
        reajuste_percentual = 0.15
        bonus = 200
    elif salario_atual <= 2000:
        reajuste_percentual = 0.10
        bonus = 300
    else:
        reajuste_percentual = 0
        bonus = 500

    if tempo_servico < 1:
        bonus = 0

    aumento = salario_atual * reajuste_percentual
    salario_reajustado = salario_atual + aumento + bonus

    return salario_reajustado


# Entrada do salário atual e tempo de serviço
salario_atual = float(input("Digite o salário atual do funcionário: R$ "))
tempo_servico = int(input("Digite o tempo de serviço (em anos): "))

# Calcular o salário reajustado
salario_reajustado = calcular_aumento(salario_atual, tempo_servico)

# Exibição do resultado
if salario_reajustado > salario_atual:
    print(f"Salário reajustado: R$ {salario_reajustado:.2f}")
else:
    print("O funcionário não tem direito a nenhum aumento.")

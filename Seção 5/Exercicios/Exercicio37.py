"""
37 - As tarifas de certo parque de estacionamento são as seguintes:

     1º e 2ª hora - R$ 1,00 cada
     3º e 4º hora - R$ 1,40 cada
     5º horas e seguintes - R$ 2,00 cada

     O número de de horas a pagar é sempre inteiro e arrdondado por excesso. Deste modo,
     quem estacionar durante 61 minutos pagará por dua horas, que é o mesmo que pagaria
     se estivesse permanecido 120 minutos. Os momento de chegada ao parque e partida deste
     são apresentados na forma de pares inteiros, representando horas e minutos.
     Por exemplo, o par 12 50 representará " dez para uma da tarde". Pretende-se criar
     um programa que, lidos pelo teclado os momentos de chegada e a partida se dão com
     interva-lo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior
     à da partida, isso não é umas situação de erro, antes significará que a partida ocorreu
     no dia seguinte ao da chegada.
"""
from datetime import datetime

def calcular_custo_estacionamento_com_data(chegada, partida):
    # Convertendo data, horas e minutos para minutos totais
    minutos_chegada = chegada[0] * 24 * 60 + chegada[1] * 60 + chegada[2]
    minutos_partida = partida[0] * 24 * 60 + partida[1] * 60 + partida[2]

    # Calculando o tempo total em minutos
    tempo_total_minutos = minutos_partida - minutos_chegada

    # Calculando o tempo total em dias e minutos
    dias, minutos = divmod(tempo_total_minutos, 24 * 60)

    # Calculando o custo com base nas tarifas
    if dias == 0:
        # Mesmo dia
        if minutos <= 120:  # 1ª e 2ª hora
            custo = minutos * 1.00
        elif minutos <= 240:  # 3ª e 4ª hora
            custo = 120 + (minutos - 120) * 1.40
        else:  # 5ª hora e seguintes
            custo = 120 + 120 + (minutos - 240) * 2.00
    else:
        # Dias adicionais
        custo = dias * 24 * 2.00  # R$ 2,00 por hora para dias adicionais

    return custo

# Entrada dos momentos de chegada e partida
data_chegada = datetime.strptime(input("Data de chegada (DD/MM/YYYY):\n "), "%d/%m/%Y")
hora_chegada = int(input("Hora de chegada (0 a 23):\n "))
minuto_chegada = int(input("Minuto de chegada (0 a 59):\n "))

data_partida = datetime.strptime(input("Data de partida (DD/MM/YYYY):\n "), "%d/%m/%Y")
hora_partida = int(input("Hora de partida (0 a 23):\n "))
minuto_partida = int(input("Minuto de partida (0 a 59):\n "))

# Cálculo do custo de estacionamento
custo_total = calcular_custo_estacionamento_com_data(
    (data_chegada.day, hora_chegada, minuto_chegada),
    (data_partida.day, hora_partida, minuto_partida)
)

# Exibição do resultado formatado
print(f"O custo total de estacionamento é: R$ {custo_total:.2f}")

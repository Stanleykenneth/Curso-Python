"""
15 - Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
     correspondente a este número. Isto é, Janeiro 1, Fevereiro 2, e assim por diante.

"""
def meses_do_ano(num):
    mes = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novenbro",
        12: "Dezembro"
    }

    return mes.get(num, "Número inválido!")

numero_mes = int(input("Digite um número entre 1 e 12:\n "))

resultado = meses_do_ano(numero_mes)
print(resultado)

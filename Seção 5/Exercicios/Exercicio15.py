"""
15 - Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana
     correspondente a este número. Isot é, domingo 1, segunda 2, e assim por diante.

"""
def dias_da_semana(num):
    dias = {
        1: "Domingo",
        2: "Segunda-Feira",
        3: "Terça-Feira",
        4: "Quarta-Feira",
        5: "Quinta-Feira",
        6: "Sexta-Feira",
        7: "Sábado"
    }

    return dias.get(num, "Número inválido!")

numero_dia = int(input("Digite um número entre 1 e 7:\n "))

resultado = dias_da_semana(numero_dia)
print(resultado)

"""
26 - Leia a distância em Km e a quantidade de litros de gasolina consumidos por uma carro em um percurso,
     calcule o consumo em km/l e escreva uma mensagem de acordo com a tabela abaixo:

     Consumo > 8, venda o carro!
     Consumo entre 8 e 14, Econômico!
     Consumo 12 Super Econômico!

"""
distancia = float(input("Digite a distância percorrida:\n"))
litros = 42
consumo = distancia / litros

if consumo >= 8:
    print("Venda o carro!")

elif 8 >= consumo <= 12:
    print("Econômico!")

elif consumo >= 14:
    print("Super econômico!")

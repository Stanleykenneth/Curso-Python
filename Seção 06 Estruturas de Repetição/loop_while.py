"""
Loop while

Forma Geral

while expressão_booleana:
    //execuçao do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.
Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5
num < 5

# Exemplo 1
numero = 1

while numero <= 10:
    print(numero)
    numero = numero + 1
#OBS: Em um loop while, é importante que cuidemos do critério de parada, para não causar um loop infinito.(Onde nunmca sai do loop)


# Exemplo 2


"""
# EXemplo 2
resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Jéssica?')
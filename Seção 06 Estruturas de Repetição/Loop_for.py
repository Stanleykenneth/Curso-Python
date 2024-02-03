"""
Loop for
Loop -> Estrutura de repetição.
For  -> Uma dessas estruturas.

C ou Java
for(int i = 0; i < 10; i++){
    // execução do programa
}

Python

for item in iteravel:
    //execução!

Utilizamos loops para itera sobre seguências ou sobre valores interáveis.
Exemplo de interáveis:
- String
  nome = 'Geek University'
- Lista
  lista = [1, 2, 3, 4, 5]
- Range
  numeros = range(1, 10)

  Enumerate:
((0, 'g'), (1, e), (2, e))

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice. letra in enumerate(nome):
    print(letra)

for _, letra in enumerate:
    print(letra)
OBS: Quando não precisamos de um valor podemos descarta-lo utilizando um undeline (_)

for valor in enumerate(nome):
    print(valor)
(0, 'G')
(1, 'e')
(2, 'e')
(3, 'k')
(4, ' ')
(5, 'U')
(6, 'n')
(7, 'i')
(8, 'v')
(9, 'e')
(10, 'r')
(11, 's')
(12, 'i')
(13, 't')
(14, 'y')


qtd = int(input("Quantas vezes esse loop deve rodar?\n"))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f"Informe o {n}/{qtd} valor:\n"))
    soma = soma  + num
print(f'A soma é {soma}')

Quantas vezes esse loop deve rodar?
5
Informe o 1/5 valor:
2
Informe o 2/5 valor:
3
Informe o 3/5 valor:
4
Informe o 4/5 valor:
5
Informe o 5/5 valor:
6
A soma é 20


Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# exemplo de for 1 (Interando em uma String)
for letra in nome:
    print(letra)
print("")
# Exemplo de for 2 (Interando sobre uma lista)
for numeros in lista:
    print(numeros)
print("")

# Exemplo de for 3 (Interando sobre um Range)
"""
range(valor_inicial, valor_final)
OBS: O valor final não é inclusive. (Inicia no número 1 e vai até o 9)
"""
for numero in range(1, 10):
    print(numero)
print("")

"""
Enumerate:
((0, 'g'), (1, e), (2, e))
"""
for i, v in enumerate(nome):
    print(nome[i])

print("")
for valor in enumerate(nome):
    print(valor)

print("--------------------------------------")

qtd = int(input("Quantas vezes esse loop deve rodar?\n"))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f"Informe o {n}/{qtd} valor:\n"))
    soma = soma  + num
print(f'A soma é {soma}')

# Imprimindo tudo na mesma linha
for letra in nome:
    print(letra, end='')

#------------------------------------------------------------------------------------
# Imprimindo emoji 
# Original: U+1F60D
# Modificado: U0001F60D

emoji = 'U0001F60D'
for num in range(1, 11):
    print('\U0001F60D' * num)
"""
Ranges

  - Precisamos conhecer o loop for para usar os ranges.
  - Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequência numéricas, nãp de forma aleatória,
mas sim de maneira especificada.

Formas Gerais:

# forma 1

range(valor_de_parada)
OBS: valor_de_parada não inclusive (início padrão 0, passo de 1 em 1)
# Exemplo forma 1
for num in range(11):
    print(num)

# forma 2
range(valor_de_inici, valor_de_parada)
OBS: valor_de_parada não inclusive(início especificado pelo usuário, e passo de 1 em 1)
# Exemplo forma 2
for num in range(1, 11):
    print(num, end='')


# forma 3
range(valor_de_inici, valor_de_parada, passo)
OBS: valor_de_parada não inclusive(início especificado pelo usuário, e passo específicado peço usuário)
# Exemplo forma 3
for num in range(2, 12, 2):
    print(num, end='')


# forma 4 (Inversa)
range(valor_de_início, valor_de_parada, passo)
OBS: valor_de_parada não inclusive(valor_de_início especificado pelo usuário, e passo específicado peço usuário)

"""
# Exemplo forma 1
for num in range(11):
    print(num, end='')
print('')

# Exemplo forma 2
for num in range(1, 11):
    print(num, end='')
print('')

# Exemplo forma 3
for num in range(2, 12, 2):
    print(num, end='')
print('')

# Exemplo forma 4
for num in range(10, -1, -1):
    print(num,'', end='')

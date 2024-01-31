"""
Estruturas Lógicas: and(e), or(ou), not(não), is(é)
Operadore: unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:

- Para o 'AND', ambos os valores precisam ser True.
- Para o 'OR', um ou outro valor precisa ser TRUE.
- Para o 'NOT', o valor do booleano é invertido, ou seja, se for TRUE, vira Falso, se for FALSE vira TRUE.

"""
ativo = True
logado = True

"""Para o 'AND', ambos os valores precisam ser True. """
if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta, cheque seu e-mail')

print("----------------------------------------------------------")

""" Para o 'OR', um ou outro valor precisa ser TRUE """
if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta, cheque seu e-mail')

print("----------------------------------------------------------")

""" SE não estive ativo """
if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu email')
else:
    print('Bem-vindo usuário!')
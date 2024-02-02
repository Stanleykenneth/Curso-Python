"""
35 - Leia um data e determine se ela é válida. Ou seja. verifique se o mês está entre 1 e 12,
     e se o dia existe naquele mês. Note que fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.
"""

def is_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True, "É ano bissexto!"
    else:
        return False, "Não é ano bissexto!"

def valida_data(ano, mes, dia):
    if 1 <= mes <= 12:
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= dia <= 31
        elif mes in [4, 6, 9, 11]:
            return 1 <= dia <= 30
        else:
            if is_bissexto(ano)[0]:
                return 1 <= dia <= 29
            else:
                return 1 <= dia <= 28
    else:
        return False

dia = int(input("Digite o Dia:\n "))
mes = int(input("Digite o Mês:\n "))
ano = int(input("Digite o Ano:\n "))

if valida_data(ano, mes, dia):
    print("Data válida.")
else:
    print("Data inválida.")

bissexto, mensagem_bissexto = is_bissexto(ano)
print(f"O ano é {ano}. {mensagem_bissexto}")

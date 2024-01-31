"""
23 - Determine se um ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se
     for divisível por 4 e não divisível por 100. Por exemplo:
     1988, 1992, 1996
"""

def is_bissexto(ano):
    if(ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

anos = int(input("Digite um ano:\n"))

if is_bissexto(anos):
    print(f"O ano {anos} é bissexto.")
else:
    print(f"O ano {anos} não é bissexto.")
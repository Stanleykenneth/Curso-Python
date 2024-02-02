"""
38 - Leia uma data de nascimento de uma pessoa fornecida através de três número inteiros:
     Dia, Mês e Ano. Teste a validade desta data para saber se esta data é uma data válida.
     Teste se o dia fornecido é um dia válido: dia > 0, dia <= 28 para o mês de fevereiro
     (29 se o ano for bissexto), dia <= 30 em abril, junho, setembro e novembro, dia <= 31
     nos outros meses. Teste a validade do mês > 0 e mês 13. Teste a validades do ano <= anos atual
     (Use uma constante definida como valor igual a 2024). Iprimir: "data válida" ou "data Inválida"
     no final da execuçao do programa.
"""
from datetime import datetime
import locale

# Configuração para o formato brasileiro
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Constante para o ano atual
ANO_ATUAL = 2024

def validar_data(dia, mes, ano):
    try:
        data_nascimento = datetime(ano, mes, dia)
        return True, data_nascimento
    except ValueError:
        return False, None

def calcular_idade(data_nascimento):
    hoje = datetime(ANO_ATUAL, 1, 1)  # Considerando o primeiro dia do ano atual como referência
    idade = (hoje - data_nascimento).days // 365
    return idade

# Entrada da data de nascimento
dia = int(input("Digite o dia de nascimento: \n"))
mes = int(input("Digite o mês de nascimento:\n "))
ano = int(input("Digite o ano de nascimento:\n "))

# Validar a data de nascimento
data_valida, data_nascimento = validar_data(dia, mes, ano)

# Verificar se a data é válida e calcular a idade
if data_valida:
    idade_usuario = calcular_idade(data_nascimento)
    data_formatada = data_nascimento.strftime('%d de %B de %Y')
    print(f"Data válida. Idade do usuário: {idade_usuario} anos. Data formatada: {data_formatada}")
else:
    print("Data inválida.")

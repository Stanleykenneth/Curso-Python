"""
09 - Leia o salário de um trabalhador e o valor da prestação de um emprestimo.
     Se a prestação for maior que 20% do seu salário imprima: Empréstimo não concedido.
     Caso contrário imprima: Empréstimo concedido

"""

salario = float(input('Digite o valor do seu salário:\n'))
emprestimo = float(input('Digite o valor que deseja solicitar de empréstimo:\n'))
parcelas = int(input('Digite a quantidade de parcelas em que deseja pagar:\n'))
prestacao = emprestimo / parcelas

if prestacao > salario * 0.2:
    print(f"O valor da prestação R${round(prestacao, 2)} excede 20% do salário. Empréstimo não concedido!!!")
else:
    if parcelas <= 5:
       print(f"Empréstimo concedido! O valor da parcela é de R${round(prestacao, 2)} parcelado em {parcelas}X, sem juros.")

    elif 6 <= parcelas <= 9:
         juros = emprestimo * 0.1
         prestacao_com_juros = prestacao + juros
         if prestacao_com_juros > salario * 0.2:
             print(f"O valor da prestação R${round(prestacao, 2)} excede 20% do salário. Empréstimo não concedido!!!")
         else:
             print(f"Empréstimo concedido! A quantidade de parcelas sugeridas foi {parcelas} e o valor da prestação ficou de R${round(prestacao_com_juros, 2)} com 10% de juros sobre o valor do empréstimo.")

    elif parcelas >= 10:
        juros = emprestimo * 0.2
        prestacao_com_juros = prestacao + juros
        if prestacao_com_juros > salario * 0.2:
            print(f"O valor da prestação R${round(prestacao, 2)} excede 20% do salário. Empréstimo não concedido!!!")
        else:
            print(f"Empréstimo concedido! A quantidade de parcelas sugeridas foi {parcelas} e o valor da prestação ficou de R${round(prestacao_com_juros, 2)} com 10% de juros sobre o valor do empréstimo.")

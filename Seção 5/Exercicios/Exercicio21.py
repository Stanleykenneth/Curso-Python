"""
21 - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a aoperação escolhida.
     Escreva uma mensagem de erro se a opção for inválida.

     Escolha a opção:
     1 - Soma de dois números.
     2 - Diferença entre dois  números (maior pelo menor)
     3 - Produto entre 2 números
     4 - Divisão entre 2 numeros (o denominador não pode ser zero).
     Opção
"""

def soma(a, b):
    return a + b

def diferenca(a, b):
    return a - b

def protudo(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: O número não pode ser divido por zero."

while True:
    print("\nEscola a opção:\n")
    print("1 - Soma de dois números.")
    print("2 - Diferença entre dois números (Maior pelo Menor).")
    print("3 - Produto entre dois números.")
    print("4 - Divisão entre dois números (o Denominador não pode ser zero).")
    print("5 - Sair do programa.")
    print("")

    opcao = input("Opção:\n")
    if opcao == "5":
        print("Obrigado por utilizar nosso Programa!")
        break

    elif opcao in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Digite o primeiro número:\n"))
            num2 = float(input("Digite o segundo número:\n"))

            if opcao == "1":
                resultado = soma(num1, num2)

            elif opcao == "2":
                resultado = diferenca(num1, num2)

            elif opcao == "3":
                resultado = protudo(num1, num2)

            elif opcao == "4":
                resultado = divisao(num1, num2)

            print("Resultado:", resultado)

        except ValueError:
            print("Erro: Por favor, insira números válidos.")
    else:
        print("Erro: Opção inválida. Escolha uma opção entre 1 e 5.")
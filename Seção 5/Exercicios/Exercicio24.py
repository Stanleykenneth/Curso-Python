"""
24 - Uma empresa vende o mesmo produto para quatro diferentes estados.
     Cada estado possui uma taxa diferente de imposto sobre o produto
     (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuário
     entre com o valor e o estado destino do produto e o programa
     retorne o preço final do produto acrescido do imposto do estado em
     que ele será vendido. Se o estado digitado não for válido, mostra
     uma mensagem de erro.
"""

def preco_final(valor, estado):
    impostos = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}

    estado = estado.upper()

    if estado in impostos:
        preco_final = valor + (valor * impostos[estado])
        return preco_final
    else:
        return "Erro: Estado inválido."

valor_produto = float(input("Digite o valor do produto:\n R$"))
estado_destino = input("digite o valor de destino (MG, SP, RJ, MS):\n")

resultado = preco_final(valor_produto, estado_destino)

if isinstance(resultado, str):
    print(resultado)
else:
    print(f" O preço final do produto para o estado {estado_destino} é R$ {resultado:.2f}.")
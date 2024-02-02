"""
32 - Escrever um programa que leia o código de produto escolhido do cardápio de uma lanchonete e a quantidade.
     O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução será calculado um pedido.
     O cardápio da lanchonete segue o padrão:

     Especificação:                  Código:       Preço:
     Cachorro Quente                 100           1.20
     Bauru Simples                   101           1.30
     Bauru com Ovo                   102           1.50
     Hamburguer                      103           1.20
     Cheeseburguer                   104           1.70
     Suco                            105           2.20
     Refrigerante                    106           1.00
"""
print("")
def calcular_pedido(codigo, quantidade):
    cardapio = {
        100: ("Cachorro Quente", 1.20),
        101: ("Bauru Simples", 1.30),
        102: ("Bauru com Ovo", 1.50),
        103: ("Hamburguer", 1.20),
        104: ("Cheeseburguer", 1.70),
        105: ("Suco", 2.20),
        106: ("Refrigerante", 1.00),
    }

    if codigo in cardapio:
        nome_produto, preco_unitario = cardapio[codigo]
        total = quantidade * preco_unitario
        return nome_produto, quantidade, preco_unitario, total
    else:
        return None

print("Cardápio")
print("100 - Cachorro Quente - R$1.20")
print("101 - Bauru Simples - R$1.30")
print("102 - Bauru com Ovo - R$1.50")
print("103 - Hamburguer - R$1.20")
print("104 - Cheeseburguer - R$1.70")
print("105 - Suco - R$2.20")
print("106 - Refrigerante - R$1.00")
print("")

pedido = []

while True:
    codigo_pedido = int(input("\nDigite o código do produto (ou 0 para encerrar o pedido):\n "))

    if codigo_pedido == 0:
        break

    quantidade_pedido = int(input("Digite a quantidade desejada:\n "))

    produto = calcular_pedido(codigo_pedido, quantidade_pedido)

    if produto:
        pedido.append(produto)
        print(f"\nProduto adicionado ao pedido: {quantidade_pedido}x {produto[0]}")
    else:
        print("Código de produto inválido.")

# Exibir o resumo do pedido
if pedido:
    print("\nResumo do Pedido:")
    for produto in pedido:
        print(f"{produto[1]}x {produto[0]} - Preço Unitário: R${produto[2]:.2f} - Total: R${produto[3]:.2f}")
    total_pedido = sum(produto[3] for produto in pedido)
    print(f"\nTotal a Pagar: R${total_pedido:.2f}")
else:
    print("Pedido vazio.")

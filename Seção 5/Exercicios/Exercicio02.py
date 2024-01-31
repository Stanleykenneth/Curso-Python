"""
02 - Leia um números fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
     Se o número for negativo, mostre uma mensagem dizendo que o números é inválido.
"""
import  math

num = float(input('Digite um número:\n'))

if num > 0:
   raiz = round(math.sqrt(num), 2)
   print(f"A raiz quadra de {num} é {raiz}")
else:
    print("Número inválido. Por favor, forneca um número posistivo!")
"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(),metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
import utilidadesCeV.moeda as moeda
preco = float(input('Digite o preço: '))

print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(preco, 10)}')


"""
adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
"""
import utilidadesCeV.moeda as moeda
preco = float(input('Digite o preço: '))

print(f'A metade de {moeda(preco)} é {moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda(preco)} é {moeda(moeda.dobro(preco))}')
print(f'Aumentando 10%, temos {moeda(moeda.aumentar(preco, 10))}')
print(f'Diminuindo 10%, temos {moeda(moeda.diminuir(preco, 10))}')

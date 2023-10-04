"""
    Modifique as funções que foram criadas no desafio 107 para que ela aceitem mais de um parâmeto, a mais, informado se o valor retornado por eles vai ser ou não formatado pela função moeda(), desenvolvido no desafio108.
"""
import utilidadesCeV.moeda as moeda
preco = float(input('Digite o preço: '))

print(f'A metade de {moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(preco, 10, True)}')
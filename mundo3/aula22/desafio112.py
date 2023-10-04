"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma Função chamada leiaDinheiro() que seja capaz de de funcionar como uma input() mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""
from utilidadesCeV import dado
valor = dado.leiaDinheiro('Digite um valor monetário: ')
print(f'O valor digitado foi {valor:.2f}')
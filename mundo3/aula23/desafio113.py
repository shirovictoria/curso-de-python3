"""
Reescreva a função leiaInt() que fizemos no desafio 104, inlcuindo agora a possibilidade de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionabilidade.
"""
def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Valor inválido. Digite um número inteiro válido.')
def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('Valor inválido. Digite um número real válido.')
inteiro = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número inteiro {inteiro}')

flutuante = leiaFloat('Digite um número real: ')
print(f'Você digitou o número real {flutuante}')

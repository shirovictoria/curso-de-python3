"""
Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico.
Ex:
n = leiaInt('Digite um N')
"""
def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print('Valor inválido. Digite um número inteiro válido.')

n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')

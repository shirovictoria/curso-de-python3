"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) de 10 até 0. de 2 em 2
c) Uma contagem personalizada.
"""
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
    print()
print('Contagem de 1 até 10, de 1 em 1:')
contador(1, 10, 1)
print('\nContagem de 10 até 0, de 2 em 2:')
contador(10, 0, 2)
print('\nContagem personalizada:')
inicio = int(input('Digite o valor de início: '))
fim = int(input('Digite o valor de fim: '))
passo = int(input('Digite o valor do passo: '))
contador(inicio, fim, passo)

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
número = int(input('Digite um valor: '))
if número %2 == 0:
    print(f'O número {número} é PAR.')
else:
    print(f'O número {número} é ÍMPAR.')

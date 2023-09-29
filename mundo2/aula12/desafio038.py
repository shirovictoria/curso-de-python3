"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
"""
número1 = int(input('Digite o 1º número: '))
número2 = int(input('Digite o 2º número: '))
if número1 > número2:
    print(f'O número {número1} é maior do que {número2}.')
elif número2 > número1:
    print(f'O número {número2} é maior do que {número1}.')
else:
    print(f'Eles são iguais.')

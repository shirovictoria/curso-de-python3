# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética. No final mostre os 10 primeiros termos dessa progressão.
primeiro_termo = int(input('Digite o 1ª termo da Progressão Aritmética: '))
razão = int(input('Digite a razão da Progressão Aritmética: '))
for contador in range(1,11):
    print(f'{primeiro_termo + (contador - 1) * razão}')

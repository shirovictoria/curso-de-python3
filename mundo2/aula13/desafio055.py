# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos.
maior_peso = 0
menor_peso = 0

for contador in range(1,6):
    peso = float(input('Digite o seu peso: '))
    if contador == 1:
        maior_peso = peso
        menor_peso = peso
    elif maior_peso < peso:
        maior_peso = peso
    elif menor_peso > peso:
        menor_peso = peso
print(f'O maior peso foi [{maior_peso}] e o menor peso foi [{menor_peso}].')

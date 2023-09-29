# Faça um programa que leia três números e mostre qual é o maior e qual é o o menor.
contador = 1
maior_número = 0
menor_número = 0
while contador <=3:
    número = int(input(f'Digite o {contador}°: '))
    if contador == 1:
        maior_número = número
        menor_número = número
    elif maior_número < número:
        maior_número = número
    elif menor_número > número:
        menor_número = número
    contador+=1
print(f'O maior número foi: {maior_número} e o menor foi: {menor_número}.')

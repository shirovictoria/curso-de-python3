# Faça um programa que leia um número inteiro qualquer e mostre a sua tabuada.
número = int(input('Digite um número para mostrar a sua tabuada: '))
contador = 1
while contador <= 10:
    print(f'[{número}] X [{contador}] = [{número * contador}].')
    contador+=1

# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: Digite um número: 6.127 - O número 6.127 tem a parte inteira 6.
from math import trunc
número_real = float(input('Digite um número fracionado: '))
print(f'O número {número_real} tem a parte inteira: {trunc(número_real)}.')

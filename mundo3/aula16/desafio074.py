"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
import random
numeros_aleatorios = tuple(random.randint(1, 100) for _ in range(5))
print(f'Números gerados: {numeros_aleatorios}')
menor_valor = min(numeros_aleatorios)
maior_valor = max(numeros_aleatorios)
print(f'Menor valor na tupla: {menor_valor}')
print(f'Maior valor na tupla: {maior_valor}')

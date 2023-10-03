"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e sorteiaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro de uma lista e a segunda função vai mostrar a soma entre todos os valores PAREA sorteados pela função anterior.
"""
import random
numeros = []
def sorteia():
    for _ in range(5):
        numeros.append(random.randint(1, 10))
def somaPar(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma
sorteia()
print(f'Números sorteados: {numeros}')
soma_pares = somaPar(numeros)
print(f'Soma dos números pares: {soma_pares}')

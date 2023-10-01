"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
numeros = []
while True:
    numero = int(input('Digite um número (ou 0 para parar): '))
    
    if numero == 0:
        break
    
    numeros.append(numero)
quantidade = len(numeros)
numeros.sort(reverse=True)
contem_cinco = 5 in numeros
print(f'A) Quantidade de números digitados: {quantidade}')
print(f'B) Lista de valores em ordem decrescente: {numeros}')
print(f'C) O valor 5 {"está" if contem_cinco else "não está"} na lista.')

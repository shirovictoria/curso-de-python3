"""
    Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
    O programa será interropido quando o número solicitado for negativo.
"""
while True:
    numero = int(input('Digite um número para ver a sua tabuada (digite um número negativo para sair): '))
    if numero < 0:
        break
    print(f'Tabuada do {numero}:')
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')

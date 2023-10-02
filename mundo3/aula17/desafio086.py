"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação completa.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        valor = int(input(f'Digite o valor da posição [{i + 1}][{j + 1}]: '))
        matriz[i][j] = valor
print('Matriz 3x3:')
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=' ')
    print()

"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
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
soma_total = sum(sum(linha) for linha in matriz)
soma_terceira_coluna = sum(matriz[i][2] for i in range(3))
maior_valor_segunda_linha = max(matriz[1])
print(f'A) Soma de todos os valores digitados: {soma_total}')
print(f'B) Soma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'C) Maior valor da segunda linha: {maior_valor_segunda_linha}')

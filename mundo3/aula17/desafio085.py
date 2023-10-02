"""
Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""
valores_pares = []
valores_impares = []
for i in range(7):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)
valores_pares.sort()
valores_impares.sort()
print('Valores pares em ordem crescente:', valores_pares)
print('Valores ímpares em ordem crescente:', valores_impares)

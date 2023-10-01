"""
    Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista.
    CXaso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
valores_unicos = []
while True:
    valor = int(input('Digite um valor (ou 0 para sair): '))
    if valor == 0:
        break
    if valor not in valores_unicos:
        valores_unicos.append(valor)
valores_unicos.sort()
print('Valores únicos digitados (em ordem crescente):')
for valor in valores_unicos:
    print(valor, end=' ')

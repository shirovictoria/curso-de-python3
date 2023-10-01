"""
    Fala um programa que leia 5 valores númericos e guarde-os em uma lista.
    No final, mostre qual foi o maior valor e o menor valor digitado e as suas respectivas posições na lista.
"""
valores = []
for i in range(5):
    valor = float(input(f'Digite o {i + 1}º valor: '))
    valores.append(valor)
maior_valor = max(valores)
menor_valor = min(valores)
posicao_maior = valores.index(maior_valor)
posicao_menor = valores.index(menor_valor)
print(f'Valores digitados: {valores}')
print(f'Maior valor: {maior_valor} (Posição: {posicao_maior})')
print(f'Menor valor: {menor_valor} (Posição: {posicao_menor})')

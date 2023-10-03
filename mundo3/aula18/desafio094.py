"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada uma pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B)A média de idade do grupo
C)Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.
"""
# Lista para armazenar os dicionários de pessoas
pessoas = []
while True:
    pessoa = {}
    pessoa['Nome'] = input('Digite o nome da pessoa: ')
    pessoa['Sexo'] = input('Digite o sexo da pessoa (M/F): ').upper()
    pessoa['Idade'] = int(input('Digite a idade da pessoa: '))
    pessoas.append(pessoa)
    continuar = input('Deseja cadastrar outra pessoa? (S/N): ').upper()
    if continuar != 'S':
        break
soma_idades = 0
total_pessoas = len(pessoas)
mulheres = []
acima_da_media = []
for pessoa in pessoas:
    soma_idades += pessoa['Idade']
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
media_idade = soma_idades / total_pessoas
for pessoa in pessoas:
    if pessoa['Idade'] > media_idade:
        acima_da_media.append(pessoa['Nome'])
print(f'\nForam cadastradas {total_pessoas} pessoas.')
print(f'A média de idade do grupo é de {media_idade:.1f} anos.')
print(f'Mulheres cadastradas: {", ".join(mulheres)}')
print(f'Pessoas com idade acima da média: {", ".join(acima_da_media)}')

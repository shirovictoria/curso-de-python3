"""
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
pessoas = []
maior_peso = menor_peso = 0
while True:
    nome = input('Digite o nome da pessoa (ou digite "sair" para parar): ')
    if nome.lower() == 'sair':
        break
    peso = float(input('Digite o peso da pessoa (em kg): '))
    pessoa = (nome, peso)
    pessoas.append(pessoa) 
    
    if peso > maior_peso or maior_peso == 0:
        maior_peso = peso
    if peso < menor_peso or menor_peso == 0:
        menor_peso = peso
quantidade = len(pessoas)
pessoas_pesadas = [pessoa for pessoa in pessoas if pessoa[1] == maior_peso]
pessoas_leves = [pessoa for pessoa in pessoas if pessoa[1] == menor_peso]
print(f'A) Quantidade de pessoas cadastradas: {quantidade}')
print(f'B) Pessoas mais pesadas:')
for nome, peso in pessoas_pesadas:
    print(f'   Nome: {nome}, Peso: {peso} kg')
print(f'C) Pessoas mais leves:')
for nome, peso in pessoas_leves:
    print(f'   Nome: {nome}, Peso: {peso} kg')

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
nome_da_cidade = input('Digite o nome da cidade: ')
primeiro_nome = nome_da_cidade[:5].upper()
print(f'A cidade tem o nome Santo no começo? R: {"SANTO" in primeiro_nome}.')



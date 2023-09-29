# Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas. - O nome com todas minúsculas. - Quantas letras ao todo (sem considerar o espaços). - Quantas letras tem o primeiro nome.
nome_completo = input('Digite o seu nome completo: ')
primeiro_nome = nome_completo.split()[0]
nome_sem_espaços = nome_completo.replace(" ", "")
print(f'Seu nome completo em maíusculas: {nome_completo.upper()}.')
print(f'Seu nome completo em minúsculas: {nome_completo.lower()}.')
print(f'A quantidade de caracteres de seu nome completo sem espaços: {len(nome_sem_espaços)} letras.')
print(f'E seu primeiro nome tem {len(primeiro_nome)} letras.')

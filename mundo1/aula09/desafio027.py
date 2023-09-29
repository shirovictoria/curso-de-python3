# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Sousa, primeiro = Ana, último = Sousa.
nome_completo = input('Digite o nome completo: ')
primeiro_nome = nome_completo.split()[0]
último_nome = nome_completo.split()[-1]
print(f'O seu primeiro nome é {primeiro_nome} e o seu último é {último_nome}.')

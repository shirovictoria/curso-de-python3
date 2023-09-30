"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No Final Mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""
maiores_de_idade = homens_cadastrados = mulheres_menos_de_20 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()
    if idade > 18:
        maiores_de_idade += 1
    if sexo == 'M':
        homens_cadastrados += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menos_de_20 += 1
    continuar = input('Deseja continuar cadastrando? [S/N]: ').strip().upper()
    if continuar != 'S':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores_de_idade}')
print(f'Total de homens cadastrados: {homens_cadastrados}')
print(f'Total de mulheres com menos de 20 anos: {mulheres_menos_de_20}')

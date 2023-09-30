"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    - A média de idade do Grupo
    - Qual é o nome do homem mais velho.
    - Quantas mulheres têm menos de 20 anos.
"""
idades = 0
nome_do_homem_mais_velho = 'Lorem Ipsum'
mulheres_com_menos_de_20 = 0 
idade_do_homem_mais_velho = 0
for contador in range(1,5):
    nome = input('Digite o seu nome')
    idade = int(input('Digite a sua idade: '))
    idades+=idade
    sexo = input("Digite o seu sexo [M/F]: ").upper()
    if idade < 20 and sexo == 'F':
        mulheres_com_menos_de_20+=1
    elif idade_do_homem_mais_velho < idade and sexo == 'M':
        idade_do_homem_mais_velho = idade
        nome_do_homem_mais_velho = nome
print(f'O nome do homem mais velho é {nome_do_homem_mais_velho} com a idade de {idade_do_homem_mais_velho} anos. A média de idade do grupo é de {idades/4:.2f} e possui {mulheres_com_menos_de_20} mulheres com menos de 20 anos.')

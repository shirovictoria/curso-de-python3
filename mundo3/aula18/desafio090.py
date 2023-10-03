"""
Faça um programa que leia nome e média de um aluno, guardando também a sua situação em um dicionário.
No final mostre o contéudo da estrutura na tela.
"""
def determinar_situacao(media):
    if media >= 7.0:
        return 'Aprovado'
    elif media >= 5.0:
        return 'Recuperação'
    else:
        return 'Reprovado'
aluno = {}
aluno['Nome'] = input('Digite o nome do aluno: ')
aluno['Média'] = float(input('Digite a média do aluno: '))
aluno['Situação'] = determinar_situacao(aluno['Média'])
print('\nDados do aluno:')
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')

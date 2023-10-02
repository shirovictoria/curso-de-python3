"""
Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
def calcular_media(notas):
    return sum(notas) / len(notas)
alunos = []

while True:
    nome = input('Digite o nome do aluno (ou "sair" para parar): ')
    if nome.lower() == 'sair':
        break
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    aluno = [nome, [nota1, nota2]]
    alunos.append(aluno)

print('\nBoletim:')
for i, aluno in enumerate(alunos, start=1):
    nome = aluno[0]
    notas = aluno[1]
    media = calcular_media(notas)
    print(f'Aluno {i}: {nome}, Média: {media:.2f}')
while True:
    escolha = input('Deseja ver as notas individuais de um aluno? (s/n): ')
    if escolha.lower() == 'n':
        break
    if escolha.lower() == 's':
        indice = int(input('Digite o número do aluno: '))
        if 1 <= indice <= len(alunos):
            aluno = alunos[indice - 1]
            nome = aluno[0]
            notas = aluno[1]
            print(f'Notas de {nome}: {notas[0]} e {notas[1]}')
        else:
            print('Número de aluno inválido.')
    else:
        print('Opção inválida. Digite "s" para sim ou "n" para não.')

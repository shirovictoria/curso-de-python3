# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um prorgama que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
contador = 1
nome_dos_alunos = []
while contador <=4:
    nome = input((f'Escreva o nome do {contador}°: '))
    nome_dos_alunos.append(nome)
    contador+=1
print(f'O aluno escolhido foi: {choice(nome_dos_alunos)}.')

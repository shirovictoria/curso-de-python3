# O mesmo professor do desafio anterior, quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.
from random import shuffle
contador = 1
nome_dos_alunos = []
while contador <=4:
    nome = input((f'Escreva o nome do {contador}°: '))
    nome_dos_alunos.append(nome)
    contador+=1
shuffle(nome_dos_alunos)
print(f'A ordem de apresentação é : {nome_dos_alunos}.')

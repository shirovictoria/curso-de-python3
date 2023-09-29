# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
reta_1 = int(input('Digite a 1ª reta: '))
reta_2 = int(input('Digite a 2ª reta: '))
reta_3 = int(input('Digite a 3ª reta: '))
if reta_1 + reta_2 > reta_3 and reta_1 + reta_3 > reta_2 and reta_2 + reta_3 > reta_1:
    print(f'As retas: {reta_1},{reta_2} e {reta_3} podem formar um triângulo.')
else:
    print(f'As retas: {reta_1},{reta_2} e {reta_3} não podem formar um triângulo.')

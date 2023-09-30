# Faça um programa que leia um número qualquer e mostre o seu fatorial. EX: 5! 5x4x3x2x1.
numero = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1
contador = numero

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f'{numero}! = {fatorial}')

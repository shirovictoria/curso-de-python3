"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar digitar valores.
"""
maior = menor = total = contador = 0
continuar = 'S'
while continuar == 'S':
    numero = int(input('Digite um número inteiro: '))
    if contador == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    total += numero
    contador += 1
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
print(f'Você digitou os números:')
for i in range(contador):
    print(total, end=' ' if i < contador - 1 else '\n')
print(f'O maior valor digitado foi {maior}.')
print(f'O menor valor digitado foi {menor}.')

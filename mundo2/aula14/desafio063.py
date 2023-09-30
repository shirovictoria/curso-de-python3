# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci. Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
n = int(input('Digite a quantidade de termos da sequência de Fibonacci que você deseja mostrar: '))
termo_anterior = 0
termo_atual = 1

contador = 0

while contador < n:
    print(termo_anterior, end=' -> ')
    novo_termo = termo_anterior + termo_atual
    termo_anterior = termo_atual
    termo_atual = novo_termo
    contador += 1

print('Fim')

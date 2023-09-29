# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. Exemplo Digite um número: 1834 - unidade 4, dezena 3, centena 8, milhar 1.
número_digitado = int(input('Digite um número entre 0 e 9999: '))
unidade = número_digitado % 10
dezena = (número_digitado % 100) // 10
centena = (número_digitado % 1000) // 100
unidade_de_milhar = número_digitado // 1000
print(f'Unidade: [{unidade}].')
print(f'Dezena: [{dezena}]')
print(f'Centena: [{centena}].')
print(f'Milhar: [{unidade_de_milhar}].')

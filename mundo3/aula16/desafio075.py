"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final Mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
valores = tuple(int(input(f'Digite o {i + 1}º valor: ')) for i in range(4))
quantidade_de_noves = valores.count(9)
print(f'A) O valor 9 apareceu {quantidade_de_noves} vezes.')
if 3 in valores:
    primeira_posicao_do_tres = valores.index(3) + 1
    print(f'B) O primeiro valor 3 foi digitado na posição {primeira_posicao_do_tres}.')
else:
    print('B) O valor 3 não foi digitado.')
numeros_pares = [valor for valor in valores if valor % 2 == 0]
print(f'C) Os números pares digitados foram: {numeros_pares}')

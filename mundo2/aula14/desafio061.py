# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma Progressão Aritmética, mostrando os 10 primeiros termos da progressão usando a estrutura while.
primeiro_termo = int(input('Digite o 1º termo da Progressão Aritmética: '))
razao = int(input('Digite a razão da Progressão Aritmética: '))

contador = 0
termo_atual = primeiro_termo

while contador < 10:
    print(f'Termo {contador + 1}: {termo_atual}')
    termo_atual += razao
    contador += 1

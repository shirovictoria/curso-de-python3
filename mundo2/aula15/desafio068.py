"""
    Faça um programa que jogue par ou ímpar com o computador.
    O jogo só será interropido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
import random
vitorias_consecutivas = 0
while True:
    jogador = input('Escolha par (P) ou ímpar (I): ').strip().upper()
    if jogador not in ['P', 'I']:
        print('Escolha inválida. Digite "P" para par ou "I" para ímpar.')
        continue
    numero_jogador = int(input('Digite um número: '))
    numero_computador = random.randint(1, 10)
    total = numero_jogador + numero_computador
    resultado = "PAR" if total % 2 == 0 else "ÍMPAR"
    print(f'Você escolheu {jogador}.')
    print(f'Você jogou {numero_jogador} e o computador jogou {numero_computador}.')
    print(f'O total é {total}, que é {resultado}.')
    if (jogador == 'P' and resultado == 'PAR') or (jogador == 'I' and resultado == 'ÍMPAR'):
        print('Você venceu!')
        vitorias_consecutivas += 1
    else:
        print('Você perdeu!')
        break
print(f'Você conquistou {vitorias_consecutivas} vitórias consecutivas.')

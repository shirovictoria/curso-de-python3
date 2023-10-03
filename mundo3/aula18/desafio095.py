"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogado.
"""
jogadores = []
while True:
    jogador = {}
    jogador['Nome'] = input('Digite o nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols_por_partida = []
    total_gols = 0
    for partida in range(1, partidas + 1):
        gols = int(input(f'Quantos gols {jogador["Nome"]} fez na partida {partida}? '))
        gols_por_partida.append(gols)
        total_gols += gols
    jogador['Gols por Partida'] = gols_por_partida
    jogador['Total de Gols'] = total_gols
    jogadores.append(jogador)
    continuar = input('Deseja cadastrar outro jogador? (S/N): ').upper()
    if continuar != 'S':
        break
print('\nAproveitamento de cada jogador:')
for i, jogador in enumerate(jogadores):
    print(f'\nJogador {i + 1}:')
    print(f'Nome: {jogador["Nome"]}')
    print(f'Total de Gols: {jogador["Total de Gols"]}')
    print(f'Gols por Partida: {", ".join(map(str, jogador["Gols por Partida"]))}')

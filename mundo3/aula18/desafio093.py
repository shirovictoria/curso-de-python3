"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = {}
jogador['Nome'] = input('Digite o nome do jogador: ')
partidas = int(input('Digite a quantidade de partidas jogadas: '))
gols_por_partida = []
total_gols = 0
for partida in range(1, partidas + 1):
    gols = int(input(f'Digite a quantidade de gols na partida {partida}: '))
    gols_por_partida.append(gols)
    total_gols += gols
jogador['Gols por Partida'] = gols_por_partida
jogador['Total de Gols'] = total_gols
print('\nAproveitamento do jogador:')
for chave, valor in jogador.items():
    print(f'{chave}: {valor}')

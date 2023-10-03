"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
def ficha(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
nome_jogador = input('Digite o nome do jogador: ')
gols_jogador = input('Digite a quantidade de gols: ')
if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
    ficha(nome_jogador, gols_jogador)
else:
    ficha(nome_jogador)

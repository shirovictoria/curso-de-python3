"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perrguntar quantos jogos serão gerados e vai sortear 6 números ebtre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
import random
def gerar_jogo():
    return sorted(random.sample(range(1, 61), 6))
quantidade_jogos = int(input('Quantos jogos você deseja gerar? '))
jogos = []
for _ in range(quantidade_jogos):
    jogo = gerar_jogo()
    jogos.append(jogo)
print(f'Palpites gerados:')
for i, jogo in enumerate(jogos, start=1):
    print(f'Jogo {i}: {jogo}')

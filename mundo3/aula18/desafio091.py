"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.
"""
import random
def jogar_dado():
    return random.randint(1, 6)
resultados = {}
for jogador in range(1, 5):
    resultado = jogar_dado()
    resultados[f'Jogador {jogador}'] = resultado
print('Resultados dos jogadores:')
for jogador, resultado in resultados.items():
    print(f'{jogador}: {resultado}')
vencedor = max(resultados, key=resultados.get)
print(f'\nO vencedor é: {vencedor} com o resultado {resultados[vencedor]}.')

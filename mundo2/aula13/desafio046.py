# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 a 0, com uma psusa de 1 segundo entre eles.
from time import sleep
for contador in range(10, 0, -1):
    print(f'{contador}')
    sleep(1)
print("FOGOS!")

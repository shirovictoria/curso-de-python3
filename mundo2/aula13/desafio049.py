# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
número = int(input('Digite o número da tabuada que você deseva ver: '))
for contador in range(1, 11):
    print(f'[{número}] X [{contador}] = [{número * contador}].')

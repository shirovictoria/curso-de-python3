"""
Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta, de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""
valores = []
for i in range(5):
    valor = int(input('Digite um valor: '))
    posicao = 0
    while posicao < len(valores) and valor > valores[posicao]:
        posicao += 1
    valores.insert(posicao, valor)
print('Lista ordenada:')
print(valores)

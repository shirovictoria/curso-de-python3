# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1.00 = R$3.27
reais = float(input('Digite quanto você tem na carteira: R$'))
print(f'Com R${reais:.2f} dá para comprar US${reais/3.27:.2f}.')

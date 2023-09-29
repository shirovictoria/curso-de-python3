# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Digite o preço do produto: '))
desconto_de_5_porcento = preço - (preço * 5) / 100
print(f'O produto custava R${preço}, agora com 5% de desconto ficou R${desconto_de_5_porcento}.')

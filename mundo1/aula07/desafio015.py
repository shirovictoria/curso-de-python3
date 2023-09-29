# Crie um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.
dias_alugados = int(input('Quantos dias o carro foi alugado: '))
km_rodados = float(input('Quantos kms o carro foi rodado: '))
print(f'O total a pagar é de R${(dias_alugados * 60 + km_rodados * 0.15):.2f}')

# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200km e R$0.45 para viagens mais longas.
distância_em_km = float(input('Digite a distância em Km: '))
if distância_em_km <= 200:
    preço_da_passagem = distância_em_km * 0.50
    print(f'O preço da passagem é: R${preço_da_passagem:.2f}.')
else:
    preço_da_passagem = distância_em_km * 0.45
    print(f'O preço da passagem é: R${preço_da_passagem:.2f}.')

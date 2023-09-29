# Escreva um programa que converta uma temperatura digitada em C° e converta para F°.
temperatura_em_C = float(input('Digite a temperatura em C° para ser convertida em F°: '))
temperatura_em_F = (temperatura_em_C * 9/5) + 32
print(f'A temperatura {temperatura_em_C}C° em F° é igual a: {temperatura_em_F}F°.')

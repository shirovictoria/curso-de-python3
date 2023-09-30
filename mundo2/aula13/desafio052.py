número_digitado = int(input('Digite um número para ver se ele é primo ou não: '))
quantidade_de_divisores = 0

for contador in range(1, número_digitado + 1):
    if número_digitado % contador == 0:
        quantidade_de_divisores += 1

if quantidade_de_divisores == 2:
    print(f'{número_digitado} é um número primo.')
else:
    print(f'{número_digitado} não é um número primo.')

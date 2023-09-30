# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e qie se encontram no intervalo de 1 até 500.
soma = 0
for contador in range(1,501):
    if contador%2 != 0 and contador% 3 == 0:
        soma+=contador
print(f'A soma deu {soma}.')

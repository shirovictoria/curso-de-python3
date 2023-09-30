# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
for contador in range(1,7):
    valor = int(input(f'Digite o {contador}° valor: '))
    if valor%2 == 0:
        soma+=valor
print(f'A soma dos valores pares deu {soma}!')

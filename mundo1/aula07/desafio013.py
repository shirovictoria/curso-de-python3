# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input('Digite o seu salário R$: '))
novo_salário = salário + (salário * 15) / 100
print(f'O seu salário era de R${salário}, com o aumento de 15% ficou R${novo_salário}.')
 
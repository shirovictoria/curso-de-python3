# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários superiores a R$1.250.00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salário = float(input('Digite o seu salário: '))
if salário <= 1250:
    aumento = (salário * 15) / 100
    print(f'Agora seu salário com aumento de 15% vai ficar R${salário + aumento}.')
else:
    aumento = (salário * 10) / 100
    print(f'Agora seu salário com aumento de 10% vai ficar R${salário + aumento}.')


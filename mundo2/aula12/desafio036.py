"""
Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""
from colorama import just_fix_windows_console, Fore
just_fix_windows_console()
cor_vermelha = Fore.RED
cor_verde = Fore.GREEN
resetar_cor = Fore.RESET
valor_da_casa = float(input('Digite o valor da casa R$: '))
salário_do_usuário = float(input('Digite o valor de seu salário R$: '))
anos_de_pagamento = int(input('Digite em quantos anos deseja pagar a casa: '))
trinta_porcento_do_salário = (salário_do_usuário * 30) / 100
prestações = anos_de_pagamento * 12
valor_das_parcelas = valor_da_casa / prestações
if valor_das_parcelas <= trinta_porcento_do_salário:
    print(f'{cor_verde}EMPRESTIMO APROVADO!{cor_verde}{resetar_cor} Ficou {prestações}x de {valor_das_parcelas:.2f}.')
else:
    print(f'{cor_vermelha}EMPRESTIMO NEGADO!{cor_vermelha}{resetar_cor} A parcela ficou R${valor_das_parcelas:.2f} que está acima de 30% de seu salário!')

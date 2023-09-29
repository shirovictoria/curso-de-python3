"""
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
- Até 9 anos: Mirin
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
"""
from datetime import date
ano_atual = date.today().year
ano_de_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_de_nascimento
if idade <= 9:
    print(f'Com {idade} anos você está na categoria: MIRIN.')
elif idade <= 14:
    print(f'Com {idade} anos você está na categoria: INFANTIL.')
elif idade <= 19:
    print(f'Com {idade} anos você está na categoria: JUNIOR.')
elif idade <= 20:
    print(f'Com {idade} anos você está na categoria: SÊNIOR.')
else:
    print(f'Com {idade} anos você está na categoria: MASTER.')

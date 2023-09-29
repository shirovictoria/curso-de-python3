"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou o tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
ano_atual = date.today().year
ano_de_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_de_nascimento
if idade < 18:
    print(f'Você deve se alistar daqui {18 - idade} anos.')
elif idade == 18:
    print(f'Você tem 18 anos, está na hora de se alistar!')
else:
    print(f'Você tem {idade} anos e tá atrasado o alistamento em {idade - 18} anos.')

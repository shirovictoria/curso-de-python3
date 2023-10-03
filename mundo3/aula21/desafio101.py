"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
"""
def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return 'Voto Negado'
    elif 16 <= idade < 18 or idade >= 70:
        return 'Voto Opcional'
    else:
        return 'Voto Obrigatório'
ano_nascimento = int(input('Digite o ano de nascimento: '))
resultado = voto(ano_nascimento)
print(f'Situação do voto: {resultado}')

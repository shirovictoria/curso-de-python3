"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionárior receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade
pessoa = {}
pessoa['Nome'] = input('Digite o nome: ')
ano_nascimento = int(input('Digite o ano de nascimento: '))
pessoa['Idade'] = calcular_idade(ano_nascimento)
pessoa['CTPS'] = int(input('Digite o número da Carteira de Trabalho (0 se não tiver): '))
if pessoa['CTPS'] != 0:
    pessoa['Ano de Contratação'] = int(input('Digite o ano de contratação: '))
    pessoa['Salário'] = float(input('Digite o salário: '))
    anos_contribuicao = date.today().year - pessoa['Ano de Contratação']
    idade_aposentadoria = pessoa['Idade'] + (35 - anos_contribuicao)
    pessoa['Idade de Aposentadoria'] = idade_aposentadoria
print('\nDados da Pessoa:')
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')

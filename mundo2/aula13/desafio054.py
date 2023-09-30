# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas j[a são maiores.
from datetime import date
maiores_de_idade = 0
menores_de_idade = 0
ano_atual = date.today().year
for contador in range(1, 8):
    ano_de_nascimento = int(input(f'Digite o ano de nascimento da pessoa {contador}°: '))
    if ano_atual - ano_de_nascimento >= 18:
        maiores_de_idade+=1
    else:
        menores_de_idade+=1
print(f'Existem [{maiores_de_idade}] maiores de idade e [{menores_de_idade}] menores de idade!')

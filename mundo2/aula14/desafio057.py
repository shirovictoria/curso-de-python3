# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até um valor correto.
resposta = True
while resposta == True:
    sexo = input('Digite o sexo da pessoa [M/F]: ').upper()
    if sexo[0] != 'M' and sexo[0] != 'F':
        print(f'Você digitou {sexo}, é um valor inválido!')
    else:
        resposta = False
print(f'Você é do sexo {sexo}.')
    

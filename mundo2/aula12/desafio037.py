"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
from colorama import just_fix_windows_console, Fore
just_fix_windows_console()
cor_vermelha = Fore.RED
resetar_cor = Fore.RESET
número_digitado = int(input('Digite um número: '))
print(f"""
Você quer converter o valor {número_digitado} para qual base:
[ 1 ] - Binário.
[ 2 ] - Octal.
[ 3 ] - Hexadecimal.
""")
opção = int(input('Digite a opção que você escolheu: '))
if opção == 1:
    print(f'O número {número_digitado} em Binário é [{bin(número_digitado)[2:]}].')
elif opção == 2:
    print(f'O número {número_digitado} em Octal é [{oct(número_digitado)[2:]}].')
elif opção == 3:
    print(f'O número {número_digitado} em Hexadecimal é [{hex(número_digitado)[2:]}].')
else:
    print(f'{cor_vermelha}O valor {opção} não foi reconhecido!{cor_vermelha}{resetar_cor}')


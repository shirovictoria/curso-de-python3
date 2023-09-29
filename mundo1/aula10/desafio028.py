# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido  pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from colorama import just_fix_windows_console,Fore
just_fix_windows_console()
texto_vermelho = Fore.RED
texto_verde = Fore.GREEN
resetar_cor = Fore.RESET
from random import randint
número_pensado = randint(0, 5)
número_digitado = int(input('Eu pensei um número entre 0 e 5: Tente adivinhar qual pensei: '))
if número_pensado == número_digitado:
    print(f'{texto_verde}VOCÊ ACERTOU!{texto_verde}{resetar_cor} Realmente pensei no número {número_digitado}.')
else:
    print(f'{texto_vermelho}VOCÊ ERROU!{texto_vermelho}{resetar_cor} Tinha digitado {número_digitado} mas eu pensei no número {número_pensado}.')
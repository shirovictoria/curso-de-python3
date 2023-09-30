"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantas tentativas foram nescessárias para vencer. 
"""
from colorama import just_fix_windows_console,Fore
just_fix_windows_console()
jogo_iniciado = True
número_de_tentativas = 0
texto_vermelho = Fore.RED
texto_verde = Fore.GREEN
resetar_cor = Fore.RESET
from random import randint
número_pensado = randint(0, 10)
while jogo_iniciado == True:
    número_digitado = int(input('Eu pensei um número entre 0 e 10: Tente adivinhar qual pensei: '))
    if número_pensado == número_digitado:
        print(f'{texto_verde}VOCÊ ACERTOU!{texto_verde}{resetar_cor} Realmente pensei no número {número_digitado} e você tentou {número_de_tentativas} vezes para acertar o número que pensei!.')
        jogo_iniciado = False
    else:
        print(f'{texto_vermelho}VOCÊ ERROU!{texto_vermelho}{resetar_cor} Tinha digitado {número_digitado} mas eu pensei em outro número, tente novamente!.')
        número_de_tentativas+=1
"""
Faça um mini-sistema que utlize o Interactive Help do  Python.
O usuário vai digitar o commando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: Use cores;
"""
import pydoc
from colorama import Fore, Style

while True:
    comando = input('Digite um comando ou "FIM" para sair: ')

    if comando.upper() == 'FIM':
        break

    try:
        help_text = pydoc.render_doc(comando)
        print(f'{Fore.GREEN}{help_text}{Style.RESET_ALL}')
    except ImportError:
        print(f'{Fore.RED}Comando não encontrado. Digite "FIM" para sair.{Style.RESET_ALL}')

print('Programa encerrado.')

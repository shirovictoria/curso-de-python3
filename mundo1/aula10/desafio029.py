# Escreva um programa que leia a velocidade de um carro. Se ele tiver ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ por cada KM acima do limite.
from colorama import just_fix_windows_console, Fore
just_fix_windows_console()
texto_vermelho = Fore.RED
resetar_cor = Fore.RESET
km_por_h = int(input('Digite quantos Km está o carro: '))
if km_por_h <=80:
    print(f'O carro está {km_por_h}km.')
else:
    valor_da_multa = (km_por_h - 80) * 7.00
    print(f'{texto_vermelho}MULTADO!{texto_vermelho}{resetar_cor} Você foi multado em {texto_vermelho}R${valor_da_multa:.2f}{texto_vermelho}{resetar_cor}.')

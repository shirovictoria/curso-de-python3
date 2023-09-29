"""
Crie um programa qie leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0:
REPROVADO
- Média entre 5.0 e 6.9:
RECUPERAÇÃO
- Média 7.0 ou superior:
APROVADO
"""
from colorama import just_fix_windows_console, Fore
just_fix_windows_console()
letra_vermelha = Fore.RED
letra_amarela = Fore.YELLOW
letra_verde = Fore.GREEN
resetar_cor = Fore.RESET
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
média = (nota1 + nota2) / 2
if média < 5:
    print(f'{letra_vermelha}VOCÊ FOI REPROVADO!{letra_vermelha}{resetar_cor} Sua média foi {média:.2f}.')
elif média >= 5 and média <= 6.9:
    print(f'{letra_amarela}VOCÊ ESTÁ DE RECUPERAÇÃO!{letra_amarela}{resetar_cor} Sua média foi {média:.2f}.')
else:
    print(f'{letra_verde}VOCÊ FOI APROVADO!{letra_verde}{resetar_cor} Sua média foi {média:.2f}.')

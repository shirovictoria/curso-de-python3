# crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
opções = ['Pedra','Papel','Tesoura']
opção_da_maquina = choice(opções)
print("""
Vamos jogar Jokenpô! Escolha uma dessas opções:
      [ 1 ] Pedra.
      [ 2 ] Papel.
      [ 3 ] Tesoura.
""")
opção_do_usuário = input('Digite o nome de sua opção: ').title()
if opção_do_usuário != 'Pedra' and  opção_do_usuário != 'Papel' and opção_do_usuário != 'Tesoura':
    print(f'A opção {opção_do_usuário} é inválida!')
elif opção_do_usuário	 == opção_da_maquina:
    print(f'Você escolheu {opção_do_usuário} e eu {opção_da_maquina}, empatamos!')
elif opção_do_usuário == 'Pedra' and opção_da_maquina == 'Tesoura':
    print(f'Você escolheu {opção_do_usuário} e eu {opção_da_maquina}, você ganhou!')
elif opção_do_usuário == 'Papel' and opção_da_maquina == 'Pedra':
    print(f'Você escolheu {opção_do_usuário} e eu {opção_da_maquina}, você ganhou!')
elif opção_do_usuário == 'Tesoura' and opção_da_maquina == 'Papel':
    print(f'Você escolheu {opção_do_usuário} e eu {opção_da_maquina}, você ganhou!')
elif opção_da_maquina == opção_do_usuário:
    print(f'Você escolheu {opção_do_usuário} e eu {opção_da_maquina}, empatamos')
else:
    print(f'Você escolheu {opção_do_usuário} e eu {opção_da_maquina}, Você perdeu!')

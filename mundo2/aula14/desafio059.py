"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do programa
"""
iniciar_programa = True
número_1 = int(input('Digite o primeiro número: '))
número_2 = int(input('Digite o segundo número: '))
while iniciar_programa == True:
    print("""
    Escolha uma das opções:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do programa
""")
    opção_escolhida = int(input('Digite aqui a opção escolhida: '))
    if opção_escolhida == 1:
        print(f'A soma entre {número_1} e {número_2} é igual {número_1 + número_2}.')
    elif opção_escolhida == 2:
        print(f'A multiplicação  entre {número_1} e {número_2} é igual {número_1 * número_2}.')
    elif opção_escolhida == 3:
        if número_1 > número_2:
            print(f'O maior número entre {número_1} e {número_2} é {número_1}.')
        else:
            print(f'O maior número entre {número_1} e {número_2} é {número_2}.')
    elif opção_escolhida == 4:
        número_1 = int(input('Digite o primeiro número: '))
        número_2 = int(input('Digite o segundo número: '))
    elif opção_escolhida == 5:
        iniciar_programa = False
    else:
        print(f'A opção escolhida {opção_escolhida} é inválida!')

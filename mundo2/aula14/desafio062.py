# melhore o DESAFIO 061, perguntando opara o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
primeiro_termo = int(input('Digite o 1º termo da Progressão Aritmética: '))
razao = int(input('Digite a razão da Progressão Aritmética: '))

contador = 0
termo_atual = primeiro_termo
termos_extras = 10 

while termos_extras != 0:
    while contador < termos_extras:
        print(f'Termo {contador + 1}: {termo_atual}')
        termo_atual += razao
        contador += 1
    termos_extras = int(input('Quantos termos extras você deseja mostrar? (0 para encerrar): '))
    contador = 0

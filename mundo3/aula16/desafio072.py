"""
    Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
    Seu prograna deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
# Tupla com números por extenso de zero até vinte
numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)
numero = int(input('Digite um número entre 0 e 20: '))
if 0 <= numero <= 20:
    extenso = numeros_por_extenso[numero]
    print(f'O número {numero} por extenso é: {extenso}')
else:
    print('Número fora do intervalo válido.')

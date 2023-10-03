"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: O primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cáculo fatorial.
"""
def fatorial(numero, show=False):
    """
    Calcula o fatorial de um número.

    :param numero: O número para o qual calcular o fatorial.
    :param show: Um valor lógico (True/False) para mostrar ou não o processo de cálculo.
    :return: O valor do fatorial do número.
    """
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
        if show:
            if i == 1:
                processo = f'{i} '
            else:
                processo += f'x {i} '
    if show:
        return f'{numero}! = {processo}= {resultado}'
    else:
        return resultado

numero = int(input('Digite um número para calcular o fatorial: '))
mostrar_processo = input('Deseja mostrar o processo de cálculo? (S/N): ').strip().upper()

if mostrar_processo == 'S':
    resultado = fatorial(numero, show=True)
else:
    resultado = fatorial(numero)

print(resultado)

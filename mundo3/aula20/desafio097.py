"""
Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parâmetro e mostre uma mensagem com o tamanho adaptável.
Ex: escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""
def escreva(texto):
    tamanho_linha = len(texto) + 4
    print('~' * tamanho_linha)
    print(f'  {texto}')
    print('~' * tamanho_linha)

texto = input('Digite o texto que deseja exibir: ')
escreva(texto)

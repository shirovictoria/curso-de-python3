"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
def verifica_balanceamento(expressao):
    pilha = []
    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha:
                return False
            pilha.pop()  
    return not pilha 
expressao = input('Digite uma expressão com parênteses: ')
if verifica_balanceamento(expressao):
    print('A expressão está com os parênteses balanceados.')
else:
    print('A expressão não está com os parênteses balanceados.')

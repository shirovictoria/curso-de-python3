"""
Faça um prorgama que tenha uma função chamada maior(), que recebe vários parâmetros com valores inteiros.
Seu prorgama tem que analisar todos os valores e dizer qual deles é o maior.
"""
def maior(*valores):
    if len(valores) == 0:
        return None
    
    maior_valor = valores[0]
    
    for valor in valores:
        if valor > maior_valor:
            maior_valor = valor
    
    return maior_valor

# Exemplos de uso da função
resultado1 = maior(4, 8, 2, 10, 6)
resultado2 = maior(15, 27, 12)
resultado3 = maior()

print(f'O maior valor é {resultado1}')
print(f'O maior valor é {resultado2}')
print(f'O maior valor é {resultado3}')

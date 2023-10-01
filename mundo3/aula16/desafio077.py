"""
Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""# Tupla com várias palavras
palavras = ("python", "programação", "computador", "algoritmo", "linguagem")
def vogais_da_palavra(palavra):
    vogais = ""
    for letra in palavra:
        if letra in "aeiou":
            vogais += letra
    return vogais
for palavra in palavras:
    vogais = vogais_da_palavra(palavra)
    print(f'Vogais de "{palavra}": {vogais}')

"""
Refaça o DESAFIO 035 dos triângulos , acrecentando o recurso de mostrar que tipo de triângulo será fromado:
- Equilátero: Todos os lados iguais.
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes.
"""
reta_1 = int(input('Digite a 1ª reta: '))
reta_2 = int(input('Digite a 2ª reta: '))
reta_3 = int(input('Digite a 3ª reta: '))
if reta_1 + reta_2 > reta_3 and reta_1 + reta_3 > reta_2 and reta_2 + reta_3 > reta_1:
    print(f'As retas: {reta_1},{reta_2} e {reta_3} podem formar um triângulo.')
    if reta_1 == reta_2 and reta_2 == reta_3:
        print("Os valores anteriores formam um triângulo Equilátero!")
    elif reta_1 == reta_2 or reta_2 == reta_3 or reta_1 == reta_3:
        print('Os valores anteriores formam um triângulo Isóceles! ')
    else:
        print('Os valores anteriores formam um triângulo Escaleno!')
else:
    print(f'As retas: {reta_1},{reta_2} e {reta_3} não podem formar um triângulo.')

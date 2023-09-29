# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
comprimento_da_hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'O comprimento da hipotenusa é de {comprimento_da_hipotenusa:.2f}.')

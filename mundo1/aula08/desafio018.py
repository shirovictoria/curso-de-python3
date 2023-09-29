# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, cos, tan, sin
ângulo_digitado = int(input('Digite o ângulo: '))
seno = sin(radians(ângulo_digitado))
cosseno = cos(radians(ângulo_digitado))
tangente = tan(radians(ângulo_digitado))
print(f'O Ângulo digitado foi: {ângulo_digitado:.2f}. O seu seno é {seno:.2f}, o cosseno é {cosseno:.2f} e sua tangente é {tangente:.2f}.')



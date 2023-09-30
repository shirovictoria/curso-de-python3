# Crie um programa que leia um frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input('Digite uma frase: ').upper()
nova_sem_espaços = frase.replace(" ", "")
frase_ao_contrário = frase[::-1]
if(nova_sem_espaços == frase_ao_contrário):
    print(f'A frase {frase_ao_contrário} é um palíndromo!')
else:
    print(F'A frase {frase_ao_contrário} não é um palíndromo!')


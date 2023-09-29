# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
área_da_parede = largura * altura
quantidade_de_tinta = área_da_parede / 2
print(f'Uma parede {largura:.2f}X{altura:.2f} precisa de {quantidade_de_tinta:.2f} baldes de tinta para pintar toda a parede.')

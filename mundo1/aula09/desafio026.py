# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.
texto = input('Digite um texto: ').upper()
print(f'A letra A parece {texto.count("A")} vezes.')
print(f'A primeira ocorrência da palavra A tá na posição: {texto.find("A")}.')
print(f'A última ocorrência da palavra A tá na posição: {texto.rfind("A")}.')

def leiaDinheiro(msg):
    while True:
        valor = input(msg).replace(',', '.').strip()  # Substitui ',' por '.' para aceitar números decimais
        if valor.replace('.', '', 1).isdigit():
            return float(valor)
        else:
            print('Valor inválido. Digite um valor monetário válido.')
def aumentar(preco, taxa, formatar=False):
    resultado = preco + (preco * taxa / 100)
    return moeda(resultado) if formatar else resultado

def diminuir(preco, taxa, formatar=False):
    resultado = preco - (preco * taxa / 100)
    return moeda(resultado) if formatar else resultado

def dobro(preco, formatar=False):
    resultado = preco * 2
    return moeda(resultado) if formatar else resultado

def metade(preco, formatar=False):
    resultado = preco / 2
    return moeda(resultado) if formatar else resultado

def moeda(preco):
    return f'R${preco:.2f}'

def resumo(preco, aumento, reducao):
    print('-' * 30)
    print('RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao, True)}')
    print('-' * 30)
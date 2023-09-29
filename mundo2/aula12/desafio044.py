"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- A vista dinheiro / cheque: 10% de desconto
- A vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3 x ou mais no cartão: 20% de juros
"""
valor_do_produto = float(input('Digite o valor do produto: '))
print("""
    Selecione um meio de pagamento:
      [ 1 ] - A vista dinheiro/ cheque.
      [ 2 ] - A vista no cartão.
      [ 3 ] - 2 x no cartão.
      [ 4 ] - 3 x ou mais.
""")
opção_selecionada = int(input('Digite uma das opções: '))
if opção_selecionada == 1:
    desconto = (valor_do_produto * 10) / 100
    print(f'Com o desconto de 10% o produto sai por R$ {valor_do_produto - desconto}.')
elif opção_selecionada == 2:
    desconto = (valor_do_produto * 5 ) / 100
    print(f'Com o desconto de 5% o produto sai por R${valor_do_produto - desconto}.')
elif opção_selecionada == 3:
    print(f'Com parcelamento de 2 vezes, o pagamento ficou com 2x de R${valor_do_produto / 2:.2f}.')
elif opção_selecionada == 4:
    parcelamento = int(input('Digite quantas vezes você quer parcelar: '))
    juros = (valor_do_produto * 20) / 100
    valor_do_produto+=juros
    print(f'Com o parcelamento de {parcelamento} x o produto ficou R${valor_do_produto / parcelamento:.2f} por mês adicionando os 20% de juros.')
else:
    print(f'A opção selecionada {opção_selecionada} não existe.')

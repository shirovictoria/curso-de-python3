"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""# Tupla com nomes de produtos e preços
produtos_e_precos = (
    ("Produto 1", 19.99),
    ("Produto 2", 29.99),
    ("Produto 3", 9.99),
    ("Produto 4", 49.99),
    ("Produto 5", 14.99)
)
print("Produto      | Preço")
print("----------------------")
for produto, preco in produtos_e_precos:
    print(f"{produto.ljust(13)} | R$ {preco:.2f}")
total = sum(preco for _, preco in produtos_e_precos)
print("----------------------")
print(f"Total        | R$ {total:.2f}")

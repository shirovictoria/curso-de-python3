"""
    Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    A) Apenas os 5 primeiros colocados.
    B) Os últimos 4 colocados da tabela.
    C) Uma lista com os times em ordem afabética.
    D) Em que posição na tabela está o time da Chapecoense.
"""
tabela_brasileirao = (
    "Flamengo", "Palmeiras", "Atlético Mineiro", "Fortaleza", "Bragantino",
    "Corinthians", "Fluminense", "Athletico Paranaense", "Ceará", "Internacional",
    "Juventude", "Santos", "Cuiabá", "Bahia", "São Paulo",
    "Sport Recife", "América Mineiro", "Grêmio", "Vasco da Gama", "Chapecoense"
)
print("A) Os 5 primeiros colocados:")
for i in range(5):
    print(f"{i + 1}: {tabela_brasileirao[i]}")
print("\nB) Os últimos 4 colocados da tabela:")
for i in range(-4, 0):
    print(f"{len(tabela_brasileirao) + i + 1}: {tabela_brasileirao[i]}")
print("\nC) Times em ordem alfabética:")
times_em_ordem_alfabetica = sorted(tabela_brasileirao)
for time in times_em_ordem_alfabetica:
    print(time)
chapecoense_posicao = tabela_brasileirao.index("Chapecoense") + 1
print(f"\nD) Posição na tabela da Chapecoense: {chapecoense_posicao}")

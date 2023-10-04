"""
Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
# Função para cadastrar uma nova pessoa
def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    idade = input("Digite a idade da pessoa: ")
    with open("pessoas.txt", "a") as arquivo:
        arquivo.write(f"{nome}, {idade}\n")
def listar_pessoas():
    try:
        with open("pessoas.txt", "r") as arquivo:
            pessoas = arquivo.readlines()
            if not pessoas:
                print("Nenhuma pessoa cadastrada.")
            else:
                print("Pessoas cadastradas:")
                for pessoa in pessoas:
                    nome, idade = pessoa.strip().split(", ")
                    print(f"Nome: {nome}, Idade: {idade}")
    except FileNotFoundError:
        print("Nenhuma pessoa cadastrada.")
def main():
    while True:
        print("\nOpções:")
        print("1 - Cadastrar uma nova pessoa")
        print("2 - Listar todas as pessoas cadastradas")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

# Define a função add_filme que recebe uma lista (database) e os dados de um filme
def add_filme(database: list, nome: str, diretor: str, ano: int, duracao: int):
    # Cria um dicionário representando o filme com as informações fornecidas
    filme = {
        "nome": nome,  # nome do filme
        "diretor": diretor,  # nome do diretor
        "ano": ano,  # ano do lançamento do filme
        "tempo de execução": duracao  # duração do filme em minutos
    }
    # Adiciona o dicionário do filme à lista do banco de dados
    database.append(filme)
    return filme  # Retorna o filme adicionado (opcional)

# Cria uma lista vazia que funcionará como o "banco de dados" de filmes
banco_filmes = []

# Adiciona alguns filmes iniciais ao banco de dados
add_filme(banco_filmes, "Matrix", "Lana Wachowski", 1999, 136)
add_filme(banco_filmes, "Interestelar", "Christopher Nolan", 2014, 169)

# Loop interativo para cadastro de novos filmes pelo usuário
while True:
    print("\n--- Cadastro de Filme ---")
    nome = input("Nome do filme: ")
    diretor = input("Nome do diretor: ")
    ano = int(input("Ano de lançamento: "))
    duracao = int(input("Duração (em minutos): "))

    # Chama a função para adicionar o filme ao banco
    filme_adicionado = add_filme(banco_filmes, nome, diretor, ano, duracao)
    print("Filme adicionado:", filme_adicionado)

    # Pergunta ao usuário se deseja adicionar outro filme
    continuar = input("Deseja adicionar outro filme? (s/n): ").lower()
    if continuar != 's':
        break

# Exibe o conteúdo completo do banco de filmes na tela, organizado
print("\n--- Banco de Filmes Completo ---")
for i, filme in enumerate(banco_filmes, start=1):
    print(f"\nFilme {i}:")
    print(f"  Nome: {filme['nome']}")
    print(f"  Diretor: {filme['diretor']}")
    print(f"  Ano de lançamento: {filme['ano']}")
    print(f"  Duração: {filme['tempo de execução']} minutos")

def add_filme(database: list, nome: str, diretor: str, ano: int, duracao: int):
    filme = {
        "nome":nome,
        "diretor":diretor,
        "ano":ano,
        "tempo de execução":duracao
    }
    database.append(filme)
    
banco_filmes = []
add_filme(banco_filmes, "Matrix", "Lana Wachowski", 1999, 136)
add_filme(banco_filmes, "Interestelar", "Christopher Nolan", 2014, 169)

print(banco_filmes)
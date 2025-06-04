try:
    with open("aula-python/projeto python/python_aulas_john/arquivos/dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
     print("Não encontrado o arquivo")
try:
    with open("aula-python/projeto python/python_aulas_john/arquivos/dados.txt", "r") as arquivo:
       linhas = 0
       for linha in arquivo:
           linhas += 1
    print("O arquivo tem ",linhas," linhas") 
except FileNotFoundError:
    print("Arquivo não encontrado")
# minha tentativa de resolução
# texto = input("Digite um texto: ")
# with open("aula-python/projeto python/python_aulas_john/arquivos/saida.txt","x") as arquivo:
#     t = arquivo
#     t.write(texto)
#     print(t)
    
texto = input("Digite um texto: ")
try:
    with open("aula-python/projeto python/python_aulas_john/arquivos/saida.txt", "x") as arquivo:
        arquivo.write(texto)
        print("Texto salvo com sucesso!")
except FileExistsError:
    print("Erro: o arquivo 'saida.txt' já existe.")

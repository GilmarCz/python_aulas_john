try:
    with open("aula-python/projeto python/python_aulas_john/arquivos/dados.csv","r") as arquivo_entrada:
        with open("aula-python/projeto python/python_aulas_john/arquivos/dados_maior1.csv","w") as arquivo_saida:
            for linha in arquivo_entrada:
                linha = linha.replace("\n","")
                if linha:
                    partes = linha.split(",")
                    nome = partes[0]
                    idade = partes[1]
                    if len(idade) <= 3:
                        if int(idade) >= 18:
                            arquivo_saida.write(linha + "\n")
    print("Arquivo 'dados_maior1.csv' criado com sucesso")
    
except FileNotFoundError:
    print("Arquivo não encontrado")
    
except ValueError:
    print("Erro: Verifique se o arquivo está no formato correto")
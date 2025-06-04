# minha tentativa de resolução
# def frutas():
    # try:
    #     with open("frutas.csv", "r") as novo_arquivo:
    #         conteudo = {}
    #     for linha in novo_arquivo:
    #         linha = linha.replace("\n","")
    #         partes = linha.split(";")
    #         fruta = partes[0]
    #         preco = partes[1:]
    #         novo_arquivo.append(linha)
    #     print("Fruta: ",fruta)
    #     print("Preço: ",preco)    
    # except FileNotFoundError:
    #     print("Arquivo não encontrado")   

# resolução co ajuda gpt
def frutas():
    # Cria um dicionário vazio para armazenar as frutas e seus preços
    dicionario_frutas = {}

    try:
        # Tenta abrir o arquivo "frutas.csv" em modo leitura
        with open("aula-python/projeto python/python_aulas_john/arquivos/frutas.csv", "r", encoding="utf-8") as arquivo:
            # Percorre cada linha do arquivo
            for linha in arquivo:
                linha = linha.strip()  # Remove espaços em branco e quebras de linha do final

                if linha:  # Verifica se a linha não está vazia
                    partes = linha.split(";")  # Divide a linha em uma lista usando o ";" como separador

                    if len(partes) == 2:  # Verifica se a linha tem exatamente dois elementos (nome e preço)
                        nome = partes[0]  # A primeira parte é o nome da fruta

                        try:
                            # A segunda parte é o preço. Substitui vírgula por ponto (caso venha assim) e converte para float
                            preco = float(partes[1].replace(",", "."))
                            # Adiciona a fruta e seu preço ao dicionário
                            dicionario_frutas[nome] = preco
                        except ValueError:
                            # Caso o preço não possa ser convertido para float, mostra uma mensagem de erro
                            print(f"Preço inválido para a fruta '{nome}'")

        # Retorna o dicionário preenchido
        return dicionario_frutas

    except FileNotFoundError:
        # Caso o arquivo "frutas.csv" não seja encontrado, exibe uma mensagem e retorna dicionário vazio
        print("Arquivo 'frutas.csv' não encontrado.")
        return {}
print("\n",frutas(),"\n")


# codigo gpt que imprime a lista
# def frutas1():
#     try:
#         with open("aula-python/projeto python/python_aulas_john/arquivos/frutas.csv","r") as novo_arquivo:
#             conteudo = {}  # Dicionário para armazenar frutas e seus preços

#             for linha in novo_arquivo:
#                 linha = linha.strip()  # Remove espaços e quebras de linha
#                 partes = linha.split(";")  # Divide a linha em partes usando ';'

#                 if len(partes) >= 2:
#                     fruta = partes[0]
#                     preco = partes[1]
#                     conteudo[fruta] = preco  # Salva no dicionário

#             # Exibe o conteúdo
#             for fruta, preco in conteudo.items():
#                 print(f"Fruta: {fruta}")
#                 print(f"Preço: {preco}")
#                 print("-----")

#     except FileNotFoundError:
#         print("Arquivo não encontrado.")
# frutas1()

# resolução John
# def frutas3():
#     dicionario_frutas = {}
    
#     try:
#         with open("aula-python/projeto python/python_aulas_john/arquivos/frutas.csv","r") as arquivo1:
#             for linha in arquivo1:
#                 #linha = linha.replace("\n","")
#                 linha = linha.strip()
#                 if linha:
#                     dados = linha.split(";")
#                     dicionario_frutas[dados[0]] = float(dados[1])
                    
#     except FileNotFoundError:
#         print("Arquivo não encontrado")
        
#     except ValueError:
#         print("Erro ao converter o preço para float")
        
#     return dicionario_frutas
# print(frutas3())
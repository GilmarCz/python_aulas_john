# minha tentativa de resolução
# import os
# def adiciona_entrada():
#     diario = {}
#     try:
#         os.mkdir("novapasta")
#         with open("aula-python/projeto python/python_aulas_john/arquivos/diario.txt","w") as arquivo_saida:
#             data = input("Digite a data: ")
#             descricao = input(" Decrição: ")
#             if linha:
#                 partes = linha.split(",")
#                 data = partes[0]
#                 descricao = partes[1]
#                 arquivo_saida.write(linha + "\n")
#         print("entrada criada com sucesso")
#         return diario
#     except FileNotFoundError:
#         print("Arquivo não encontrado")
        
#     except ValueError:
#         print("Erro: Verifique se o arquivo está no formato correto")
#     print(diario)
# adiciona_entrada()

import os
def adiciona_entrada():
    diario = {}
    try:
        # Cria a pasta se ela não existir
        pasta = "aula-python/projeto python/python_aulas_john/arquivos"
        os.makedirs(pasta, exist_ok=True)
        # Caminho do arquivo onde as entradas serão salvas
        caminho_arquivo = os.path.join(pasta, "diario.txt")
        while True:
            # Coleta os dados da entrada
            data = input("Digite a data (ex: 03/06/2025): ")
            descricao = input("Descrição: ")
            # Adiciona ao dicionário
            diario[data] = descricao
            # Escreve no arquivo
            with open(caminho_arquivo, "a", encoding="utf-8") as arquivo_saida:
                linha = f"{data},{descricao}"
                arquivo_saida.write(linha + "\n")
            print("Entrada adicionada com sucesso.\n")
            # Pergunta se o usuário quer continuar
            continuar = input("Deseja adicionar outra entrada? (s/n): ").lower()
            if continuar != 's':
                break
        print("\nEncerrado. Conteúdo do dicionário:")
        print(diario)
        return diario
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except ValueError:
        print("Erro: Verifique se os dados estão no formato correto.")
# Executa a função
adiciona_entrada()

# Resolução John
# def adicionar_entrada_diario():
#     data = input("Data: ").strip()
#     descricao = input("Descrição: ")
    
#     entrada = {
#         "Data": data,
#         "Descrição": descricao
#     }
#     with open("aula-python/projeto python/python_aulas_john/arquivos/0diario.txt", "a", encoding="utf-8") as arquivo:
#         arquivo.write(str(entrada) + "\n")
#     print("Entrada adicionada com sucesso!")    
# adicionar_entrada_diario()
    
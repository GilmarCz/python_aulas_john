# minha tentativa de resolução
# dicionario = {}
# try:
#     with open("aula-python/projeto python/python_aulas_john/arquivos/dados.csv", "r", encoding="utf-8") as arquivo:
#         for linha in arquivo:
#             linha = linha.strip()
#             if linha:
#                 partes = linha.split(";")
#                 if len(partes) == 2:
#                 nome = partes[0]
                
#                 try:
#                     idade = int(partes[1])
#                     dicionario[nome] = idade
#                 except ValueError:
#                     print("Valores errados")
                    
#     return dicionario

#     for idade in dicionario:
#         if idade >= 18:
#             with open("aula-python/projeto python/python_aulas_john/arquivos/dados_maiores.csv", "a", encoding="utf-8") as arquivo1:
#                 dicionario1 = dicionario
#                 print(dicionario1)

# except FileNotFoundError:
#     print("Arquivo não encontrado")

def filtrar_maiores_idade():
    try:
        with open("aula-python/projeto python/python_aulas_john/arquivos/dados.csv", "r", encoding="utf-8") as entrada:
            linhas = entrada.readlines()

        with open("aula-python/projeto python/python_aulas_john/arquivos/dados_maior.csv", "w", encoding="utf-8") as saida:
            saida.write("Nome,Idade\n")  # escreve o cabeçalho no novo arquivo

            for linha in linhas[1:]:  # pula o cabeçalho
                linha = linha.strip()
                if linha:
                    partes = linha.split(",")
                    if len(partes) == 2:
                        nome = partes[0].strip()
                        try:
                            idade = int(partes[1].strip())
                            if idade >= 18:
                                saida.write(f"{nome},{idade}\n")
                        except ValueError:
                            print(f"Idade inválida: {linha}")
    except FileNotFoundError:
        print("Arquivo 'dados.csv' não encontrado.")

# Executa a função
print(filtrar_maiores_idade())


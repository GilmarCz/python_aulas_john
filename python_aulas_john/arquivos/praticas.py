# minha primeira tentativa de resolução ERRADA
# conteudo = None
# def Maior():
#     try:
#         with open("numeros.txt") as novo_arquivo:
#             for linha in novo_arquivo:
#                 print(max(linha)) 
#     except FileNotFoundError:
#         print("Não encontrado o arquivo")    
# Maior()

# resolução John
try:
    with open("numeros.txt") as arquivo:
        maior = 0
        for linha in arquivo:
            numero = int(linha)
            if numero > maior:
                maior = numero
        print("Maior número: ", maior)
except FileNotFoundError:
    print("Arquivo não encontrado")
except ValueError:
    print("Error: o arquivo contem dados que não são numeros inteiros")

# def Maior():
#     try:
#         with open("numeros.txt") as novo_arquivo:
#             numeros = []  # Lista para armazenar os números convertidos
#             for linha in novo_arquivo:
#                 linha = linha.strip()  # Remove espaços em branco e quebras de linha
#                 if linha:  # Verifica se a linha não está vazia
#                     numeros.append(int(linha))  # Converte e adiciona à lista
            
#             if numeros:  # Verifica se a lista não está vazia
#                 print("Maior número:", max(numeros))  # Mostra o maior número
#             else:
#                 print("O arquivo está vazio.")
#     except FileNotFoundError:
#         print("Arquivo 'numeros.txt' não foi encontrado.")
#     except ValueError:
#         print("O arquivo contém dados que não são números.")
#     except Exception as erro:
#         print(f"Ocorreu um erro inesperado: {erro}")

# Maior()

# def Maior():
#     try:
#         # Abre o arquivo e lê todos os números de uma vez
#         numeros = [int(linha) for linha in open("numeros.txt")]
#         print("Maior número:", max(numeros))
#     except FileNotFoundError:
#         print("Arquivo não encontrado.")
#     except ValueError:
#         print("Erro: O arquivo contém algo que não é número.")

# Maior()

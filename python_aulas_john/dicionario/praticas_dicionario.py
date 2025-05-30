# Primeira tentativa
# def histogram(palavra: str):
#     p1 = {}
#     for letra in palavra:
#         if letra not in p1:
#             p1[letra] = 0
#         p1[letra] += 1
#     return (p1 * "*")
# print(histogram("abba"))

def histogram(palavra: str):  # Define uma função que recebe uma string como argumento
    p1 = {}  # Dicionário vazio para armazenar a contagem de cada letra

    for letra in palavra:  # Percorre cada letra da string
        if letra not in p1:  # Se a letra ainda não estiver no dicionário
            p1[letra] = 0  # Inicializa a contagem com 0
        p1[letra] += 1  # Incrementa a contagem da letra

    resultado = ""  # String vazia para construir o resultado final

    for letra in p1:  # Para cada letra armazenada no dicionário
        resultado += f"{letra}: {'*' * p1[letra]}\n"  # Adiciona à string uma linha com a letra e os asteriscos correspondentes

    return resultado  # Retorna o histograma como uma string formatada

# Exibe o histograma da palavra "papagaio"
print(histogram("papagaio"))


# # Resolução John
# def histogram(texto: str):  # Define a função que recebe a string como parâmetro
#     contagem = {}  # Cria um dicionário vazio para contar as ocorrências

#     for letra in texto:  # Percorre cada letra da string
#         if letra in contagem:  # Se a letra já estiver no dicionário
#             contagem[letra] += 1  # Incrementa sua contagem
#         else:
#             contagem[letra] = 1  # Caso contrário, inicia a contagem com 1

#     for letra in contagem:  # Percorre o dicionário resultante
#         print(letra + ": " + "*" * contagem[letra])  # Exibe a letra seguida de asteriscos representando sua quantidade

# # Chama a função com a string "abbbaaccc"
# histogram("abbbaaccc")

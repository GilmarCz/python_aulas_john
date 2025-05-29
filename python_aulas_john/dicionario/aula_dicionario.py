# Dicionário

# Usado para armazenar dados no formato: Chave:valor
# São ordenados
# Mutáveis
# Não permitem elementos duplicados

# meu_dicionario = {}
# meu_dicionario["apina"] = "macaco"
# meu_dicionario["nome"] = "John"

# print(meu_dicionario)
# print(meu_dicionario["nome"])

# palavra = input("Digite uma palavra: ")

# if palavra in meu_dicionario:
#     print("Tradução: ", meu_dicionario[palavra])
# else:
#     print("Palavra não encontrada")
    

# resultado = {}
# resultado["maria"] = 5
# resultado["julia"] = 10

# soma = resultado["maria"] + resultado["julia"]

# Imprimir chave:valor
# dicionario = {}
# dicionario["apina"] = "Macaco"
# dicionario["banana"] = "Amarela"
# dicionario["cembalo"] = "Cravo"

# for chave in dicionario:
#     print("Chave:", chave)
#     print("Valor:",dicionario[chave])
    
# Popular
lista_palavras = [
  "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
  "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
  "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
]

def contagens(minha_lista):
    palavras = {}    
    for palavra in minha_lista:
        if palavra not in palavras:
            palavras[palavra] = 0
        palavras[palavra] += 1
    return palavras
print(contagens(lista_palavras))
            
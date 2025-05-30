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
# lista_palavras = [
#   "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
#   "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
#   "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
# ]

# def contagens(minha_lista):
#     palavras = {}    
#     for palavra in minha_lista:
#         if palavra not in palavras:
#             palavras[palavra] = 0
#         palavras[palavra] += 1
#     return palavras
# print(contagens(lista_palavras))
    
# Deletando chaves 
# del
# staff = {"Alan":"Professor", "Emily":"Aluna", "Davi":"Professor"}     
# print(staff) 
# del staff["Alan"]  
# print(staff)

# Pop armazena o valor deletado, podemos gravar em uma variável
# pop
# deletado = staff.pop("Emily")
# print(deletado)

# Estrutura dados com Dicionário
Pessoa1 = {"nome":"Peppa Pig", "altura":100, "peso":50, "idade":10}
Pessoa2 = {"nome":"Lilo Stitch", "altura":110, "peso":40, "idade":20}
Pessoa3 = {"nome":"Ariel", "altura":150, "peso":70, "idade":18}

Pessoas = [Pessoa1, Pessoa2, Pessoa3]

# for pessoa in Pessoas:
#     print(pessoa["nome"])
for pessoa in Pessoas:
    print(f"Nome: {pessoa["nome"]}")
    print(f"Idade: {pessoa["idade"]} anos")
    print(f"Altura: {pessoa["altura"]} cm")
    print(f"Peso: {pessoa["peso"]} kg\n")
    
    
altura_combinada = 0
for pessoa in Pessoas:
    altura_combinada += pessoa["altura"]
    
print(f"{altura_combinada} cm")
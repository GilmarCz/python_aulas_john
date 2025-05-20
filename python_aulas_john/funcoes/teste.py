# numero = int(input("Qual o número: "))
# contador = 0
# elemento = ""
# coluna = 0

# while contador < numero:
#     print("linha"*numero)
#     contador += 1

# while contador < numero:
#     while contador < numero:
#         elemento += "letra"
#         coluna += 1
#     print(elemento)
#     contador += 1

# numero = int(input("Qual o número: "))
# linha = 0

# while linha < numero:  # Quantidade de linhas que serão repetidas
#     coluna = 0
#     elemento = ""
    
#     while coluna < numero:   # Quantas vezes irá repetir dentro do primeiro while
#         if (linha + coluna) % 2 == 0:
#             elemento += "0"
#         else:
#             elemento += "1"
#         coluna += 1
    
#     print(elemento)
#     linha += 1

def cumprimentar (nome):
    print(f"Olá, {nome}")
    
def cumprimentar_vezes (nome, vezes):
    while vezes > 0:
        cumprimentar(nome)
        vezes -= 1
        
cumprimentar_vezes("Maria", 5)
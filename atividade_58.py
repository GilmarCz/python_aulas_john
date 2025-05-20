# texto = input("Palavra: ")
# print("*"*30)
# if len(texto) < 30 and len(texto)%2 != 0:
#     print("* "+texto+" *")
#     print("*"*30)
# else:
#     print("* "+texto+" *")

# texto = input("Palavra: ")
# print("*" * 30)

# if len(texto) < 30:
#     # Calcula os espaços para centralizar
#     espacos = (28 - len(texto)) // 2  # 28 = 30 - 2 (os asteriscos laterais)
    
#     # Monta a linha centralizada
#     linha_centralizada = "*" + " " * espacos + texto + " " * espacos
    
#     # Ajuste para caso o comprimento seja ímpar
#     if (28 - len(texto)) % 2 != 0:
#         linha_centralizada += " "  # Adiciona um espaço extra à direita
    
#     linha_centralizada += "*"
    
#     print(linha_centralizada)
#     print("*" * 30)
# else:
#     # Se for maior que 30, corta e mostra entre asteriscos
#     print("* " + texto[:26] + " *")

texto = input("Digite uma palavra ou frase: ")
#largura total
largura_total = 30
#Linhas do topo e do rodapé
linha_borda = "*" * largura_total
#aqui é o espaço total disponivel tirando o tamanho da palavra
espacos_total = largura_total - len(texto)
#aqui é quanto de espaço para esquerda que é o espaco_total dividido por 2
espacos_esquerda = espacos_total // 2 
#aqui é o espaço da direita
espacos_direita = espacos_total - espacos_esquerda-2
#aqui monta a linha central

if len(texto) % 2 == 0:    
    linha_central = "*" + " " * espacos_esquerda + texto + " " * espacos_direita + "*"
else:
    linha_central = "*"+ texto + "*"


print(linha_borda)
print(linha_central)
print(linha_borda)


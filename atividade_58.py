# texto = input("Palavra: ")
# print("*"*30)
# if len(texto) < 30 and len(texto)%2 != 0:
#     print("* "+texto+" *")
#     print("*"*30)
# else:
#     print("* "+texto+" *")

texto = input("Palavra: ")
print("*" * 30)

if len(texto) < 30:
    # Calcula os espaços para centralizar
    espacos = (28 - len(texto)) // 2  # 28 = 30 - 2 (os asteriscos laterais)
    
    # Monta a linha centralizada
    linha_centralizada = "*" + " " * espacos + texto + " " * espacos
    
    # Ajuste para caso o comprimento seja ímpar
    if (28 - len(texto)) % 2 != 0:
        linha_centralizada += " "  # Adiciona um espaço extra à direita
    
    linha_centralizada += "*"
    
    print(linha_centralizada)
    print("*" * 30)
else:
    # Se for maior que 30, corta e mostra entre asteriscos
    print("* " + texto[:26] + " *")
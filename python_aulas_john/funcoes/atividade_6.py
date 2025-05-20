def linha():
    num = int(input("Número: "))
    pal = input("Palavra: ")
    
    if len(pal) == 0:
        texto = "*"
    else:
        texto = pal[0]
    
    print(texto * num)

# Chamada correta (sem argumentos)
linha()
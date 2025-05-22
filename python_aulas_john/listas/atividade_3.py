def verificacao():    
    lista= []
    while len(lista) < 5:
        adiciona = input("Digite 5 nomes: ")
        if adiciona in lista:
            print("Esse nome já esta na lista")
        else:
            lista.append(adiciona)
            print(lista)
    print("Lista completa")
    return lista
print(verificacao())
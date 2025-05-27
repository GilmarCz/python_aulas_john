def lista_compras():
    print("Lista interativa de compras\n(Digite 'sair' para sair da lista e 'remover' para tirar um item)")
    lista = []
    while True:       
        compra = input("Digite um item para comprar: ")
        if compra == "sair":
            break
        elif compra == "remover":
            deletar = input("Qual item deseja remover? ")
            if deletar in lista:
                lista.remove(deletar)
                print(f"Item '{deletar}' removido da lista.")
            else:
                print(f"Item '{deletar}' não encontrado na lista.")    
        else:
            lista.append(compra)
    # lista.sort()
    # print(lista)
    
    compras_ordenadas = sorted(lista)
    i=0
    print("Lista:")
    while i < len(compras_ordenadas):
        print(compras_ordenadas[i])
        i+=1
    
lista_compras()        
